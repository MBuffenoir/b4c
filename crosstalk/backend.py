###############################################################################
##
##  Copyright (C) 2014, Tavendo GmbH and/or collaborators. All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions are met:
##
##  1. Redistributions of source code must retain the above copyright notice,
##     this list of conditions and the following disclaimer.
##
##  2. Redistributions in binary form must reproduce the above copyright notice,
##     this list of conditions and the following disclaimer in the documentation
##     and/or other materials provided with the distribution.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
##  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
##  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
##  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
##  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
##  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
##  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
##  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
##  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
##  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##
###############################################################################

from twisted.internet.defer import inlineCallbacks

from os import environ

#for python 2 or 3 detection
import sys

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

from autobahn.wamp.types import RegisterOptions

from twisted.python import log, util

from djangoadmin.settings import CROSSBAR_CELERY_TASKS, GET_LIST_DATA_TASKS, GET_DETAIL_DATA_TASKS, CREATE_DATA_TASKS, CROSSBAR_DOMAIN

from crosstalk.utils import import_celery_tasks


#this isn't very nice but it works.  cleanup!
ns = {} #namespace for call_*_task functions
ns_get_list = {} #namespace for data_get_list_task
ns_get_detail = {} #namespace for data_get_detail_task
ns_create = {} # namespace for data_create

ns = import_celery_tasks(ns, CROSSBAR_CELERY_TASKS)

import_get_list_code = compile('from crosstalk.tasks import data_get_list_task', '<string>', 'exec')
import_get_detail_code = compile('from crosstalk.tasks import data_get_detail_task', '<string>', 'exec')
import_create_code = compile('from crosstalk.tasks import data_create_task', '<string>', 'exec')

returnfunc = compile('def returnData(d):    return d', '<string>', 'exec')

if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    exec(import_get_list_code, ns_get_list)
    exec(import_get_detail_code, ns_get_detail)
    exec(import_create_code, ns_create)

    exec(returnfunc, ns)
    exec(returnfunc, ns_get_list)
    exec(returnfunc, ns_get_detail)
    exec(returnfunc, ns_create)
    
else:
    # Python 2 code in this block
    exec import_get_list_code in ns_get_list 
    exec import_get_detail_code in ns_get_detail 
    exec import_create_code in ns_create 

    exec returnfunc in ns
    exec returnfunc in ns_get_list
    exec returnfunc in ns_get_detail
    exec returnfunc in ns_create


class AppSession(ApplicationSession):
    #pass
    @inlineCallbacks
    def onJoin(self, details):
               
        # REGISTER celery tasks as procedures for remote calling
        #
        for t in CROSSBAR_CELERY_TASKS:
            code = compile('%s = lambda *args, **kwargs: %s.delay(*args, caller_session_id=kwargs["caller_details"].caller).addCallback(returnData)' % (t.get('cb_rpc'), t.get('task')), '<string>', 'exec')
            if (sys.version_info > (3, 0)):
                exec code in ns
            else:
                exec(code, ns)
            
            reg = yield self.register(ns[t.get('cb_rpc')], 'com.example.%s' % t.get('cb_rpc'), options=RegisterOptions(details_arg = 'caller_details'))
            print("procedure %s() registered" % t.get('cb_rpc'))

        ## Register DATA_GET_LIST tasks
        for t in GET_LIST_DATA_TASKS:
            cb_rpc = 'get_list_%s%s' % (t.get('app'), t.get('model'))
            code = compile('%s = lambda *args, **kwargs: data_get_list_task.delay("%s", "%s", %s, %s, filter=args[0], caller_session_id=kwargs["caller_details"].caller).addCallback(returnData)' % (cb_rpc, t.get('app'), t.get('model'), t.get('fields'), t.get('filter_fields')), '<string>', 'exec')
            
            if (sys.version_info > (3, 0)):
                exec code in ns_get_list
            else:
                ecec(code, ns_get_list)
    
            reg = yield self.register(ns_get_list[cb_rpc], 'com.example.%s' % cb_rpc, options=RegisterOptions(details_arg = 'caller_details'))
            print("procedure %s() registered" % cb_rpc)

        ## Register DATA_GET_DETAIL tasks
        for t in GET_DETAIL_DATA_TASKS:
            cb_rpc = 'get_detail_%s%s' % (t.get('app'), t.get('model'))
            code = compile('%s = lambda item_id, **kwargs: data_get_detail_task.delay("%s", "%s", %s, item_id, caller_session_id=kwargs["caller_details"].caller).addCallback(returnData)' % (cb_rpc, t.get('app'), t.get('model'), t.get('fields')), '<string>', 'exec')    
            
            if (sys.version_info > (3, 0)):
                exec code in ns_get_detail
            else:
                exec(code, ns_get_detail)
    
            reg = yield self.register(ns_get_detail[cb_rpc], 'com.example.%s' % cb_rpc, options=RegisterOptions(details_arg = 'caller_details'))
            print("procedure %s() registered" % cb_rpc)

        ## Register DATA_CREATE tasks
        for t in CREATE_DATA_TASKS:
            cb_rpc = 'create_%s%s' % (t.get('app'), t.get('model'))
            code = compile('%s = lambda *args, **kwargs: data_create_task.delay("%s", "%s", %s, create_dict=args[0], caller_session_id=kwargs["caller_details"].caller).addCallback(returnData)' % (cb_rpc, t.get('app'), t.get('model'), t.get('fields')), '<string>', 'exec')
            
            if (sys.version_info > (3, 0)):
                exec code in ns_create
            else:
                exec(code, ns_create)
    
            reg = yield self.register(ns_create[cb_rpc], 'com.example.%s' % cb_rpc, options=RegisterOptions(details_arg = 'caller_details'))
            print("procedure %s() registered" % cb_rpc)

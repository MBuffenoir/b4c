# -*- coding: utf-8 -*-
import sys

def import_celery_tasks(ns, task_dict):
    ti = []
    for t in task_dict:
        ti.append('%s.%s'%(t.get('app'), t.get('task')))
    ti_unique = list(set(ti))
    import_list = []
    for import_task in ti_unique:
        i = import_task.split('.')
        imt = 'from %s.%s import %s' % (i[0], i[1], i[2])
        importcode = compile(imt, '<string>', 'exec')
        if (sys.version_info > (3, 0)):
            exec importcode in ns
        else:
            exec(importcode, ns)

    return ns
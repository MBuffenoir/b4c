# -*- coding: utf-8 -*-
from celery.utils.log import get_task_logger

# #for crossbar(twisted)
from txcelery.defer import CeleryClient

from djangoadmin.celery import app as celery_app

#TO ACCESS DB MODELS
from django.apps import apps
from django.core import serializers


@CeleryClient
@celery_app.task
def data_get_list_task(app, model, fields, filter_fields, filter, caller_session_id):
    """
    A generic task for get_list
    """
    
    
    db = apps.get_model(app_label=app, model_name=model)
    #try:
    d = db.objects.all()
    if filter:
        #filter the filter dict by filter_fields
        filter_keys = list(set(filter_fields) & set(filter.keys()))
        if len(filter_keys) > 0:
            filter_dict = { filter_key: filter[filter_key] for filter_key in filter_keys }
            d = d.filter(**filter_dict)
    #except db.DoesNotExist:
        #dosomething
    return serializers.serialize("json", d, fields=fields) # fields

@CeleryClient
@celery_app.task
def data_get_detail_task(app, model, fields, item_id, caller_session_id):
    """
    A generic task for get_detail
    """
    db = apps.get_model(app_label=app, model_name=model)
    d = db.objects.get(id=item_id)
    return serializers.serialize("json", d, fields=fields) # fields

@CeleryClient
@celery_app.task
def data_create_task(app, model, fields, create_dict, caller_session_id):
    """
    A generic task for create
    """    
    
    db = apps.get_model(app_label=app, model_name=model)
    #try:
    if create_dict:
        #filter the filter dict by filter_fields
        create_keys = list(set(fields) & set(create_dict.keys()))
        if len(create_keys) > 0:
            create_dict_s = { create_key: create_dict[create_key] for create_key in create_keys }
            d = db.objects.create(**create_dict_s)
            return d.id
        else:
            return False
    #except db.DoesNotExist:
        #dosomething
#! coding: utf-8
from celery.task import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task()
def create_property_on_zona_prop(prop):
    logger.info('Creating property on ZonaProp: %s' % prop)
    # TODO: Implement


@task()
def update_property_on_zona_prop(prop):
    logger.info('Updating property on ZonaProp: %s' % prop)
    # TODO: Implement


@task()
def delete_property_on_zona_prop(prop):
    logger.info('Deleting property on ZonaProp: %s' % prop)
    # TODO: Implement
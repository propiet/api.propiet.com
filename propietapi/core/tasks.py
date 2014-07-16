#! coding: utf-8
from celery.task import task
from celery.utils.log import get_task_logger
from django.conf import settings
from core.models import UserProfile
from django.template import Context
from django.template.loader import render_to_string


logger = get_task_logger(__name__)


@task()
def create_post_on_zona_prop(post):
    logger.info('Creating post on ZonaProp: %s' % post.property)

    prop = post.property
    specs = {}
    list_specs = {}
    ambiences = []
    services = []
    features = []
    specs['luminosidad'] = prop.get_zonaprop_lightness()
    specs['orientacion'] = prop.get_zonaprop_orientation()
    specs['disposicion'] = prop.get_zonaprop_disposition()
    specs['cantidad_ambientes'] = prop.get_zonaprop_quantity_ambiences()
    specs['cantidad_banios'] = prop.get_zonaprop_quantity_bathrooms()
    specs['cant_cocheras'] = prop.get_zonaprop_quantity_garages()
    specs['cobertura_cocheras'] = prop.get_zonaprop_garage_coverage()
    specs['tipo_edificio'] = prop.get_zonaprop_building_type()
    specs['estado_gral_edificio'] = prop.get_zonaprop_building_status()
    specs['categoria_edificio'] = prop.get_zonaprop_building_category()
    specs['cantidad_ascensores'] = prop.get_zonaprop_quantity_elevators()
    specs['tipo_techo'] = prop.get_zonaprop_roof_type()
    specs['tipo_techo_industrial'] = prop.get_zonaprop_industrial_roof_type()
    specs['tipo_porton'] = prop.get_zonaprop_gate_type()
    specs['etapa_inmueble'] = prop.get_zonaprop_stage()
    specs['apto_profesional'] = prop.get_zonaprop_suitable_professional()
    specs['apto_credito'] = prop.get_zonaprop_suitable_credit()
    specs['uso_comercial'] = prop.get_zonaprop_commercial_usage()
    specs['ofrece_financiacion'] = prop.get_zonaprop_provides_funding()

    specs['fot'] = prop.fot
    specs['frente_terreno'] = prop.frontGround
    specs['largo_terreno'] = prop.largeGround
    specs['superficie_descubierta'] = prop.total_uncovered_meters
    specs['deptos_x_piso'] = prop.apartmentsPerFloor
    specs['cant_pisos_edificio'] = prop.quantityBuildingFloors
    specs['expensas'] = prop.expenses
    specs['altura-techo'] = prop.roofHeight
    specs['antiguedad'] = prop.antiqueness

    #Campos obligatorios para algun tipo de propiedad
    specs['hectareas'] = prop.get_zonaprop_hectares()
    specs['cantidad_ambientes'] = prop.get_zonaprop_ambiences()
    specs['superficie_total'] = prop.get_zonaprop_square_meters()
    specs['superficie_cubierta'] = prop.get_zonaprop_covered_meters()
    specs['cant_dormitorios'] = prop.get_zonaprop_bedrooms()

    for ambience in prop.ambiences.all():
        ambiences.append(ambience.get_zonaprop_ambience())
    list_specs['ambiente'] = ambiences

    for service in prop.services.all():
        services.append(service.get_zonaprop_service())
    list_specs['servicio'] = services

    for feature in prop.features.all():
        features.append(feature.get_zonaprop_feature())
    list_specs['adicional'] = features

    location_id = prop.location.get_zonaprop_cod()
    if prop.location.get_zonaprop_cod():
        other_location = None
    else:
        other_location = prop.location.address

    property_type = prop.get_zonaprop_property_type()

    images = []
    for image in post.postphoto_set.all():
        images.append(image.file.url)

    currency = post.currency.get_zonaprop_currency()
    operation_type = post.operation.get_zonaprop_operation()

    if post.agent is not None and post.agent.first_name:
        ZONAPROP_CONTACT_FIRST_NAME = post.agent.first_name
    else:
        ZONAPROP_CONTACT_FIRST_NAME = settings.ZONAPROP_CONTACT_FIRST_NAME

    if post.agent is not None and post.agent.last_name:
        ZONAPROP_CONTACT_LAST_NAME = post.agent.last_name
    else:
        ZONAPROP_CONTACT_LAST_NAME = settings.ZONAPROP_CONTACT_LAST_NAME

    if post.agent is not None and post.agent.email:
        ZONAPROP_CONTACT_MAIL = post.agent.email
    else:
        ZONAPROP_CONTACT_MAIL = settings.ZONAPROP_CONTACT_LAST_NAME

    try:
        agent_profile = UserProfile.objects.get(user=post.agent)
        if agent_profile.area_code:
            ZONAPROP_AREA_CODE = agent_profile.area_code
        else:
            ZONAPROP_AREA_CODE = settings.ZONAPROP_AREA_CODE

        if agent_profile.phone:
            ZONAPROP_PHONE_NUMBER = agent_profile.phone
        else:
            ZONAPROP_PHONE_NUMBER = settings.ZONAPROP_PHONE_NUMBER
    except UserProfile.DoesNotExist:
        ZONAPROP_AREA_CODE = settings.ZONAPROP_AREA_CODE
        ZONAPROP_PHONE_NUMBER = settings.ZONAPROP_PHONE_NUMBER

    template_vars = {
        'property_id': prop.id,
        'property_type': property_type,
        'location_id': location_id,
        'other_location': other_location,
        'specs': specs,
        'list_specs': list_specs,
        'description': post.description,
        'subtitle': post.title,
        'images': images,
        'video': post.video_url,
        'price': int(post.price),
        'currency': currency,
        'operation_type': operation_type,
        'ZONAPROP_PROVEEDOR': settings.ZONAPROP_PROVEEDOR,
        'ZONAPROP_USUARIO': settings.ZONAPROP_USUARIO,
        'ZONAPROP_PASSWORD': settings.ZONAPROP_PASSWORD,
        'ZONAPROP_HORARIO_ATENCION': settings.ZONAPROP_HORARIO_ATENCION,
        'ZONAPROP_AREA_CODE': ZONAPROP_AREA_CODE,
        'ZONAPROP_PHONE_NUMBER': ZONAPROP_PHONE_NUMBER,
        'ZONAPROP_CONTACT_MAIL': ZONAPROP_CONTACT_MAIL,
        'ZONAPROP_CONTACT_FIRST_NAME': ZONAPROP_CONTACT_FIRST_NAME,
        'ZONAPROP_CONTACT_LAST_NAME': ZONAPROP_CONTACT_LAST_NAME
    }

    c = Context(template_vars)

    open('output', "w").write(render_to_string('zona_prop.xml', c).encode("utf-8"))


@task()
def update_post_on_zona_prop(post):
    logger.info('Updating post on ZonaProp: %s' % post.property)
    # TODO: Implement


@task()
def delete_post_on_zona_prop(post):
    logger.info('Deleting post on ZonaProp: %s' % post.property)
    # TODO: Implement
# -*- coding: utf-8 -*-
# Django imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import *
from django.utils import simplejson
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Tastypie imports
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpCreated
from tastypie.utils import trailing_slash 
from tastypie import fields
from tastypie.models import ApiKey
from tastypie.serializers import Serializer
# core
from core.handlers  import *
from core.constants import *
from core.models import Post,Service, Ambience, Feature, Property, Category, SubCategory, Operation, Location, UserProfile, PostPhoto
from core.forms import GetObjectForm, PropertyForm
from cities_light.models import Country, Region, City
from django.utils.translation import ugettext_lazy as _

from lxml import etree

class IntegrationResource(ModelResource):
     """ Class IntegrationResource integration of differents webs.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""
     requestHandler = RequestHandler() 

     class Meta:
        queryset = Post.objects.all()
        allowed_methods = ['post','get']
        resource_name = 'integration'

     def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/properati_create%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('properati_create'), name="api_integration_properati_create"),
            url(r"^(?P<resource_name>%s)/properati_delete%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('properati_delete'), name="api_integration_properati_delete"),
            ]
            
     def properati_delete(self,request,**kwargs):
        
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        
        if request_data:
            post = Post.objects.get(pk=request_data['post_id'])
            if post.operation.operation == "Emprendimiento":
                filename='/home/sites/api.propiet.com/propietapi/media/emprender.xml'
            else:
                filename='/home/sites/api.propiet.com/propietapi/media/propiedades.xml'
            
            parser = etree.XMLParser(strip_cdata=False)
            xml = etree.parse(filename, parser)
            root = xml.getroot()
            for ad in root.findall('ad'):
                if int(ad.find("id").text) == request_data['post']['id']:
                    root.remove(ad)
                    with open(filename,'w') as f:
                        test = f.write(etree.tostring(xml,encoding='utf-8'))
                    return self.create_response(request, {'response':{'success': True},})       
                else:
                    return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized) 

     def properati_create(self,request,**kwargs):
        
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        
        URL = "http://propiet.com/publicacion/"
        URL_IMAGE = "http://api.propiet.com/media/"

        if request_data:
            
            post = Post.objects.get(pk=request_data['post_id'])
                             
            if post:
                
                property = Property.objects.get(pk=post.property.pk)
                category =  Category.objects.get(pk=post.category_id)
                sub_category = SubCategory.objects.get(pk=property.subcategory_id)
                location = Location.objects.get(property=post.property.pk)

                            
                if post.operation.operation == "Emprendimiento":

                    filename = '/home/sites/api.propiet.com/propietapi/media/emprender.xml'
                    parser = etree.XMLParser(strip_cdata=False)
                    xml = etree.parse('/home/sites/api.propiet.com/propietapi/media/emprender.xml', parser)
                    ads = xml.getroot()
                    ad = etree.Element("ad")

                    post_id = etree.SubElement(ad,"id")
                    post_id.text = etree.CDATA(str(post.id)) 
                    post_title = etree.SubElement(ad,"title")
                    post_title.text = etree.CDATA(post.title)
                    post_content = etree.SubElement(ad,"content")
                    post_content.text = etree.CDATA(post.description)
                    
                    #ADDRESS
                    
                    post_address = etree.SubElement(ad,"address")
                    post_address.text = etree.CDATA(location.address)

                    #REGION

                    post_region = etree.SubElement(ad,"region")
                    post_region.text = etree.CDATA(post.region.name)

                    #AGENCY INFORMATION
                    agency = etree.SubElement(ad,"agency")

                    #id
                    agency_id = etree.SubElement(agency,"id")
                    agency_id.text = etree.CDATA(str(5851))
                    #name
                    agency_name = etree.SubElement(agency,"name")
                    agency_name.text = etree.CDATA("Propiet")
                    #phone
                    agency_phone = etree.SubElement(agency,"phone")
                    agency_phone.text = etree.CDATA("011-4706-3466")
                    #email
                    agency_email = etree.SubElement(agency,"email")
                    agency_email.text = etree.CDATA("contacto@propiet.com")
                    #address
                    agency_address = etree.SubElement(agency,"address")
                    agency_address.text = etree.CDATA("Av. Libertador 5851")
                    #city_area
                    agency_city_area = etree.SubElement(agency,"city_area")
                    agency_city_area.text = etree.CDATA("Belgrano")
                    #city
                    agency_city = etree.SubElement(agency,"city")
                    agency_city.text = etree.CDATA("Ciudad de Buenos Aires")
                    #region
                    agency_region = etree.SubElement(agency,"region")
                    agency_region.text = etree.CDATA("Ciudad de Buenos Aires")
                    #country
                    agency_country = etree.SubElement(agency,"country")
                    agency_country.text = etree.CDATA("Argentina")
                    #logo_url
                    agency_logo = etree.SubElement(agency,"logo_url")
                    agency_logo.text = etree.CDATA("http://www.propiet.com/bundles/nucleushubcms/images/whiteLogo.png")

                    #PICTURES
                    pictures = etree.SubElement(ad,"pictures")

                    photos = PostPhoto.objects.filter(post=post.pk)
                    photo_first = True;
                    if photos:
                        for photo in photos:
                            if photo_first:
                                photo_file = etree.SubElement(pictures,"picture", featured = "true")
                                photo_first = False
                            else:
                                photo_file = etree.SubElement(pictures,"picture")
                            photo_file.text = etree.CDATA(URL_IMAGE+str(photo.file))


                     #city_area
                    post_city_area = etree.SubElement(ad,"city_area")
                    post_city_area.text = etree.CDATA(location.region.name)

                    #city
                    post_city = etree.SubElement(ad,"city")
                    post_city.text = etree.CDATA(location.city.name)

                    #Amenities
                    amenities = property.features.all()
                    if amenities:
                        post_amenities = etree.SubElement(ad,"amenities")
                        for amenitie in amenities:
                            post_amenitie = etree.SubElement(post_amenities,"amenitie")
                            amenitie_type = ""
                            if amenitie.name == "Aire Acondicionado":
                                amenitie_type = "Air Conditioner"
                            if amenitie.name == "Alarma":
                                amenitie_type = "Alarm"
                            if amenitie.name == "Calefacción":
                                amenitie_type = ""
                            if amenitie.name == "Cancha deportes":
                                amenitie_type = "Sport field"
                            if amenitie.name == "Gimnasio":
                                amenitie_type == "Gym"
                            if amenitie.name == "Hidromasaje":
                                amenitie_type = "Hidromassage"
                            if amenitie.name == "Laundry":
                                amenitie_type = "Laundry"
                            if amenitie.name == "Parilla":
                                amenitie_type = "Barbecue"
                            if amenitie.name == "Piscina":
                                amenitie_type = "Swimming Pool"
                            if amenitie.name == "Quincho":
                                amenitie_type = "Barbecue"
                            if amenitie.name == "Sala de Juegos":
                                amenitie_type = "Play Room"
                            if amenitie.name == "Sauna":
                                amenitie_type = "Sauna"
                            if amenitie.name == "Solarium":
                                amenitie_type = "Solarium"
                            if amenitie.name == "SUM":
                                amenitie_type = "Multipurpose Room"
                            if amenitie.name == "Vigilancia":
                                amenitie_type = "V"
                            post_amenitie.text = etree.CDATA(amenitie_type)

                    #Servicios
                    services = property.services.all()

                    if services:
                        post_servicies = etree.SubElement(ad,"services")
                        for service in services:
                            post_service = etree.SubElement(post_servicies,"service")
                            if service.name == "Agua corriente":
                                service_type = "Water"
                            if service.name == "Desagüe cloacal":
                                service_type = ""
                            if service.name == "Gas Natural":
                                service_type = "Natural Gas"
                            if service.name == "Internet":
                                service_type = "Internet"
                            if service.name == "Luz":
                                service_type = "Electricity"
                            if service.name == "Pavimento":
                                service_type = ""
                            if service.name == "Teléfono":
                                service_type = "Phone Line"
                            if service.name == "Video Cable":
                                service_type = "Cable"
                            post_service.text = etree.CDATA(service_type)
                    ads.append(ad)

                    with open(filename,'w') as f:
                        test = f.write(etree.tostring(ads,encoding='utf-8'))
                else:
                    filename='/home/sites/api.propiet.com/propietapi/media/propiedades.xml'
                    parser = etree.XMLParser(strip_cdata=False)
                    xml = etree.parse(filename, parser)
                    ads = xml.getroot()
                    ad = etree.Element("ad")

                    post_id = etree.SubElement(ad,"id")
                    post_id.text = etree.CDATA(str(post.id))
                    post_url = etree.SubElement(ad,"url")
                    post_url.text = etree.CDATA(URL+str(post.id)+"-"+post.title)
                    post_title = etree.SubElement(ad,"title")
                    post_title.text = etree.CDATA(post.title)
                    post_content = etree.SubElement(ad,"content")
                    post_content.text = etree.CDATA(post.description)

                    #TYPE CONVERTION
                    if (post.operation.operation == "Alquiler"):
                        oper_text = "for rent"
                    elif(post.operation.operation == "Venta"):
                        oper_text = "for sale"
                    else:
                        oper_text = " "

                    post_type = etree.SubElement(ad,"type")
                    post_type.text = etree.CDATA(oper_text)

                    #PROPERTY TYPE 
                    
                    if category:
                        pr_type = category.name
                        spr_type = sub_category.name
                        if(pr_type == "Departamentos"):
                            cate_text = "apartament"
                        elif(pr_type == "Casas"):
                            cate_text = "house"
                        elif(pr_type == "PH"):
                            cate_text = "ph"
                        elif(pr_type == "Countries y Barrios cerrados"):
                            if(spr_type == "Terreno"):
                                cate_text = "country"
                            elif(spr_type == "Casa"):
                                cate_text = "country house"
                        elif(pr_type == "Quintas"):
                            cate_text = "farm"
                        elif(pr_type == "Terrenos y Lotes"):
                            cate_text = "lot"
                        elif(pr_type == "Campos y Chacras"):
                            cate_text = "farm"
                        elif(pr_type == "Galpones depositos y edificios industriales"):
                            cate_text  = "store"
                        elif(pr_type == "Locales comerciales"):
                            cate_text = ""
                        elif(pr_type == "Oficinas"):
                            cate_text = "office"
                        elif(pr_type == "Consultorios"):
                            cate_text == ""
                        elif(pr_type == "Cocheras"):
                            cate_text = "garage"
                    else:
                        cate_text = " "

                    post_category = etree.SubElement(ad,"property_type")
                    post_category.text = etree.CDATA(cate_text)

                    #ADDRESS
                    
                    post_address = etree.SubElement(ad,"address")
                    post_address.text = etree.CDATA(location.address)

                    #REGION

                    post_region = etree.SubElement(ad,"region")
                    post_region.text = etree.CDATA(post.region.name)

                    #AGENCY INFORMATION
                    agency = etree.SubElement(ad,"agency")

                    #id
                    agency_id = etree.SubElement(agency,"id")
                    agency_id.text = etree.CDATA(str(5851))
                    #name
                    agency_name = etree.SubElement(agency,"name")
                    agency_name.text = etree.CDATA("Propiet")
                    #phone
                    agency_phone = etree.SubElement(agency,"phone")
                    agency_phone.text = etree.CDATA("011-4706-3466")
                    #email
                    agency_email = etree.SubElement(agency,"email")
                    agency_email.text = etree.CDATA("contacto@propiet.com")
                    #address
                    agency_address = etree.SubElement(agency,"address")
                    agency_address.text = etree.CDATA("Av. Libertador 5851")
                    #city_area
                    agency_city_area = etree.SubElement(agency,"city_area")
                    agency_city_area.text = etree.CDATA("Belgrano")
                    #city
                    agency_city = etree.SubElement(agency,"city")
                    agency_city.text = etree.CDATA("Ciudad de Buenos Aires")
                    #region
                    agency_region = etree.SubElement(agency,"region")
                    agency_region.text = etree.CDATA("Ciudad de Buenos Aires")
                    #country
                    agency_country = etree.SubElement(agency,"country")
                    agency_country.text = etree.CDATA("Argentina")
                    #logo_url
                    agency_logo = etree.SubElement(agency,"logo_url")
                    agency_logo.text = etree.CDATA("http://www.propiet.com/bundles/nucleushubcms/images/whiteLogo.png")

                    #PRICE
                    if (post.currency.name == "Dólares"):
                        curr = "USD"
                    elif(post.currency.name == "Pesos"):
                        curr = "ARS"
                    else:
                        curr = ""
                    post_price = etree.SubElement(ad,"price", currency = curr)
                    post_price = etree.CDATA(str(post.price))

                    #AGENT
                    agent = etree.SubElement(ad,"agent")

                    user = User.objects.get(pk=post.agent.pk)
                    user_profile = UserProfile.objects.get(pk=post.agent.pk)

                    #email
                    agent_mail = etree.SubElement(agent,"email")
                    agent_mail.text = etree.CDATA(user.email)
                    #name
                    agent_name = etree.SubElement(agent,"name")
                    agent_name = etree.CDATA(user_profile.agency_name)
                    #phone
                    agent_phone = etree.SubElement(agent,"phone")
                    agent_phone.text = etree.CDATA(user_profile.phone)

                    #PICTURES
                    pictures = etree.SubElement(ad,"pictures")

                    photos = PostPhoto.objects.filter(post=post.pk)
                    photo_first = True;
                    if photos:
                        for photo in photos:
                            if photo_first:
                                photo_file = etree.SubElement(pictures,"picture", featured = "true")
                                photo_first = False
                            else:
                                photo_file = etree.SubElement(pictures,"picture")
                            photo_file.text = etree.CDATA(URL_IMAGE+str(photo.file))

                    #date
                    post_date = etree.SubElement(ad,"date")
                    post_date.text = etree.CDATA(str(post.creation_date.date()))
                    
                    #city_area
                    post_city_area = etree.SubElement(ad,"city_area")
                    post_city_area.text = etree.CDATA(location.region.name)

                    #city
                    post_city = etree.SubElement(ad,"city")
                    post_city.text = etree.CDATA(location.city.name)

                    #floor_number
                    if post.property.floorNumber:
                        post_floor_number = etree.SubElement(ad,"floor_number")
                        post_floor_number.text = etree.CDATA(str(post.property.floorNumber))
                    #floor_area
                    if post.property.total_covered_meters:
                        post_floor_area = etree.SubElement(ad,"floor_area")
                        post_floor_area.text = etree.CDATA(str(post.property.total_covered_meters)) 
                    #floor_area_open
                    if post.property.total_uncovered_meters:
                        post_floor_area_open = etree.SubElement(ad, "floor_area_open")
                        post_floor_area_open.text = etree.CDATA(str(post.property.total_uncovered_meters))
                    #rooms
                    if post.property.quantityAmbiences:
                        post_rooms = etree.SubElement(ad,"rooms")
                        post_rooms.text = etree.CDATA(str(post.property.quantityAmbiences))
                    #bedrooms
                    if post.property.quantityBedrooms:
                        post_bedrooms = etree.SubElement(ad,"bedrooms")
                        post_bedrooms.text = etree.CDATA(str(post.property.quantityBedrooms))            
                    #bathrooms
                    if post.property.quantityBathrooms:
                        post_bathrooms = etree.SubElement(ad,"bathrooms")
                        post_bathrooms.text = etree.CDATA(str(post.property.quantityBathrooms))
                    #condition
                    

                    #is_furnished
                    if property.ambiences.filter(name="Amoblado"):
                        post_furnished = etree.SubElement(ad,"is_furnished")
                        post_furnished.text = etree.CDATA("1")
                    
                    #parking
                    if post.property.quantityGarages:
                        post_parking = etree.SubElement(ad,"parking")
                        post_parking.text = etree.CDATA(str(1))

                    ambientes = property.ambiences.all()
                    for ambiente in ambientes:
                        if ambiente == "Patio":
                            #patio
                            post_patio = etree.SubElement(ad,"patio")
                            post_patio.text = etree.CDATA("1")
                        if ambiente == "Terraza":
                            #terrace
                            post_terraza = etree.SubElement(ad,"terrace")
                            post_terraza.text = etree.CDATA("1")
                        if ambiente == "Balcón":
                            #balcony
                            post_balcony = etree.SubElement(ad,"balcony")
                            post_balcony.text = etree.CDATA("1")                            
                    #feauters
                        #feauter
                
                    ads.append(ad)
                    
                    with open(filename,'w') as f:
                        test = f.write(etree.tostring(ads,encoding='utf-8'))
                    return self.create_response(request, {'response':{'success': True},})       
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized) 

     def is_secure(self, request):         
         #if(request.is_secure()):                
        if(self.method_check(request, allowed=['post']) and request.user.is_authenticated()
            and self.throttle_check(request) == None):            
            self.log_throttled_access(request)            
        else: 
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized) 
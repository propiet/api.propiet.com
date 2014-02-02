from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from tastypie.models import ApiKey
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpCreated
from core.models import Agency
from core.handlers import SerializationHandler, CryptHandler


class UserResourceTest(TestCase):
    """ Test Case for User End Point
        Perform Actions: Authentication, Logout
        @author: Lionel Cuevas <lionel@hoopemedia.com> """

    fixtures = ['core.json']
    serializer = SerializationHandler()
    crypt = CryptHandler()            

    def setUp(self):
        super(UserResourceTest, self).setUp()
        """ setUp Initial data, Headers and Security
            @author: Lionel Cuevas <lionel@hoopemedia.com> """
        self.password = 'test_pwd'
        #self.client = Client(enforce_csrf_checks=False)
        self.client = Client()
        self.user = User.objects.get(pk=4)
        self.user.set_password(self.password)
        self.user.save()
        self.username = self.user.username
        user = authenticate(username=self.username, password=self.password)
        login = self.client.login(username=self.username, password=self.password)
        api_key = ApiKey.objects.get(user=user)
        self.api_key = api_key.key        
        self.agency = Agency.objects.get(user=user)
        self.agency_id = self.agency.agency_id
        self.user_group = user.groups.all()[0]
        # Authentication Headers: SSL, ApiKey
        self.auth_headers = {            
            'HTTP_AUTHORIZATION': 'ApiKey ' + self.username+':'+self.api_key,
        #    'wsgi.url_scheme': 'https'
        }

    def test_auth_user(self):
        """ Test User Authentication
            @author: Lionel Cuevas <lionel@hoopemedia.com> """
        data = '{"username":"'+ self.username +'","password":"'+self.password+'"}'
        data_enc = self.crypt.encode(data)
        response = self.client.post('/v1/user/auth/',{'request': data_enc})
        content = self.serializer.decode(response.content)
        #Check Status: HTTP 200 - OK
        self.assertEqual(response.status_code, 200)        
        #Check User Data
        self.assertEqual(content['response']['data']['user_id'], self.user.pk)
        self.assertEqual(content['response']['data']['username'], self.username)
        self.assertEqual(content['response']['data']['user_email'], self.user.email)
        self.assertEqual(content['response']['data']['user_token'], self.api_key)
        self.assertEqual(content['response']['data']['user_agency'], self.agency_id)
        self.assertEqual(content['response']['data']['user_role'], self.user_group.name)
        self.assertTrue(content['response']['success'])        
    
    def test_logout_user(self):
        """ Test User Logout
            @author: Lionel Cuevas <lionel@hoopemedia.com> """        
        response = self.client.get('/v1/user/logout/')                        
        #Check Status: HTTP 200 - OK
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        """ Test User Authentication Fail
            @author: Lionel Cuevas <lionel@hoopemedia.com> """
        data = '{"username":"'+ self.username +'","password":"'+'wrong'+'"}'
        data_enc = self.crypt.encode(data)
        self.client.get('/v1/user/logout/')
        response = self.client.post('/v1/user/auth/',{'request': data_enc})
        content = self.serializer.decode(response.content)        
        #Check Status: HTTP 403 - Forbidden
        self.assertEqual(response.status_code, 403)
        self.assertRaises(HttpForbidden)           

    def test_profile_user(self):
        """ Test User Profile
            @author: Lionel Cuevas <lionel@hoopemedia.com> """
        data = '{"data":{"user_id":"'+str(self.user.pk)+'", "first_name":"John","last_name":"Doe","email":"test_2@hoopemedia.com"}}'
        data_enc = self.crypt.encode(data)
        signature = self.crypt.get_signature(self.api_key, self.username)
        response = self.client.post('/v1/user/profile/',{'request': data_enc,'username':self.username,'api_key':self.api_key, 'signature':signature},
            **self.auth_headers)
        content = self.serializer.decode(response.content)
        #Check Status: HTTP 200 - OK
        self.assertEqual(response.status_code, 200)        
        #Check User Data        
        self.assertTrue(content['response']['success'])
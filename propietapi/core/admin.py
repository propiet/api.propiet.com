from django.contrib import admin
from core.models import UserProfile, Ambience, Category, SubCategory, Feature, Location, Post, Service, Currency, Operation
from core.models.consulting_room import ConsultingRoom
from core.models.country_house import CountryHouse
from core.models.department import Department
from core.models.field import Field
from core.models.garage import Garage
from core.models.house import House
from core.models.industrial_building import IndustrialBuilding
from core.models.land import Land
from core.models.local import Local
from core.models.office import Office
from core.models.ph import Ph
from core.models.shed import Shed
from core.models.storage import Storage
from core.models.saved_query import SavedQuery
from core.models.alert import Alert
from core.models.picture import Picture

admin.site.register(UserProfile)
admin.site.register(Ambience)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Feature)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Service)
admin.site.register(Currency)
admin.site.register(ConsultingRoom)
admin.site.register(CountryHouse)
admin.site.register(Department)
admin.site.register(Field)
admin.site.register(Garage)
admin.site.register(House)
admin.site.register(IndustrialBuilding)
admin.site.register(Land)
admin.site.register(Local)
admin.site.register(Office)
admin.site.register(Ph)
admin.site.register(Shed)
admin.site.register(Storage)
admin.site.register(Alert)
admin.site.register(SavedQuery)
admin.site.register(Operation)
admin.site.register(Picture)
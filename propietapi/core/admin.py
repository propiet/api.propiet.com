from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from core.models import *

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    max_num = 1
    min_num = 1
    extra = 1

class UserAdmin(admin.ModelAdmin):
    model = Post
    inlines = (UserProfileInline,)

class PostPhotoInline(admin.TabularInline):
    model = PostPhoto
    max_num = 5
    min_num = 1
    extra = 1

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (PostPhotoInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Site)
admin.site.register(Ambience)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Feature)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
admin.site.register(Property)
admin.site.register(Service)
admin.site.register(Currency)
admin.site.register(Operation)
from django.contrib import admin

from profiles_api import models


admin.site.register(models.UserProfile) # makes our UserProfile manager accessible with Django admin
admin.site.register(models.ProfileFeedItem)

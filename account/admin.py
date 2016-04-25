from django.contrib import admin
from account.models import profile, social
# Register your models here.


class profil_admin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(profile, profil_admin)
admin.site.register(social)

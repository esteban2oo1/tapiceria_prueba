# users_roles/admin.py
from django.contrib import admin
from users_roles.models import UsuariosRoles

@admin.register(UsuariosRoles)
class UsuariosRolesAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol')

    def username(self, instance):
        return instance.user.username
    username.short_description = 'Username'

    def email(self, instance):
        return instance.user.email
    email.short_description = 'Email'

    def first_name(self, instance):
        return instance.user.first_name
    first_name.short_description = 'First Name'

    def last_name(self, instance):
        return instance.user.last_name
    last_name.short_description = 'Last Name'


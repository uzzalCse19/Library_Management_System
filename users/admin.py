from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Role & Permissions', {
            'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

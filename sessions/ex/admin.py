from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Site_User, Tip

# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType

# content_type = ContentType.objects.get_for_model(Tip)

# permission = Permission.objects.create(
#     codename='downvote_tip',
#     name='Can downvote tip',
#     content_type=content_type,
# )


@admin.register(Site_User)
class SiteUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'reputation', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'reputation')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'reputation')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'reputation', 'password1', 'password2'),
        }),
    )

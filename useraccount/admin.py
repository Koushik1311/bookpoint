from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import UserRegistraionForm, UserEditForm

class AccountAdmin(UserAdmin):
    add_form = UserRegistraionForm
    form = UserEditForm
    model = Account
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_active',)
    readonly_fields = ('id', 'date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password',)}),
        ('Personal Details', {'fields': ('first_name', 'last_name', 'gender', 'birthday',)}),
        ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_active', 'groups', 'user_permissions',)}),
        ('Readonly Fields', {'fields': ('id', 'date_joined', 'last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
            }
        ),
    )

    search_fields = ('email', 'username')

admin.site.register(Account, AccountAdmin)
# admin.site.register(Account)

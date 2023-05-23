from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserWallet, BankAccount


# grab fields
fields = list(UserAdmin.fieldsets)
# change fields
fields[1] = (
    'Personal Info',
    {'fields': ('first_name', 'last_name', 'za_id_number', 'email')},
)
# set back fields
UserAdmin.fieldsets = tuple(fields)


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'tokens')


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_account', 'bank_name', 'phone_number')
    

admin.site.register(User, UserAdmin)
admin.site.register(UserWallet, UserWalletAdmin)
admin.site.register(BankAccount, BankAccountAdmin)

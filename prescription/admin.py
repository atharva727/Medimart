from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from prescription.models import User

class AccountAdmin (UserAdmin):
    list_display = ( 'username','email','id')
    search_fields =('email', 'username')
    readonly_fields= ('id', 'date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ('date_joined',)  
    fieldsets=()    
    ordering = ('id','username')

# Register your models here.
admin.site.register(User, AccountAdmin)
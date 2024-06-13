from django.contrib import admin
from .models import Member


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","date_of_birth","email","phone_number","address","city","postal_code","country","gender","membership_date","membership_number","active")
    list_filter = ("active",)
    readonly_fields = ('membership_number',)
    search_fields = ("last_name",)
    ordering = ("last_name",)


admin.site.register(Member,MemberModelAdmin)

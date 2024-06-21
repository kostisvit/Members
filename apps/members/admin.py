from django.contrib import admin
from .models import Member, Company, Subscription, Course


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","company","date_of_birth","email","phone_number","address","city","postal_code","country","gender","membership_date","membership_number","active")
    list_filter = ("active","company")
    readonly_fields = ('membership_number',)
    search_fields = ("last_name",)
    ordering = ("last_name",)


class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("name","address",)


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ("member","plan_name","start_date","end_date","active","subscription_number")
    readonly_fields = ('subscription_number',)


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ("title","description","created_at","updated_at")

admin.site.register(Member,MemberModelAdmin)
admin.site.register(Company)
admin.site.register(Subscription,SubscriptionModelAdmin)
admin.site.register(Course,CourseModelAdmin)

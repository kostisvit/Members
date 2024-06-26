from django.contrib import admin
from .models import Member, Course, Subscription


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ("user","company","is_student","membership_number","created_at","updated_at")
    list_filter = ("company",)
    readonly_fields = ('membership_number',)
    search_fields = ("user",)
    ordering = ("user",)


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ("member","course","is_online","start_date","end_date")
    readonly_fields = ()


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ("title","description","is_online","created_at","updated_at")

admin.site.register(Member,MemberModelAdmin)
admin.site.register(Subscription,SubscriptionModelAdmin)
admin.site.register(Course,CourseModelAdmin)


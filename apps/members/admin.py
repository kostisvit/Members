from django.contrib import admin
from .models import Member


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ("user","is_student","membership_number")
    list_filter = ("user",)
    readonly_fields = ('membership_number',)
    search_fields = ("user",)
    ordering = ("user",)


# class SubscriptionModelAdmin(admin.ModelAdmin):
#     list_display = ("member","plan_name","start_date","end_date","active","subscription_number")
#     readonly_fields = ('subscription_number',)


# class CourseModelAdmin(admin.ModelAdmin):
#     list_display = ("title","description","created_at","updated_at")

admin.site.register(Member,MemberModelAdmin)
# admin.site.register(Subscription,SubscriptionModelAdmin)
# admin.site.register(Course,CourseModelAdmin)


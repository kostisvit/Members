import random
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from company.models import Company

class Member(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default='1')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course', through='Subscription')
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    membership_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    membership_number = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.membership_number:
            self.membership_number = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            membership_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            if not Member.objects.filter(membership_number=membership_number).exists():
                break
        return membership_number
    
    def get_absolute_url(self):
        return reverse('member_edit', args=[str(self.id)])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    


class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    subscription_number = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.subscription_number:
            self.subscription_number = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            subscription_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            if not Subscription.objects.filter(subscription_number=subscription_number).exists():
                break
        return subscription_number

    # def __str__(self):
    #     return f"{self.plan_name} for {self.member.last_name}"




# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
    
#     def __str__(self):
#         return self.name
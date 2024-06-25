import random
from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from company.models import Company



class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Member(TimeStampMixin):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='1')
    is_student = models.BooleanField(default=True)
    membership_number = models.CharField(max_length=10, unique=True, blank=True)
    
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
        return f"{self.user}"


    class Meta:
        ordering = ['user']
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


class Course(TimeStampMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
class Subscription(TimeStampMixin):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} subscribed to {self.course.title}"
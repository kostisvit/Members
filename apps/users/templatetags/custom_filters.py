# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def username_from_email(value):
    """Extract the username part from an email address."""
    return value.split('@')[0]

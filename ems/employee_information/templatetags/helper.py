from django import template
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='in_group')
def in_group(user, groups):
    result = False
    groups=groups.replace(", ", ",")
    groups=groups.split(",")
    for x in groups:
        if Group.objects.filter(name=x).exists():
            group = Group.objects.get(name=x)
        else:
            group = Group.objects.none()
        result = True if group in user.groups.all() else False
        if result:
            return result
    return result 
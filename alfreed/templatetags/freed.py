from django import template
# Create your views here.



register = template.Library()

@register.filter(name='subtract')
def subtract(value,args):
    return value - args
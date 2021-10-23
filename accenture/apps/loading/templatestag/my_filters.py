from django import template


register = template.Library()

@register.filter
def isinst(value, class_str):
    if isinstance(value, class_str):
    	return True
    return False


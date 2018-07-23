from django import template
from django.template.defaultfilters import stringfilter
import binascii

register = template.Library()

@register.filter
@stringfilter
def toHex(value):
	a_bytes = bytes(value, "ascii").hex()
	s = ' '.join(a_bytes[i:i+2] for i in range(0, len(a_bytes), 2))
	return s.upper()
	

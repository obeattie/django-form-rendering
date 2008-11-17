"""Template library utilities."""
from django import template
from django.utils.translation import ugettext_lazy as _

def template_truth_test(tag_name, value):
    if not value:
        raise template.TemplateSyntaxError(_(u'%s argument must not evaluate False.') % tag_name)
    elif isinstance(value, (int, long, float)) and not value > 0:
        raise template.TemplateSyntaxError(_(u'%s argument must be greater than 0.') % tag_name)

def check_quoted(tag_name, value):
    """Checks that the value is quoted and returns it unquoted."""
    assert isinstance(value, basestring), 'value must be a string'
    if not ((value[0] == value[-1]) and (value[0] in ('\'', '"'))):
        raise template.TemplateSyntaxError(_(u'%s argument must be quoted.') % tag_name)
    else:
        value = value[1:-1]
        template_truth_test(tag_name, value)
        return value

def check_not_quoted(tag_name, value):
    """Checks the value is not quoted (the inverse of check_quoted)."""
    try:
        result = check_quoted(tag_name, value)
    except template.TemplateSyntaxError, m:
        err = m
        return value
    raise template.TemplateSyntaxError(_(u'%s argument must not be quoted.') % tag_name)

"""Template library utilities."""
from django import template
from django.utils.translation import ugettext_lazy as _

def _check_evaluates(tag_name, value):
    """Checks that the value passed evaluates to True, raising TemplateSyntaxError with an appropriate
       message if it doesn't."""
    if not value:
        raise template.TemplateSyntaxError(_(u'%s argument must not evaluate False.') % tag_name)
    elif isinstance(value, (int, long, float)) and not value > 0:
        raise template.TemplateSyntaxError(_(u'%s argument must be greater than 0.') % tag_name)

def check_quoted(tag_name, value):
    """Checks that the value is quoted and returns it unquoted."""
    assert isinstance(value, basestring), 'value must be a string'
    # Make sure that the argument is in quotes and they are the same type of quotes at either end
    if not ((value[0] == value[-1]) and (value[0] in ('\'', '"'))):
        raise template.TemplateSyntaxError(_(u'%s argument must be quoted.') % tag_name)
    else:
        # Get rid of the quotes...
        value = value[1:-1]
        # ...and check it evaluates
        _check_evaluates(tag_name, value)
        # Everything is okey-dokey :)
        return value

def check_not_quoted(tag_name, value):
    """Checks the value is not quoted (the inverse of check_quoted)."""
    # Wrap check_quoted and check that it *does* raise an error :)
    try:
        result = check_quoted(tag_name, value)
    except template.TemplateSyntaxError:
        return value
    raise template.TemplateSyntaxError(_(u'%s argument must not be quoted.') % tag_name)

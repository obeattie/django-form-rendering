"""Template library for form-related jazz."""
from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from utils import check_not_quoted

register = template.Library()

class QuickFormNode(template.Node):
    def __init__(self, form, *args, **kwargs):
        self.form = form
        return super(QuickFormNode, self).__init__(*args, **kwargs)
    
    def render(self, context):
        return render_to_string(getattr(settings, 'QUICK_FORM_TEMPLATE', 'inc/forms/quick_form.html'), {
            'form': self.form.resolve(context),
        })

@register.tag(name='form')
def quick_form(parser, token):
    """Renders the new-form instance into a ready-to-use quick form template."""
    # {% form form_object %}
    # tag ^    ^ form instance
    try:
        tokens = token.split_contents()
        assert len(tokens) == 2
    except AssertionError:
        raise template.TemplateSyntaxError, _(u'%r tag requires a form instance as its only argument.') % token.contents.split()[0]
    form = template.Variable(check_not_quoted(tokens[0], tokens[1]))
    return QuickFormNode(form=form)

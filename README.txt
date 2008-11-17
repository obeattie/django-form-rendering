This is a very simple library to help with form rendering in Django. Basically provides a template tag to render any
sort of Form instance you can throw at it into a generic template. This assists in keeping your templates maintainable,
as all of the form code will be stored in one place, and is easily changeable site-wide should the feeling take you.

To use this, you'll need to copy the templatetags directory into one of your applications. If you're not familiar with
doing this, you'll find more information at http://docs.djangoproject.com/en/dev/howto/custom-template-tags/

Next, create a generic form template (you'll find an example as quick_form.sample.html) and put it somewhere on your
template path. Then tell us where it is by setting the variable QUICK_FORM_TEMPLATE in your settings.py file. If you
don't set this, it will default to inc/forms/quick_form.html

Once you've done that, you should be good to go. So, go ahead and {% load forms %} at the top of any of your templates
where you want to render a form. Then, wherever you want the template code to be inserted, simply do
{% form <<form variable name here>> %} -- simple, eh?

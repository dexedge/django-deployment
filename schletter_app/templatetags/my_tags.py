from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="display_title")
def display_title(value, arg=""):
    """
    Construct italicization for Event titles based on content
    """
    if arg == "Concert" or value == "No title": 
        pass
    elif arg == "Oratorio" or arg == "Cantata" or arg =="Festa teatrale":
        # If the title has a tag in parentheses like (TKS),
        # leave it in plain text
        i = value.find('(')
        if i > 0:
            title = value[:i-1]
            tag = value[i:]
            value = f"<em>{title}</em> " + tag
        else:
            value = f"<em>{value}</em>"
    else:
        value = f"<em>{value}</em>"

    return value


# Adapted from:
# https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/
@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
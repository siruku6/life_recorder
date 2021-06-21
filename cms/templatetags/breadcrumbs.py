import django
from django.urls import reverse


register = django.template.Library()


@register.inclusion_tag('partials/_breadcrumb_item.html.haml')
def breadcrumb(title: str, url_name: str = None, **kwargs):
    if url_name is None:
        return {'title': title}

    link: str = reverse(url_name, kwargs=kwargs)
    return {'title': title, 'link': link, }

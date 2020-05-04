from django import template
from django.template.loader import get_template

register = template.Library()


@register.simple_tag
def admin_list_filter(cl, spec):
    try:
        tpl = get_template(cl.model_admin.change_list_filter_template)
    except:
        tpl = get_template(spec.template)
    return tpl.render({
        'title': spec.title,
        'choices': list(spec.choices(cl)),
        'spec': spec,
        'class': spec.css_class,
        'attrs': spec.attrs,
        'multiple': getattr(spec, 'multiple', False),
    })

from django.conf import settings

if 'grappelli' in settings.INSTALLED_APPS:
    TEMPLATE = 'admin/select2_change_list_filter_confirm_sidebar.html'
else:
    TEMPLATE = 'admin/select2_change_list.html'


class Select2AdminFilterMixin:
    change_list_template = TEMPLATE

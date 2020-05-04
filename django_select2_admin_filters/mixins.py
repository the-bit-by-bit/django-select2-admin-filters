from django.contrib import admin


class Select2FilterMixin:
    select2_widget_class = None
    dependent_fields = {}

    def init_select2(self):
        if self.select2_widget_class is None:
            raise ValueError('You must specify "select2_widget_class".')

    def has_output(self):
        return True

    def queryset(self, request, queryset):
        val = self.value()
        if val:
            return queryset.filter(**{self.parameter_name: val})
        return queryset


class MultipleSelect2FilterMixin:
    multiple = True

    def value_as_list(self):
        return self.value().split(',') if self.value() else []

    def queryset(self, request, queryset):
        val = self.value_as_list()
        if len(val) > 0:
            return queryset.filter(**{f'{self.parameter_name}__in': val})
        return queryset


class ModelFilterMixin(Select2FilterMixin):
    autocomplete_queryset = None
    search_fields = None

    def init_select2(self):
        super().init_select2()
        if self.autocomplete_queryset is None:
            raise ValueError('You must specify "autocomplete_queryset".')
        if self.search_fields is None:
            raise ValueError('You must specify "search_fields".')
        select2 = self.select2_widget_class(
            queryset=self.autocomplete_queryset,
            search_fields=self.search_fields,
            dependent_fields=self.dependent_fields,
        )
        select2.set_to_cache()
        self.attrs = select2.build_attrs(base_attrs={
            'id': f'id-{self.parameter_name}-filter',
            'name': f'{self.parameter_name}-filter',
            'data-parameter_name': self.parameter_name,
        })
        self.css_class = self.attrs.pop('class', '')

    def get_display_label(self, obj):
        return str(obj)

    def lookups(self, request, model_admin):
        return []


class ChoiceFilterMixin(Select2FilterMixin):
    autocomplete_choice_list = None

    def init_select2(self):
        super().init_select2()
        if self.autocomplete_choice_list is None:
            raise ValueError('You must specify "autocomplete_choice_list".')
        select2 = self.select2_widget_class(
            choices=self.autocomplete_choice_list,
        )
        self.attrs = select2.build_attrs(base_attrs={
            'id': f'id-{self.parameter_name}-filter',
            'name': f'{self.parameter_name}-filter',
            'data-parameter_name': self.parameter_name,
        })
        self.css_class = self.attrs.pop('class', '')

    def lookups(self, request, model_admin):
        return self.autocomplete_choice_list


class AdminFilterWidget(admin.SimpleListFilter):
    template = 'admin/select2_filter.html'
    parameter_name = None

    def __init__(self, request, params, model, model_admin):
        super().__init__(request, params, model, model_admin)
        self.init_select2()

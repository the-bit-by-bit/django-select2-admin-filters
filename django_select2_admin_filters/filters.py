from django_select2.forms import (
    ModelSelect2MultipleWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget)

from .mixins import (
    AdminFilterWidget, ChoiceFilterMixin, ModelFilterMixin,
    MultipleSelect2FilterMixin)


class ModelSelect2Filter(ModelFilterMixin, AdminFilterWidget):
    select2_widget_class = ModelSelect2Widget

    def get_selected(self):
        val = self.value()
        if val:
            return self.autocomplete_queryset.filter(pk=val)
        return None

    def choices(self, changelist):
        yield {
            'selected': self.value() is None,
            'value': '',
            'display': '',
        }
        for obj in self.get_selected():
            yield {
                'selected': True,
                'value': obj.pk,
                'display': self.get_display_label(obj),
            }


class MultipleModelSelect2Filter(
    ModelFilterMixin,
    MultipleSelect2FilterMixin,
    AdminFilterWidget,
):
    select2_widget_class = ModelSelect2MultipleWidget

    def get_selected(self):
        val = self.value_as_list()
        if val:
            return self.autocomplete_queryset.filter(pk__in=val)
        return []

    def choices(self, changelist):
        for obj in self.get_selected():
            yield {
                'selected': True,
                'value': obj.pk,
                'display': self.get_display_label(obj),
            }


class ChoiceSelect2Filter(ChoiceFilterMixin, AdminFilterWidget):
    select2_widget_class = Select2Widget

    def choices(self, changelist):
        selected = self.value()
        yield {
            'selected': self.value() is None,
            'value': '',
            'display': '',
        }
        for val, name in self.autocomplete_choice_list:
            yield {
                'selected': str(val) == selected,
                'value': val,
                'display': name,
            }


class MultipleChoiceSelect2Filter(
    ChoiceFilterMixin,
    MultipleSelect2FilterMixin,
    AdminFilterWidget,
):
    select2_widget_class = Select2MultipleWidget

    def choices(self, changelist):
        selected = [str(val) for val in self.value_as_list()]
        for val, name in self.autocomplete_choice_list:
            yield {
                'selected': val in selected,
                'value': val,
                'display': name,
            }

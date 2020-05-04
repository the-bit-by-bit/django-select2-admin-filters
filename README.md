
## django_select2_admin_filters

This extension is based on [django-select2](https://github.com/applegrew/django-select2) and works with or without Grappelli.

## Installation

* Install using pip

    ```
    pip install django-select2-admin-filters
    ```

* Update INSTALLED_APPS, you need too put django_select2_admin_filters after admin and django_select2

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        #
        'django_select2',
        'django_select2_admin_filters',
    ]
    ```

* Update urls.py to use model filters (refer to [django-select2 documentation](https://django-select2.readthedocs.io/en/latest/get_started.html#installation))

    ```
    path('select2/', include('django_select2.urls')),
    ```

## Filters

Filters are generally of two types, but each of them can be single or multiple selectable:
* ChoiceFilter
  * ChoiceSelect2Filter
  * MultipleChoiceSelect2Filter
* ModelFilter
  * ModelSelect2Filter
  * MultipleModelSelect2Filter

## Usage

* Use filter in your admin.py
    ```python
      from django.contrib import admin
      from libs.django_select2_admin_filters.admin import (
          Select2AdminFilterMixin)
      from libs.django_select2_admin_filters.filters import (
          ChoiceSelect2Filter, MultipleChoiceSelect2Filter,
          ModelSelect2Filter, MultipleModelSelect2Filter)
      from your_app.models import Country, Person, Profession


      class CountryFilter(ModelSelect2Filter):
          title = 'Country of residence'                 # filter's title
          parameter_name = 'country'                     # parameter used in url and by default field name of Foreign Key used to filter results
          autocomplete_queryset = Country.objects.all()  # queryset to autocomplete
          search_fields = ['name__icontains']            # fields of Country model used to filtering

          # optionally you can override queryset method
          def queryset(self, request, queryset):
              val = self.value()
              if val:
                  return queryset.filter(country_of_residence=val)
              return queryset


      class ProfessionFilter(MultipleModelSelect2Filter):
          title = 'Profession'
          parameter_name = 'profession'
          autocomplete_queryset = Profession.objects.all()
          search_fields = ['name__icontains']

          def queryset(self, request, queryset):
              val = self.value_as_list()
              if len(val) > 0:
                  return queryset.filter(professions__profession_id__in=val)
              return queryset


      class StatusFilter(ChoiceSelect2Filter):
          title = 'Status'
          parameter_name = 'status'
          autocomplete_choice_list = [    # list of choices
              (1, 'Active',),
              (2, 'Suspended',),
              (3, 'Deleted',),
          ]


      @admin.register(Person)
      class PersonAdmin(Select2AdminFilterMixin, admin.ModelAdmin):

          # change_list_template = 'admin/change_list_filter_sidebar.html' <- DON'T override change_list_template
          list_filter = (CountryFilter, ProfessionFilter, StatusFilter,) # actually you cannot mix filters with traditional filters

    ```

## TODO

* add tests
* add handling `dependent_fields`

## Author

* [Bartłomiej Żmudziński](https://github.com/bartekzmudzinski)

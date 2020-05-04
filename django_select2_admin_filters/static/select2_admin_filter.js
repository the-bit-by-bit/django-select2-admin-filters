/* global define, jQuery */
(function (factory) {
  if (typeof define === 'function' && define.amd) {
    define(['jquery'], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory(require('jquery'));
  } else {
    // Browser globals
    factory(jQuery);
  }
}(function ($) {
  'use strict'

    var buildQueryString = function(urlSearchParams) {
      var params = [];

      for(let entry of urlSearchParams.entries()) {
        params.push(entry[0] + '=' + entry[1]);
      }
      if (params.length) {
        return location.pathname + '?' + params.join('&');
      }
      return location.pathname;
    }

    // changelist: filter
    var initFilter = function(method) {
        if (!method) {
            $(".django-select2-admin-filter").change(function(){
                location.href = $(this).val();
            });
        }
        if (method === 'confirm') {
            $(".django-select2-admin-filter").change(function(){
                var parameterName = $(this).data('parameter_name');
                var isMultiple = $(this).prop('multiple');
                var val = isMultiple ? [] : null;

                if (isMultiple) {
                    $(this).children('option:selected').each(function(){
                        val.push($(this).val());
                    });
                    val = val.join(',')
                } else {
                    val = $(this).children('option:selected').first().val();
                }

                var applyFilter = $(this).closest('#changelist-filter').find('#filter-apply');
                var urlFilter = applyFilter.prop('href').split('?')[1];
                var urlParams = new URLSearchParams(urlFilter);

                if (val) {
                    urlParams.set(parameterName, val);
                } else {
                    urlParams.delete(parameterName);
                }

                var queryString = buildQueryString(urlParams)
                applyFilter.attr('href', queryString);
            });
        }
    };

    $(document).ready(function() {
        initFilter('confirm');
    });

}));

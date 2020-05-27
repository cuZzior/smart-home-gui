$( document ).ready(function() {
    $('#exp_date').daterangepicker({
        "locale": {
            "format": 'DD-MM-YYYY'
        },
        "singleDatePicker": true,
        "autoApply": true,
        "linkedCalendars": false,
    }, function(start, end, label) {
    });
});
$(function () {
    $('#updateinfobtn').bind("click", function () {
        var intemperature = $('#intemperature');
        var inhumidity = $('#inhumidity');
        $.ajax({
            type: "GET",
            dataType: "json",
            contentType: "application/json",
            url: "/sensor/temperatureinfo" ,
            // data: data,
            success: function (data, status) {
                intemperature.text(data.value);
            },
            error : function() {
                intemperature.text('FAILED');
            }
        });
         $.ajax({
            type: "GET",
            dataType: "json",
            contentType: "application/json",
            url: "/sensor/humidityinfo" ,
            // data: data,
            success: function (data, status) {
                inhumidity.text(data.value);
            },
            error : function() {
                inhumidity.text('FAILED');
            }
        });
    });
});
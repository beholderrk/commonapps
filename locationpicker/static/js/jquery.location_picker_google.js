var $ = django.jQuery;

$(document).unload(function(){
    GUnload();
});

$(document).ready(function(){
    $("input.location_picker").each(function (i) {
        var map_div = $('<div class="location_picker_map"></div>');
        var input = $(this);
        map_div.insertAfter(input);
        input.css('display','none');
        
        var lat = 55.75184940068595;
        var lng = 37.62199446582031;
        if (input.val().split(',').length == 2) {
            values = input.val().split(',');
            lat = values[0];
            lng = values[1];
        }
        var center = new google.maps.LatLng(lat,lng);

        var map = new google.maps.Map(map_div[0], {
            center: center,
            zoom: 12,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          });
//        map.addControl(new google.maps.SmallMapControl());W

        var marker = new google.maps.Marker({map: map, position: center, draggable: true});

        function onMapClick (point) {
            input.val(point.latLng.lat()+','+point.latLng.lng());
            if (marker == null) {
                marker = new google.maps.Marker({map: map, position: point.latLng, draggable: true});
            } else {
                marker.setPosition(point.latLng);
            }
        }

        google.maps.event.addListener(map, "click", onMapClick);
        google.maps.event.addListener(marker, "dragend", onMapClick);
    });
});
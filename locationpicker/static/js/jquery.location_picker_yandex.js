var $ = django.jQuery;

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
        var center = new YMaps.GeoPoint(lng, lat);

        var map = new YMaps.Map(map_div[0]);
        map.setCenter(center, 10);
        map.addControl(new YMaps.Zoom());
        map.addControl(new YMaps.TypeControl());
        map.enableScrollZoom();
        
        var marker = new YMaps.Placemark(center, { style: 'default#houseIcon', draggable: true, hasBalloon: false });
        map.addOverlay(marker);

        function onMapClick (map, point) {
            var current = point.getGeoPoint().copy();
            input.val(current.getLat()+','+current.getLng());
            if (marker == null) {
                marker = new YMaps.Placemark(current, { style: 'default#houseIcon', draggable: true, hasBalloon: false });
                map.addOverlay(marker);
            } else {
                marker.setGeoPoint(current);
            }
        }

        YMaps.Events.observe(map, map.Events.Click, onMapClick);
        YMaps.Events.observe(marker, marker.Events.DragEnd, onMapClick);
    });
});
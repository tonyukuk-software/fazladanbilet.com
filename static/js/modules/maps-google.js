jQuery(function ($) {
    if ($('.b-google-map').length > 0) {
        var cenLatlng = new google.maps.LatLng(35.362961015414056, -90.71299265625);

        var myOptions = {
            zoom: 9,
            scrollwheel: false,
            draggable: ($(document).width() > 768),
            center: cenLatlng,
            mapTypeControlOptions: {
                mapTypeIds: ['greyed']
            },
            mapTypeId: 'greyed',
            mapTypeControl: false
        };

        var map = new google.maps.Map($('.b-google-map__map-view')[0], myOptions);
        $.googleMap = map;

        // set map greyed style
        var featureOpts = [
            {
                stylers: [
                    { visibility: 'simplified' },
                    { "saturation": -100 },
                    { "lightness": 50 }
                ]
            }
        ];
        var customMapType = new google.maps.StyledMapType(featureOpts, {name: 'Greyed Style'});
        map.mapTypes.set('greyed', customMapType);

        // info window
        var infoWindowTemplate = $('.b-google-map__info-window-template');
        var infoWindow = new google.maps.InfoWindow({
            content: infoWindowTemplate.html(),
            maxWidth: infoWindowTemplate.data('width')
//            ,pixelOffset: new google.maps.Size(0, 60)
        });
        var markers = [],
        locations;
        function setMarkers() {
            // markers placement
            var markerTemplate = $('.marker-template');

            var markerIcon = markerTemplate.attr('src');
            if (markerIcon.length == 0) {
                markerIcon = {
                    path: fontawesome.markers.MAP_MARKER,
                    scale: 0.7,
                    strokeWeight: 0.2,
                    strokeColor: 'black',
                    strokeOpacity: 1,
                    fillColor: '#6c6b6b',
                    fillOpacity: 1
                };
            }
            locations = [
                {title: 'Coogee Beach', lat: 35.027332, long: -89.88796, icon: markerIcon},
                {title: 'Cronulla Beach', lat: 34.727332, long: -88.86796, icon: markerIcon},
                {title: 'Manly Beach', lat: 34.627332, long: -91.84796, icon: markerIcon},
                {title: 'Maroubra Beach', lat: 34.527332, long: -92.82796, icon: markerIcon},
                {title: 'Bondi Beach', lat: 34.927332, long: -90.90796, icon: markerIcon}
            ];

            function showHiddenLabel() {
                if (currentMark && currentMark.hasOwnProperty('markerLabel')) {
                    currentMark.markerLabel.isHidden = false;
                    currentMark.markerLabel.draw();
                }
            }


            function openInfoWindow(map, marker) {
                infoWindow.close();
                showHiddenLabel();
//                infoWindow.setContent(locations[i][0]);
                if (marker.hasOwnProperty('markerLabel')) {
                    marker.markerLabel.isHidden = true;
                    marker.markerLabel.draw();
                }
                currentMark = marker;
                infoWindow.open(map, marker);
            }


            var currentMark;


            for (var i = 0; i < locations.length; i++) {
                markers[i] = new google.maps.Marker({
                    position: new google.maps.LatLng(locations[i]['lat'], locations[i]['long']),
                    title: locations[i]['title'],
                    map: map,
                    icon: locations[i]['icon']
                });

                var markerLabel = markerTemplate.data('label');
                if (markerLabel.length > 0) {
                    var label = new MarkerLabel({
                        map: map,
                        labelClass: 'f-google-map__marker-label f-primary-b text-uppercase',
                        labelText: markerLabel
                    });
                    label.bindTo('position', markers[i]);
                    label.bindTo('visible', markers[i]);
                    label.bindTo('clickable', markers[i]);
                    label.bindTo('zIndex', markers[i]);
                    markers[i].markerLabel = label;
                }


                google.maps.event.addListener(markers[i], 'click', function () {
                    openInfoWindow(map, this);
                });

                google.maps.event.addListener(infoWindow, 'closeclick', showHiddenLabel);

            }
            // open info window
            setTimeout(function () {
                openInfoWindow(map, markers[$('.b-google-map__info-window-template').data('selected-marker')]);
            }, 1500);
        }

        setMarkers();
        function clearMarkers(){
            for (var i = 0; i < locations.length; i++) {
                markers[i].setMap(null);
            }
        }
        $('.b-google-map').on('replace_marker', function () {
            clearMarkers();
            setMarkers();
        });


    }
});
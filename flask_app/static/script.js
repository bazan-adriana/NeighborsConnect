// let map;
// let service;
// let infowindow;

// function initMap() {
//     const sanFrancisco = new google.maps.LatLng(37.7749, -122.4194);

//     infowindow = new google.maps.InfoWindow();
//     map = new google.maps.Map(document.getElementById("map"), {
//         center: sanFrancisco,
//         zoom: 15,
//     });

//     const request = {
//         query: "San Francisco Museum of Modern Art",
//         fields: ["name", "geometry"],
//     };

//     service = new google.maps.places.PlacesService(map);
//     service.findPlaceFromQuery(request, (results, status) => {
//         if (status === google.maps.places.PlacesServiceStatus.OK && results) {
//             for (let i = 0; i < results.length; i++) {
//                 createMarker(results[i]);
//             }

//             map.setCenter(results[0].geometry.location);
//         }
//     });
// }

// function createMarker(place) {
//     if (!place.geometry || !place.geometry.location) return;

//     const marker = new google.maps.Marker({
//         map,
//         position: place.geometry.location,
//     });

//     google.maps.event.addListener(marker, "click", () => {
//         infowindow.setContent(place.name || "");
//         infowindow.open(map);
//     });
// }

// window.initMap = initMap;
// google.maps.event.addDomListener(window, 'load', initialize)


// // var map, infowindow, service;

// // function initMap() {

// //     // DEFAULT MAP VIEW
// //     var usa = new google.maps.LatLng(39.757, -101.390);

// //     infowindow = new google.maps.InfoWindow();
// //     map = new google.maps.Map(
// //         document.getElementById('map'), { center: usa, zoom: 5 });
// // }

// // google.maps.event.addDomListener(window, 'load', initialize)
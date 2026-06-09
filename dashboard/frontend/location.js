// Use the same server that served the page
const API = window.location.origin;

let map;
let marker;

let currentLat = null;
let currentLng = null;

async function loadLocation() {

    try {

        const response =
            await fetch(
                `${API}/device/location-history`
            );

        if (!response.ok) {
            throw new Error(
                `HTTP Error ${response.status}`
            );
        }

        const data =
            await response.json();

        if (
            !data ||
            data.length === 0
        ) {

            document.getElementById(
                "map"
            ).innerHTML = `
                <div style="
                    color:white;
                    text-align:center;
                    padding:30px;
                ">
                    📍 No Location Data Found
                </div>
            `;

            return;
        }

        const latest =
            data[0];

        const lat =
            parseFloat(
                latest.latitude
            );

        const lng =
            parseFloat(
                latest.longitude
            );

        if (
            isNaN(lat) ||
            isNaN(lng)
        ) {

            throw new Error(
                "Invalid Coordinates"
            );
        }

        currentLat = lat;
        currentLng = lng;

        if (!map) {

            map = L.map(
                "map"
            ).setView(
                [lat, lng],
                15
            );

            L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {
                    attribution:
                        "© OpenStreetMap Contributors",
                    maxZoom: 19
                }
            ).addTo(map);

            marker = L.marker(
                [lat, lng]
            ).addTo(map);

            marker.bindPopup(
                `
                <b>💻 SecureWatch Device</b>
                <br>
                Lat: ${lat}
                <br>
                Lng: ${lng}
                `
            );

        } else {

            marker.setLatLng(
                [lat, lng]
            );

            map.setView(
                [lat, lng],
                15
            );
        }

    }

    catch (error) {

        console.error(
            "Location Load Error:",
            error
        );

        document.getElementById(
            "map"
        ).innerHTML = `
            <div style="
                color:white;
                text-align:center;
                padding:30px;
            ">
                ❌ Failed To Load Map
                <br><br>
                ${error.message}
            </div>
        `;
    }
}


function navigateToDevice() {

    if (
        currentLat === null ||
        currentLng === null
    ) {

        alert(
            "📍 Location Not Loaded Yet"
        );

        return;
    }

    window.open(
        `https://www.google.com/maps/dir/?api=1&destination=${currentLat},${currentLng}`,
        "_blank"
    );
}


// Initial Load
loadLocation();


// Auto Refresh Every 10 Seconds
setInterval(
    loadLocation,
    10000
);
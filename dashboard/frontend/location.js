// ==========================================
// SecureWatch AI
// location.js
// ==========================================



let latitude = null;
let longitude = null;

// ==========================================
// Startup
// ==========================================

window.addEventListener(
    "DOMContentLoaded",
    async () => {

        await loadLocation();

        setInterval(
            loadLocation,
            30000
        );

    }
);

// ==========================================
// Load Location
// ==========================================

async function loadLocation() {

    try {

        const response = await fetch(`${API}/api/location`);

        const data = await response.json();
        if (!response.ok || data.success === false) {
            return;
        }
        latitude = data.latitude;
        longitude = data.longitude;

        latitude = data.latitude;
        longitude = data.longitude;

        setValue("latitude", data.latitude);
        setValue("longitude", data.longitude);

        setValue("city", data.city);
        setValue("country", data.country);

        setValue("accuracy", data.accuracy || "GPS");

        setValue(
            "lastUpdate",
            new Date(data.timestamp).toLocaleString()
        );

        loadMap();

    }

    catch (e) {

        console.error(

            "Location Error:",

            e

        );

    }

}

// ==========================================
// Load Google Map
// ==========================================

function loadMap() {

    if (

        latitude == null ||

        longitude == null

    )

        return;

    document.getElementById(

        "map"

    ).src =

        `https://maps.google.com/maps?q=${latitude},${longitude}&z=16&output=embed`;

}

// ==========================================
// Refresh
// ==========================================

async function refreshLocation() {

    await loadLocation();

    alert(

        "Location Updated"

    );

}

// ==========================================
// Navigation
// ==========================================

function navigateLocation() {

    if (

        latitude == null ||

        longitude == null

    )

        return;

    window.open(

        `https://www.google.com/maps/dir/?api=1&destination=${latitude},${longitude}`,

        "_blank"

    );

}

// ==========================================
// Copy Coordinates
// ==========================================

function copyCoordinates() {

    navigator.clipboard.writeText(

        `${latitude}, ${longitude}`

    );

    alert(

        "Coordinates Copied"

    );

}

// ==========================================
// Open Google Maps
// ==========================================

function openGoogleMaps() {

    if (

        latitude == null ||

        longitude == null

    )

        return;

    window.open(

        `https://maps.google.com/?q=${latitude},${longitude}`,

        "_blank"

    );

}

// ==========================================
// Location Status
// ==========================================

function locationAvailable() {

    return (

        latitude !== null &&

        longitude !== null

    );

}

// ==========================================
// Console
// ==========================================

console.log(

    "%c📍 Location Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
// ==========================================
// SecureWatch AI
// dashboard.js
// ==========================================

// ------------------------------------------
// Initialize Dashboard
// ------------------------------------------

async function initializeDashboard() {

    try {

        await Promise.all([

            loadStatus(),

            loadEvidence(),

            loadAnalytics(),

            loadRiskAnalytics(),

            loadTimeline(),

            loadAlerts(),

            checkEmergency()

        ]);

        console.log(

            "✅ Dashboard Ready"

        );

    }

    catch (e) {

        console.error(

            "Dashboard Init Error:",

            e

        );

    }

}

// ------------------------------------------
// Load Device Status
// ------------------------------------------

async function loadStatus() {

    try {

        const data = await getJSON(

            `${API}/device/status`

        );

        // Top Cards

        setValue(

            "deviceStatus",

            data.status

        );

        setValue(

            "city",

            data.city

        );

        setValue(

            "ipAddress",

            data.ip_address

        );

        setValue(

            "lastSeen",

            data.last_seen

        );

        // Device Summary

        setValue(

            "deviceName",

            data.device_name

        );

        setValue(

            "deviceStatus2",

            data.status

        );

        setValue(

            "ipAddress2",

            data.ip_address

        );

        setValue(

            "city2",

            data.city

        );

        setValue(

            "country",

            data.country

        );

        setValue(

            "latitude",

            data.latitude

        );

        setValue(

            "longitude",

            data.longitude

        );

        setValue(

            "lastSeen2",

            data.last_seen

        );

        updateDeviceBadge(

            data.status

        );

    }

    catch (e) {

        console.error(

            "Status Error:",

            e

        );

    }

}

// ------------------------------------------
// Device Badge
// ------------------------------------------

function updateDeviceBadge(status) {

    const badge =

        $("deviceStatus");

    if (!badge)
        return;

    badge.classList.remove(

        "online",

        "offline"

    );

    if (

        status &&

        status.toLowerCase() ===

        "online"

    ) {

        badge.classList.add(

            "online"

        );

    }

    else {

        badge.classList.add(

            "offline"

        );

    }

}

// ------------------------------------------
// Latest Evidence
// ------------------------------------------

async function loadEvidence() {

    try {

        const data = await getJSON(

            `${API}/evidence/latest`

        );

        if (

            $("latestImage")

            &&

            data.photo_path

        ) {

            $("latestImage").src =

                `${API}/image/${data.photo_path}?t=${Date.now()}`;

        }

        setValue(

            "eventId",

            data.event_id

        );

        setValue(

            "photoPath",

            data.photo_path

        );

        setValue(

            "videoPath",

            data.video_path

        );

        setValue(

            "audioPath",

            data.audio_path

        );

    }

    catch (e) {

        console.error(

            "Evidence Error:",

            e

        );

    }

}

// ------------------------------------------
// Refresh Dashboard
// ------------------------------------------

async function refreshDashboard() {

    try {

        await Promise.all([

            loadStatus(),

            loadEvidence(),

            loadAnalytics(),

            loadRiskAnalytics(),

            loadTimeline(),

            loadAlerts(),

            checkEmergency()

        ]);

        notifySuccess(

            "Dashboard",

            "Dashboard refreshed."

        );

    }

    catch (e) {

        console.error(e);

    }

}

// ------------------------------------------
// Auto Refresh Backup
// ------------------------------------------

setInterval(

    loadStatus,

    15000

);

setInterval(

    checkEmergency,

    3000

);

// ------------------------------------------
// Dashboard Startup
// ------------------------------------------

window.addEventListener(

    "focus",

    () => {

        refreshDashboard();

    }

);

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c🛡 Dashboard Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
// ==========================================
// SecureWatch AI
// camera.js
// ==========================================

let liveRunning = false;

// ------------------------------------------
// Start Live Camera
// ------------------------------------------

function startLiveCamera() {

    const image = document.getElementById(
        "liveFeed"
    );

    const placeholder = document.getElementById(
        "cameraPlaceholder"
    );

    const badge = document.getElementById(
        "cameraStatus"
    );

    if (!image) return;

    image.style.display = "block";

    image.src = `${API}/video_feed?${Date.now()}`;

    if (placeholder) {

        placeholder.style.display = "none";

    }

    if (badge) {

        badge.innerHTML = "🟢 LIVE";

        badge.classList.add("online");

    }

    liveRunning = true;

    notifySuccess(

        "Camera",

        "Live camera started."

    );

}

// ------------------------------------------
// Stop Live Camera
// ------------------------------------------

async function stopLiveCamera() {

    try {

        await fetch(

            `${API}/video_stop`,

            {

                method: "POST"

            }

        );

    }

    catch (e) {

        console.error(e);

    }

    const image = document.getElementById(
        "liveFeed"
    );

    const placeholder = document.getElementById(
        "cameraPlaceholder"
    );

    const badge = document.getElementById(
        "cameraStatus"
    );

    if (image) {

        image.src = "";

        image.style.display = "none";

    }

    if (placeholder) {

        placeholder.style.display = "flex";

    }

    if (badge) {

        badge.innerHTML = "⚪ OFFLINE";

        badge.classList.remove("online");

    }

    liveRunning = false;

    notifyInfo(

        "Camera",

        "Live camera stopped."

    );

}

// ------------------------------------------
// Toggle Camera
// ------------------------------------------

function toggleLiveView() {

    if (liveRunning) {

        stopLiveCamera();

    }

    else {

        startLiveCamera();

    }

    updateCameraButtons();

}

// ------------------------------------------
// Update Buttons
// ------------------------------------------

function updateCameraButtons() {

    const buttons = [

        document.getElementById("liveViewBtn"),

        document.getElementById("liveViewBtn2")

    ];

    buttons.forEach(button => {

        if (!button) return;

        if (liveRunning) {

            button.innerHTML = `

                <i class="fa-solid fa-stop"></i>

                Stop Live View

            `;

        }

        else {

            button.innerHTML = `

                <i class="fa-solid fa-video"></i>

                Start Live View

            `;

        }

    });

}

// ------------------------------------------
// Snapshot
// ------------------------------------------

async function captureSnapshot() {

    try {

        const response = await fetch(

            `${API}/remote/capture`,

            {

                method: "POST"

            }

        );

        const data = await response.json();

        notifySuccess(

            "Snapshot",

            data.message

        );
        await loadEvidence();

        await loadTimeline();

        await loadAnalytics();

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Snapshot Failed",

            "Unable to capture image."

        );

    }

}

// ------------------------------------------
// Camera Status
// ------------------------------------------

function updateCameraStatus(running) {

    const badge = document.getElementById(
        "cameraStatus"
    );

    if (!badge) return;

    if (running) {

        badge.innerHTML = "🟢 LIVE";

        badge.classList.add("online");

    }

    else {

        badge.innerHTML = "⚪ OFFLINE";

        badge.classList.remove("online");

    }

}

async function toggleLiveAudio() {

    notifyInfo(

        "Audio",

        "Coming in Integration Phase"

    );

}

// ------------------------------------------
// Auto Stop
// ------------------------------------------

window.addEventListener(

    "beforeunload",

    () => {

        if (liveRunning) {

            stopLiveCamera();

        }

    }

);

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c📹 Camera Module Loaded",

    "color:#4CAF50;font-weight:bold;font-size:14px"

);
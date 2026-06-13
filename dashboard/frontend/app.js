// ==========================================
// SecureWatch AI
// app.js
// ==========================================

window.addEventListener(

    "DOMContentLoaded",

    async () => {

        console.log(

            "🚀 SecureWatch AI Starting..."

        );

        try {

            // -----------------------
            // Initialize Socket
            // -----------------------

            initializeSocket();

            // -----------------------
            // Initialize Dashboard
            // -----------------------

            await initializeDashboard();

            // -----------------------
            // Update Clock
            // -----------------------

            updateClock();

            setInterval(

                updateClock,

                1000

            );

            console.log(

                "✅ SecureWatch Ready"

            );

        }

        catch (e) {

            console.error(

                "Startup Error:",

                e

            );

            notifyError(

                "Startup Failed",

                "Unable to initialize dashboard."

            );

        }

    }

);

// ==========================================
// Live Clock
// ==========================================

function updateClock() {

    const now = new Date();

    const time = document.getElementById(

        "liveTime"

    );

    const date = document.getElementById(

        "liveDate"

    );

    if (time) {

        time.textContent =

            now.toLocaleTimeString([], {

                hour: "2-digit",

                minute: "2-digit",

                second: "2-digit"

            });

    }

    if (date) {

        date.textContent =

            now.toDateString();

    }

}

// ==========================================
// Online / Offline Status
// ==========================================

window.addEventListener(

    "online",

    () => {

        notifySuccess(

            "Internet Connected",

            "Connection restored."

        );

    }

);

window.addEventListener(

    "offline",

    () => {

        notifyWarning(

            "Internet Lost",

            "Working offline."

        );

    }

);

// ==========================================
// Before Closing Browser
// ==========================================

window.addEventListener(

    "beforeunload",

    () => {

        if (

            typeof disconnectSocket ===

            "function"

        ) {

            disconnectSocket();

        }

    }

);

// ==========================================
// Console
// ==========================================

console.log(

    "%c🛡 SecureWatch AI Loaded",

    "color:#00c853;font-size:15px;font-weight:bold"

);
// ==========================================
// SecureWatch AI
// socket.js
// ==========================================

let socket = null;

// ------------------------------------------
// Initialize Socket
// ------------------------------------------

function initializeSocket() {

    if (typeof io === "undefined") {

        console.warn(

            "Socket.IO not loaded."

        );

        return;

    }

    socket = io(API, {

        transports: ["polling"],

        reconnection: true,

        reconnectionAttempts: Infinity,

        reconnectionDelay: 1000,

        timeout: 20000

    });

    registerSocketEvents();

}

// ------------------------------------------
// Register Events
// ------------------------------------------

function registerSocketEvents() {

    // ----------------------------
    // Connected
    // ----------------------------

    socket.on(

        "connect",

        () => {

            console.log(

                "🟢 Connected"

            );

            notifyConnected();

        }

    );

    // ----------------------------
    // Disconnected
    // ----------------------------

    socket.on(

        "disconnect",

        () => {

            console.log(

                "🔴 Disconnected"

            );

            notifyDisconnected();

        }

    );

    // ----------------------------
    // Reconnected
    // ----------------------------

    socket.on(

        "reconnect",

        () => {

            console.log(

                "🟢 Reconnected"

            );

            notifyReconnected();

        }

    );

    // ----------------------------
    // Security Alert
    // ----------------------------

    socket.on(

        "security_alert",

        (data) => {

            showNotification(

                data.title,

                data.message,

                data.level

            );

            loadAlerts();

            loadTimeline();

        }

    );

    // ----------------------------
    // New Evidence
    // ----------------------------

    socket.on(

        "new_evidence",

        () => {

            loadEvidence();

            loadTimeline();

            loadAnalytics();

        }

    );

    // ----------------------------
    // Analytics
    // ----------------------------

    socket.on(

        "analytics_update",

        () => {

            loadAnalytics();

        }

    );

    // ----------------------------
    // Risk
    // ----------------------------

    socket.on(

        "risk_update",

        () => {

            loadRiskAnalytics();

        }

    );

    // ----------------------------
    // Timeline
    // ----------------------------

    socket.on(

        "timeline_update",

        () => {

            loadTimeline();

        }

    );

    // ----------------------------
    // Alerts
    // ----------------------------

    socket.on(

        "alert_update",

        () => {

            loadAlerts();

        }

    );

    // ----------------------------
    // Device Status
    // ----------------------------

    socket.on(

        "device_status",

        () => {

            loadStatus();

        }

    );

    // ----------------------------
    // Emergency
    // ----------------------------

    socket.on(
        "emergency_update",

        async () => {
            await checkEmergency();
            await loadStatus();
        }
    );

    // ----------------------------
    // Camera
    // ----------------------------

    socket.on(

        "camera_status",

        (data) => {

            updateCameraStatus(

                data.running

            );

        }

    );

}

// ------------------------------------------
// Emit Helper
// ------------------------------------------

function emit(event, data = {}) {

    if (!socket)

        return;

    socket.emit(

        event,

        data

    );

}

// ------------------------------------------
// Connected?
// ------------------------------------------

function socketConnected() {

    return socket && socket.connected;

}

// ------------------------------------------
// Disconnect
// ------------------------------------------

function disconnectSocket() {

    if (!socket)

        return;

    socket.disconnect();

}

// ------------------------------------------
// Reconnect
// ------------------------------------------

function reconnectSocket() {

    if (!socket)

        return;

    socket.connect();

}

// ------------------------------------------
// Heartbeat
// ------------------------------------------

setInterval(

    () => {

        if (

            socketConnected()

        ) {

            emit(

                "heartbeat"

            );

        }

    },

    30000

);

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c📡 Socket Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
// ==========================================
// SecureWatch AI
// notification.js
// ==========================================

// ------------------------------------------
// Show Notification
// ------------------------------------------

function showNotification(
    title,
    message,
    level = "info"
) {

    let container = document.getElementById(
        "notificationContainer"
    );

    if (!container) {

        container = document.createElement("div");

        container.id = "notificationContainer";

        container.className = "notification-container";

        document.body.appendChild(container);

    }

    const notification = document.createElement("div");

    notification.className = `notification ${level}`;

    let icon = "ℹ️";

    switch (level) {

        case "success":
            icon = "✅";
            break;

        case "warning":
            icon = "⚠️";
            break;

        case "danger":
        case "error":
            icon = "🚨";
            break;

        default:
            icon = "ℹ️";

    }

    notification.innerHTML = `

        <div class="notification-header">

            <span class="notification-icon">

                ${icon}

            </span>

            <strong>

                ${title}

            </strong>

        </div>

        <div class="notification-body">

            ${message}

        </div>

    `;

    container.appendChild(notification);

    requestAnimationFrame(() => {

        notification.classList.add("show");

    });

    setTimeout(() => {

        notification.classList.remove("show");

        notification.classList.add("hide");

        setTimeout(() => {

            notification.remove();

        }, 300);

    }, 4500);

}

// ------------------------------------------
// Shortcut Methods
// ------------------------------------------

function notifySuccess(title, message) {

    showNotification(
        title,
        message,
        "success"
    );

}

function notifyWarning(title, message) {

    showNotification(
        title,
        message,
        "warning"
    );

}

function notifyError(title, message) {

    showNotification(
        title,
        message,
        "error"
    );

}

function notifyInfo(title, message) {

    showNotification(
        title,
        message,
        "info"
    );

}

// ------------------------------------------
// Loading Notification
// ------------------------------------------

function showLoading(message = "Loading...") {

    showNotification(

        "SecureWatch AI",

        message,

        "info"

    );

}

// ------------------------------------------
// Connection Notifications
// ------------------------------------------

function notifyConnected() {

    notifySuccess(

        "Connected",

        "Live monitoring connected."

    );

}

function notifyDisconnected() {

    notifyWarning(

        "Disconnected",

        "Waiting for SecureWatch server..."

    );

}

function notifyReconnected() {

    notifySuccess(

        "Reconnected",

        "Real-time monitoring restored."

    );

}

// ------------------------------------------
// Emergency Notification
// ------------------------------------------

function notifyEmergency(message) {

    notifyError(

        "Emergency",

        message

    );

}

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c🔔 Notification Module Loaded",

    "color:#00c853;font-weight:bold;font-size:14px"

);
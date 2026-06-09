// Automatically use the same server that served the page
const API = window.location.origin;
// =============================
// SecureWatch Live Socket
// =============================

const socket = io(API);

socket.on("connect", () => {

    console.log(
        "🟢 Connected to SecureWatch Live Server"
    );

});
/**
 * Helper function to create HTML for info rows
 */
const createRow = (label, value) => `
    <div class="info-row">
        <span class="label">${label}</span>
        <span class="value">${value}</span>
    </div>
`;

/**
 * Load Device Status
 */
async function loadStatus() {
    try {
        const response = await fetch(`${API}/device/status`);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        const statusHtml =
            data.status &&
                data.status.toLowerCase() === "online"
                ? `<span class="status-badge">
                        <span class="status-dot"></span>
                        ${data.status}
                   </span>`
                : `<span class="value">${data.status || "Unknown"}</span>`;

        document.getElementById("status").innerHTML = `
            ${createRow("💻 Device Name", data.device_name || "N/A")}
            ${createRow("🟢 Status", statusHtml)}
            ${createRow("🌍 Country", data.country || "N/A")}
            ${createRow("🏙 City", data.city || "N/A")}
            ${createRow("📡 IP Address", data.ip_address || "N/A")}
            ${createRow(
            "📍 Coordinates",
            `${data.latitude || "N/A"}, ${data.longitude || "N/A"}`
        )}
            ${createRow("⏰ Last Seen", data.last_seen || "N/A")}
        `;
    } catch (e) {
        console.error("Status Load Error:", e);

        document.getElementById("status").innerHTML = `
            <div style="padding:15px;color:#ff6b6b;">
                ❌ Unable to connect to device
            </div>
        `;
    }
}

/**
 * Load Latest Evidence
 */
async function loadEvidence() {
    try {
        const response = await fetch(`${API}/evidence/latest`);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        const imageUrl = `${API}/image/${data.photo_path}`;

        document.getElementById("evidence").innerHTML = `
            <img
                src="${imageUrl}"
                class="evidence-image"
                alt="Evidence Image"
            >

            <div class="info-row">
                <span>🆔 Event ID</span>
                <span class="value">
                    ${data.event_id || "N/A"}
                </span>
            </div>

            <div class="info-row">
                <span>📸 Photo</span>
                <span class="value">
                    Available
                </span>
            </div>
        `;
    } catch (e) {
        console.error("Evidence Load Error:", e);

        document.getElementById("evidence").innerHTML = `
            <div style="padding:15px;color:#ff6b6b;">
                ❌ No evidence available
            </div>
        `;
    }
}

async function loadAnalytics() {

    try {

        const response =
            await fetch(
                `${API}/analytics`
            );

        const data =
            await response.json();

        document.getElementById(
            "analytics"
        ).innerHTML = `

            ${createRow(
            "🚨 Total Intrusions",
            data.total_intrusions
        )}

            ${createRow(
            "📸 Photos Captured",
            data.photos
        )}

            ${createRow(
            "🎥 Videos Recorded",
            data.videos
        )}

            ${createRow(
            "🕒 Last Detection",
            data.last_detection
        )}

        `;

    }

    catch (e) {

        console.error(
            "Analytics Error:",
            e
        );

        document.getElementById(
            "analytics"
        ).innerHTML = `

            <div style="
                padding:15px;
                color:#ff6b6b;
            ">
                ❌ Analytics Unavailable
            </div>

        `;
    }
}

/**
 * Remote Capture
 */
async function captureDevice() {
    try {
        const btn = document.querySelector(".capture-btn");

        if (btn) {
            const originalText = btn.innerHTML;
            btn.innerHTML = "⏳ Processing...";

            await fetch(`${API}/remote/capture`, {
                method: "POST"
            });

            await loadEvidence();

            setTimeout(() => {
                btn.innerHTML = originalText;
            }, 1000);
        }

        alert("📸 Capture Triggered");
    } catch (e) {
        console.error("Capture Error:", e);
        alert("❌ Capture Failed");
    }
}

/**
 * Remote Lock
 */
async function lockDevice() {
    try {
        await fetch(`${API}/remote/lock`, {
            method: "POST"
        });

        alert("🔒 Device Locked");
    } catch (e) {
        console.error("Lock Error:", e);
        alert("❌ Lock Failed");
    }
}

/**
 * Remote Alarm
 */
async function alarmDevice() {
    try {
        await fetch(`${API}/remote/alarm`, {
            method: "POST"
        });

        alert("🔊 Alarm Activated");
    } catch (e) {
        console.error("Alarm Error:", e);
        alert("❌ Alarm Failed");
    }
}

async function loadRiskAnalytics() {

    try {

        const response = await fetch(
            `${API}/analytics/risk`
        );

        const data = await response.json();

        document.getElementById(
            "risk-analytics"
        ).innerHTML = `

            <div class="info-row">
                <span>🔴 High Risk Events</span>
                <span class="value">${data.high_risk}</span>
            </div>

            <div class="info-row">
                <span>🟡 Medium Risk Events</span>
                <span class="value">${data.medium_risk}</span>
            </div>

            <div class="info-row">
                <span>🟢 Low Risk Events</span>
                <span class="value">${data.low_risk}</span>
            </div>

            <div class="info-row">
                <span>📈 Average Risk Score</span>
                <span class="value">${data.average_risk}</span>
            </div>

        `;

    } catch (e) {

        console.error(
            "Risk Analytics Error:",
            e
        );

    }
}

async function loadAlerts() {

    try {

        const response =
            await fetch(
                `${API}/dashboard/alerts`
            );

        const alerts =
            await response.json();

        let html = "";

        alerts.forEach(alert => {

            let eventName =
                alert.event_type;

            if (
                eventName ===
                "CAMERA_CAPTURE"
            )
                eventName =
                    "📸 Camera";

            if (
                eventName ===
                "UNKNOWN_FACE"
            )
                eventName =
                    "🚨 Unknown Face";

            if (
                eventName ===
                "FAILED_LOGIN"
            )
                eventName =
                    "🔐 Failed Login";

            let riskLabel =
                "🟢 LOW";

            if (
                alert.risk_score >= 70
            ) {

                riskLabel =
                    "🔴 HIGH";

            } else if (
                alert.risk_score >= 40
            ) {

                riskLabel =
                    "🟡 MEDIUM";
            }

            html += `
                <div class="info-row">

                    <span>
                        ${eventName}
                    </span>

                    <span class="value">
                        ${riskLabel}
                    </span>

                </div>
            `;
        });

        document.getElementById(
            "alerts"
        ).innerHTML = html;

    } catch (e) {

        document.getElementById(
            "alerts"
        ).innerHTML =
            "Unable to load alerts";
    }
}

async function loadTimeline() {

    try {

        const response =
            await fetch(
                `${API}/dashboard/timeline`
            );

        const logs =
            await response.json();

        let html = "";

        logs.forEach(log => {

            let icon = "📄";

            if (log.action.includes("PHOTO"))
                icon = "📸";

            else if (
                log.action.includes("RISK")
            )
                icon = "🎯";

            else if (
                log.action.includes("EMAIL")
            )
                icon = "📧";

            else if (
                log.action.includes("VIDEO")
            )
                icon = "🎥";

            html += `
            <div class="timeline-item">

                <div class="timeline-dot"></div>

                <div class="timeline-content">

                    <div class="timeline-time">

                        ${log.time}

                    </div>

                    <div class="timeline-title">

                        ${icon}
                        ${log.action}

                    </div>

                    <div class="timeline-details">

                        ${log.details}

                    </div>

                </div>

            </div>
            `;
        });

        document.getElementById(
            "timeline"
        ).innerHTML = html;

    }

    catch {

        document.getElementById(
            "timeline"
        ).innerHTML =
            "Unable to load timeline";
    }

}

function showNotification(
    title,
    message,
    level
) {

    const notification =
        document.createElement("div");

    notification.className =
        `live-notification ${level}`;

    notification.innerHTML = `
        <h3>${title}</h3>
        <p>${message}</p>
    `;

    document.body.appendChild(
        notification
    );

    setTimeout(() => {

        notification.classList.add(
            "show"
        );

    }, 100);

    setTimeout(() => {

        notification.classList.remove(
            "show"
        );

        setTimeout(() => {

            notification.remove();

        }, 500);

    }, 5000);

}


// =============================
// LIVE SOCKET EVENTS
// =============================

socket.on(
    "security_alert",
    data => {

        showNotification(
            data.title,
            data.message,
            data.level
        );

        // Refresh dashboard automatically

        loadStatus();

        loadEvidence();

        loadAnalytics();

        loadRiskAnalytics();

        loadAlerts();

        loadTimeline();

    }
);


/**
 * Initial Load
 */
loadStatus();
loadEvidence();
loadAnalytics();
loadRiskAnalytics();
loadAlerts();
loadTimeline();


/**
 * Auto Refresh Every 5 Seconds
 */

setInterval(loadStatus, 5000);

setInterval(loadEvidence, 10000);

setInterval(loadAnalytics, 10000);

setInterval(loadRiskAnalytics, 10000);

setInterval(loadAlerts, 10000);

setInterval(loadTimeline, 5000);
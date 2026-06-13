// ==========================================
// SecureWatch AI
// analytics.js
// ==========================================

// ------------------------------------------
// Load Analytics
// ------------------------------------------

async function loadAnalytics() {

    try {

        const data = await getJSON(
            `${API}/analytics`
        );

        setValue(
            "totalEvents",
            data.total_intrusions ?? 0
        );

        setValue(
            "todayEvents",
            data.photos ?? 0
        );

        setValue(
            "cameraStatusCount",
            1
        );

        if (document.getElementById("lastSeen")) {

            setValue(
                "lastSeen",
                data.last_detection ?? "--"
            );

        }

    }

    catch (e) {

        console.error(
            "Analytics Error:",
            e
        );

    }

}

// ------------------------------------------
// Load Risk Analytics
// ------------------------------------------

async function loadRiskAnalytics() {

    try {

        const data = await getJSON(
            `${API}/analytics/risk`
        );

        setValue(
            "highRisk",
            data.high_risk ?? 0
        );

        const score =
            data.average_risk ?? 0;

        setValue(
            "riskScore",
            `${score}%`
        );

        let level = "LOW";

        if (score >= 70) {

            level = "HIGH";

        }

        else if (score >= 40) {

            level = "MEDIUM";

        }

        setValue(
            "riskLevel",
            level
        );

        setValue(
            "riskLevel2",
            level
        );

    }

    catch (e) {

        console.error(
            "Risk Analytics Error:",
            e
        );

    }

}

// ------------------------------------------
// Load Timeline
// ------------------------------------------

async function loadTimeline() {

    try {

        const logs = await getJSON(
            `${API}/dashboard/timeline`
        );

        const container =

            document.getElementById(
                "timelineContainer"
            );

        if (!container)
            return;

        container.innerHTML = "";

        if (logs.length === 0) {

            container.innerHTML = `

            <div class="empty-state">

                No Timeline Available

            </div>

            `;

            return;

        }

        logs.forEach(log => {

            let icon =

                "📄";

            if (log.action.includes("PHOTO"))

                icon = "📸";

            else if (log.action.includes("VIDEO"))

                icon = "🎥";

            else if (log.action.includes("EMAIL"))

                icon = "📧";

            else if (log.action.includes("LOGIN"))

                icon = "🔐";

            else if (log.action.includes("RISK"))

                icon = "⚠️";

            container.innerHTML += `

            <div class="timeline-item">

                <div class="timeline-icon">

                    ${icon}

                </div>

                <div class="timeline-content">

                    <h4>

                        ${log.action}

                    </h4>

                    <p>

                        ${log.details}

                    </p>

                    <span>

                        ${log.time}

                    </span>

                </div>

            </div>

            `;

        });

    }

    catch (e) {

        console.error(
            "Timeline Error:",
            e
        );

    }

}

// ------------------------------------------
// Load Alerts
// ------------------------------------------

async function loadAlerts() {

    try {

        const alerts = await getJSON(
            `${API}/dashboard/alerts`
        );

        const container =

            document.getElementById(
                "alertsContainer"
            );

        if (!container)
            return;

        container.innerHTML = "";

        if (alerts.length === 0) {

            container.innerHTML = `

            <div class="empty-state">

                <i class="fa-solid fa-circle-check"></i>

                <p>

                    No Active Alerts

                </p>

            </div>

            `;

            return;

        }

        alerts.forEach(alert => {

            let level = "success";

            let icon = "🟢";

            let risk = "LOW";

            if (alert.risk_score >= 70) {

                level = "danger";

                icon = "🔴";

                risk = "HIGH";

            }

            else if (alert.risk_score >= 40) {

                level = "warning";

                icon = "🟡";

                risk = "MEDIUM";

            }

            container.innerHTML += `

            <div class="alert-item ${level}">

                <div class="alert-title">

                    ${icon}
                    ${alert.event_type.replaceAll("_", " ")}

                </div>

                <div class="alert-message">

                    Risk Score :
                    ${alert.risk_score}

                </div>

                <div class="alert-time">

                    ${risk}

                </div>

            </div>

            `;

        });

    }

    catch (e) {

        console.error(
            "Alert Error:",
            e
        );

    }

}

// ------------------------------------------
// Refresh Analytics
// ------------------------------------------

async function refreshAnalytics() {

    await Promise.all([

        loadAnalytics(),

        loadRiskAnalytics(),

        loadTimeline(),

        loadAlerts()

    ]);

}

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c📊 Analytics Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
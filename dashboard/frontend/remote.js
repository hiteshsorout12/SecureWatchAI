// ==========================================
// SecureWatch AI
// remote.js
// ==========================================

// ------------------------------------------
// Panic Mode
// ------------------------------------------

async function panicMode() {

    const ok = confirm(

        `🚨 PANIC MODE

This will immediately:

• 📸 Capture Evidence
• 🔊 Trigger Alarm
• 🔒 Lock Laptop
• 🚨 Activate Emergency

Continue?`

    );

    if (!ok)
        return;

    try {

        notifyWarning(

            "Panic Mode",

            "Executing emergency actions..."

        );

        const data = await postJSON(

            `${API}/remote/panic`

        );

        notifySuccess(

            "Emergency Activated",

            data.message

        );
        await loadEvidence();

        await loadTimeline();

        await loadAnalytics();

        refreshDashboard();

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Panic Failed",

            "Unable to activate panic mode."

        );

    }

}

// ------------------------------------------
// Remote Capture
// ------------------------------------------

async function remoteCapture() {

    try {

        const data = await postJSON(

            `${API}/remote/capture`

        );

        notifySuccess(

            "Capture Started",

            data.message

        );

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Capture Failed",

            "Unable to capture image."

        );

    }

}

// ------------------------------------------
// Trigger Alarm
// ------------------------------------------

async function triggerAlarm() {

    try {

        const data = await postJSON(

            `${API}/remote/alarm`

        );

        notifyWarning(

            "Alarm Activated",

            data.message

        );
        await refreshDashboard();

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Alarm Failed",

            "Unable to trigger alarm."

        );

    }

}

// ------------------------------------------
// Lock Laptop
// ------------------------------------------

async function lockDevice() {

    if (

        !confirm(

            "Lock the protected laptop?"

        )

    ) {

        return;

    }

    try {

        const data = await postJSON(

            `${API}/remote/lock`

        );

        notifySuccess(

            "Laptop Locked",

            data.message

        );
        await refreshDashboard();

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Lock Failed",

            "Unable to lock laptop."

        );

    }

}

// ------------------------------------------
// Start Emergency
// ------------------------------------------

async function startEmergency() {

    try {

        await postJSON(

            `${API}/emergency/start`

        );

        notifyWarning(

            "Emergency Mode",

            "Emergency mode activated."

        );

        checkEmergency();

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Emergency Failed",

            "Unable to start emergency."

        );

    }

}

// ------------------------------------------
// End Emergency
// ------------------------------------------

async function endEmergency() {

    try {

        const data = await postJSON(

            `${API}/emergency/end`

        );

        if (data.success) {

            notifySuccess(

                "Emergency Ended",

                "Monitoring resumed."

            );

            checkEmergency();

        }

    }

    catch (e) {

        console.error(e);

        notifyError(

            "Emergency Error",

            "Unable to stop emergency."

        );

    }

}

// ------------------------------------------
// Toggle Emergency
// ------------------------------------------

function toggleEmergency() {

    const button =

        $("emergencyBtn");

    if (!button)
        return;

    if (

        button.dataset.mode === "end"

    ) {

        endEmergency();

    }

    else {

        startEmergency();

    }

}

// ------------------------------------------
// Emergency Status
// ------------------------------------------

async function checkEmergency() {

    try {

        const data = await getJSON(

            `${API}/emergency/status`

        );

        const button =

            $("emergencyBtn");

        const badge =

            $("emergencyBadge");

        const status =

            $("securityStatus");

        if (!button)
            return;

        if (data.active) {

            button.dataset.mode = "end";

            button.classList.remove(

                "success-btn"

            );

            button.classList.add(

                "danger-btn"

            );

            button.innerHTML =

                "🛑 End Emergency";

            if (status)

                status.innerHTML =

                    "<span class='danger'>🔴 Emergency Active</span>";

            if (badge) {

                badge.style.display =

                    "flex";

                badge.innerHTML =

                    "🚨 ACTIVE";

            }

        }

        else {

            button.dataset.mode =

                "start";

            button.classList.remove(

                "danger-btn"

            );

            button.classList.add(

                "success-btn"

            );

            button.innerHTML =

                "🚨 Start Emergency";

            if (status)

                status.innerHTML =

                    "<span class='success'>🟢 Monitoring</span>";

            if (badge)

                badge.style.display =

                    "none";

        }

    }

    catch (e) {

        console.error(

            "Emergency Status Error:",

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

            "Dashboard refreshed successfully."

        );

    }

    catch (e) {

        console.error(e);

    }

}

// ------------------------------------------
// Console
// ------------------------------------------

console.log(

    "%c🎮 Remote Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
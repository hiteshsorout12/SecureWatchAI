// ==========================================
// SecureWatch AI
// settings.js
// ==========================================



// ==========================================
// Startup
// ==========================================

window.addEventListener(
    "DOMContentLoaded",
    () => {
        loadSettings();
    }
);

// ==========================================
// Load Settings
// ==========================================

async function loadSettings() {

    try {

        const response = await fetch(`${API}/api/settings`)

        const data = await response.json();

        document.getElementById(

            "startup"

        ).checked = data.startup;

        document.getElementById(

            "notification"

        ).checked = data.notifications;

        document.getElementById(

            "email"

        ).checked = data.email_alerts;

        document.getElementById(

            "sound"

        ).checked = data.alarm_sound;

    }

    catch (e) {

        console.error(

            "Settings Error:",

            e

        );

    }

}

// ==========================================
// Save Settings
// ==========================================

async function saveSettings() {

    const settings = {

        startup:

            document.getElementById(

                "startup"

            ).checked,

        notifications:

            document.getElementById(

                "notification"

            ).checked,

        email_alerts:

            document.getElementById(

                "email"

            ).checked,

        alarm_sound:

            document.getElementById(

                "sound"

            ).checked

    };

    try {

        const response = await fetch(

            `${API}/settings`,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(

                    settings

                )

            }

        );

        const data = await response.json();

        alert(

            data.message

        );

    }

    catch (e) {

        console.error(e);

        alert(

            "Unable to save settings."

        );

    }

}

// ==========================================
// Register Owner
// ==========================================

async function trainOwner() {

    if (

        !confirm(

            "Capture owner's face?"

        )

    )

        return;

    try {

        const response =

            await fetch(

                `${API}/owner/register`,

                {

                    method: "POST"

                }

            );

        const data =

            await response.json();

        alert(

            data.message

        );

    }

    catch (e) {

        console.error(e);

    }

}

// ==========================================
// Change Email
// ==========================================

async function changeEmail() {

    const email =

        prompt(

            "Enter New Email"

        );

    if (!email)

        return;

    try {

        const response =

            await fetch(

                `${API}/settings/email`,

                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify({

                        email

                    })

                }

            );

        const data =

            await response.json();

        alert(

            data.message

        );

    }

    catch (e) {

        console.error(e);

    }

}

// ==========================================
// Clear Evidence
// ==========================================

async function clearEvidence() {

    if (

        !confirm(

            "Delete ALL evidence?"

        )

    )

        return;

    try {

        const response =

            await fetch(

                `${API}/evidence/clear`,

                {

                    method: "DELETE"

                }

            );

        const data =

            await response.json();

        alert(

            data.message

        );

    }

    catch (e) {

        console.error(e);

    }

}

// ==========================================
// Reset Settings
// ==========================================

async function resetSettings() {

    if (

        !confirm(

            "Reset all settings?"

        )

    )

        return;

    try {

        const response =

            await fetch(

                `${API}/settings/reset`,

                {

                    method: "POST"

                }

            );

        const data =

            await response.json();

        alert(

            data.message

        );

        loadSettings();

    }

    catch (e) {

        console.error(e);

    }

}

// ==========================================
// Console
// ==========================================

console.log(

    "%c⚙ Settings Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);
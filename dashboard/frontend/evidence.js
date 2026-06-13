// ==========================================
// SecureWatch AI
// evidence.js
// ==========================================

const API = window.location.origin;

let evidence = [];

// ==========================================
// Startup
// ==========================================

window.onload = async () => {

    await loadEvidence();

};

// ==========================================
// Load Evidence
// ==========================================

async function loadEvidence() {

    try {

        const response = await fetch(

            `${API}/evidence/all`

        );

        evidence = await response.json();

        renderEvidence();

    }

    catch (e) {

        console.error(e);

    }

}

// ==========================================
// Render
// ==========================================

function renderEvidence() {

    const container =

        document.getElementById(

            "eventContainer"

        );

    container.innerHTML = "";

    if (

        evidence.length === 0

    ) {

        container.innerHTML = `

        <div class="empty">

            <i class="fa-solid fa-folder-open"></i>

            <h2>

                No Evidence Found

            </h2>

        </div>

        `;

        return;

    }

    evidence.reverse().forEach(

        event => {

            container.innerHTML += `

<div class="event-card">

<div class="event-header">

<div>

<h2>

🚨 Intrusion Event

</h2>

<p>

${event.event_id}

</p>

</div>

<div class="risk">

HIGH

</div>

</div>

<div class="event-image">

<img

src="${API}/image/${event.photo_path}"

loading="lazy"

onclick="openImage('${API}/image/${event.photo_path}')"

>

</div>

<div class="event-info">

<div>

<strong>

Photo

</strong>

<p>

${getFile(event.photo_path)}

</p>

</div>

<div>

<strong>

Video

</strong>

<p>

${getFile(event.video_path)}

</p>

</div>

<div>

<strong>

Audio

</strong>

<p>

${getFile(event.audio_path)}

</p>

</div>

</div>

<div class="event-buttons">

<button

onclick="playVideo('${event.video_path}')">

🎥 Video

</button>

<button

onclick="playAudio('${event.audio_path}')">

🎤 Audio

</button>

<button

onclick="viewMetadata('${event.event_id}')">

📄 Metadata

</button>

<button

onclick="downloadEvent('${event.event_id}')">

⬇ Download

</button>

<button

class="danger"

onclick="deleteEvent('${event.event_id}')">

🗑 Delete

</button>

</div>

</div>

`;

        }

    );

}

// ==========================================
// File Name
// ==========================================

function getFile(path) {

    if (!path)

        return "--";

    return path.split("/").pop();

}

// ==========================================
// Image
// ==========================================

function openImage(src) {

    window.open(

        src,

        "_blank"

    );

}

// ==========================================
// Video
// ==========================================

function playVideo(path) {

    if (

        !path ||

        path === "PROCESSING"

    ) {

        alert(

            "Video still processing."

        );

        return;

    }

    window.open(

        `${API}/video/${path}`,

        "_blank"

    );

}

// ==========================================
// Audio
// ==========================================

function playAudio(path) {

    if (!path) {

        alert(

            "No audio available."

        );

        return;

    }

    window.open(

        `${API}/audio/${path}`,

        "_blank"

    );

}

// ==========================================
// Metadata
// ==========================================

async function viewMetadata(id) {

    const response = await fetch(

        `${API}/event/${id}`

    );

    const data = await response.json();

    alert(

        `Event ID : ${data.event_id}
        Type : ${data.event_type}

        Risk : ${data.risk_level}

        Score : ${data.risk_score}`

    );

}

// ==========================================
// Download
// ==========================================

function downloadEvent(id) {

    window.location =

        `${API}/evidence/download/${id}`;

}

// ==========================================
// Delete
// ==========================================

async function deleteEvent(id) {

    if (

        !confirm(

            "Delete this event?"

        )

    )

        return;

    try {

        const response = await fetch(

            `${API}/evidence/delete/${id}`,

            {

                method: "DELETE"

            }

        );

        const data =

            await response.json();

        alert(

            data.message

        );

        loadEvidence();

    }

    catch (e) {

        console.error(e);

    }

}

console.log(

    "📂 Evidence Module Loaded"

);
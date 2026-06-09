// Automatically use current server IP/domain
const API = window.location.origin;

let evidenceData = [];

window.onload = async function () {
    await loadEvidence();
};


// Active Tab Highlight

function setActiveTab(tabId) {
    document
        .querySelectorAll(".tab-btn")
        .forEach(btn =>
            btn.classList.remove("active")
        );

    const btn = document.getElementById(tabId);

    if (btn) {
        btn.classList.add("active");
    }
}


// Load Evidence

async function loadEvidence() {

    try {

        const response =
            await fetch(
                `${API}/evidence/all`
            );

        if (!response.ok) {
            throw new Error(
                `HTTP Error ${response.status}`
            );
        }

        evidenceData =
            await response.json();

        console.log(
            "Evidence Loaded:",
            evidenceData
        );

        showPhotos();
        setActiveTab("photosBtn");
    }

    catch (error) {

        console.error(
            "Evidence Load Error:",
            error
        );

        document.getElementById(
            "gallery"
        ).innerHTML = `

        <h2
            style="
            text-align:center;
            color:white;
            ">

            ❌ Failed To Load Evidence

        </h2>

        `;
    }
}


// PHOTO TAB

function showPhotos() {

    setActiveTab(
        "photosBtn"
    );

    const gallery =
        document.getElementById(
            "gallery"
        );

    gallery.innerHTML = "";

    const photos =
        evidenceData.filter(
            item =>
                item.photo_path
        );

    if (
        photos.length === 0
    ) {

        gallery.innerHTML = `

        <h2
            style="
            text-align:center;
            color:white;
            ">

            📷 No Photos Found

        </h2>

        `;

        return;
    }

    photos.forEach(
        evidence => {

            const imageUrl =
                `${API}/image/${evidence.photo_path}?t=${Date.now()}`;

            gallery.innerHTML += `

            <div
                class="gallery-card">

                <img

                    src="${imageUrl}"

                    class="gallery-image"

                    loading="lazy"

                    style="
                        opacity:0;
                        transition:0.4s;
                    "

                    onload="
                        this.style.opacity='1'
                    "

                    onclick="
                    openModal('${imageUrl}')
                    "

                    onerror="
                    this.parentElement.style.display='none'
                    "

                >

            </div>

            `;
        }
    );
}


// VIDEO TAB

function showVideos() {

    setActiveTab(
        "videosBtn"
    );

    const gallery =
        document.getElementById(
            "gallery"
        );

    gallery.innerHTML = "";

    const videos =
        evidenceData.filter(
            item =>
                item.video_path
        );

    if (
        videos.length === 0
    ) {

        gallery.innerHTML = `

        <h2
            style="
            text-align:center;
            color:white;
            ">

            🎥 No Videos Found

        </h2>

        `;

        return;
    }

    videos.forEach(
        evidence => {

            gallery.innerHTML += `

            <div
                class="gallery-card">

                <video
                    controls
                    class="gallery-image"
                    style="
                    width:100%;
                    border-radius:12px;
                    ">

                    <source
                        src="${API}/video/${evidence.video_path}?t=${Date.now()}"
                        type="video/mp4">

                </video>

                <div
                    style="
                    padding:10px;
                    color:white;
                    ">

                    Event:
                    ${evidence.event_id || "N/A"}

                </div>

            </div>

            `;
        }
    );
}


// AUDIO TAB

function showAudio() {

    setActiveTab(
        "audioBtn"
    );

    const gallery =
        document.getElementById(
            "gallery"
        );

    gallery.innerHTML = `

    <div
        style="
        width:100%;
        text-align:center;
        padding:80px;
        color:white;
        ">

        <h2>
            🎤 Audio Gallery
        </h2>

        <p>
            Coming Soon
        </p>

    </div>

    `;
}


// OPEN IMAGE

function openModal(
    imageUrl
) {

    document.getElementById(
        "imageModal"
    ).style.display =
        "block";

    document.getElementById(
        "modalImage"
    ).src =
        imageUrl;
}


// CLOSE IMAGE

function closeModal() {

    document.getElementById(
        "imageModal"
    ).style.display =
        "none";
}


// ESC KEY CLOSE

document.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Escape"
        ) {

            closeModal();
        }
    }
);
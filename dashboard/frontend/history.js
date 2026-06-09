async function loadHistory() {

    try {

        const response = await fetch("/evidence/all");

        const data = await response.json();

        const container =
            document.getElementById(
                "history-container"
            );

        const totalEvents =
            document.getElementById(
                "total-events"
            );

        totalEvents.textContent =
            data.length;

        container.innerHTML = "";

        if (data.length === 0) {

            container.innerHTML = `
                <p>No intrusion events found.</p>
            `;

            return;
        }

        data.reverse().forEach(event => {

            const card =
                document.createElement("div");

            card.className =
                "history-card";

            card.innerHTML = `

                <div class="event-header">
                    Event ID:
                    ${event.event_id}
                </div>

                ${event.photo_path
                    ?
                    `
                    <img
                        src="/${event.photo_path}"
                        class="history-image"
                    >
                    `
                    :
                    ""
                }

                ${event.video_path
                    ?
                    `
                    <video
                        controls
                        class="history-video"
                    >
                        <source
                            src="/${event.video_path}"
                            type="video/mp4"
                        >
                    </video>
                    `
                    :
                    ""
                }
            `;

            container.appendChild(
                card
            );

        });

    }

    catch (error) {

        console.error(error);

        document.getElementById(
            "history-container"
        ).innerHTML = `
            <p>
                Failed to load events.
            </p>
        `;
    }
}

loadHistory();
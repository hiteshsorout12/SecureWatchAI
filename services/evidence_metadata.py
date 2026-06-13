import json
from pathlib import Path
from datetime import datetime


def save_metadata(

    folder,

    risk,

    owner,

    event_type,

    photo,

    video,

    audio=""

):

    metadata = {

        "created_at": datetime.now().isoformat(),

        "event_type": event_type,

        "owner_detected": owner,

        "risk_score": risk["risk_score"],

        "risk_level": risk["risk_level"],

        "photo": Path(photo).name,

        "video": Path(video).name,

        "audio": Path(audio).name if audio else ""

    }

    with open(

        Path(folder) / "metadata.json",

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            metadata,

            file,

            indent=4

        )

    print("📄 Metadata Saved")
from pathlib import Path
from datetime import datetime


def create_evidence_folder():

    event_id = "EVT_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    folder = Path("evidence/events") / event_id

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    return {
        "event_id": event_id,
        "folder": folder
    }
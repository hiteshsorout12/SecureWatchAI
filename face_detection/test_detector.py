from pathlib import Path
from face_detection.detector import detect_faces

photos = list(Path("evidence/photos").glob("*.jpg"))

latest_photo = max(
    photos,
    key=lambda p: p.stat().st_mtime
)

print("Latest Photo:", latest_photo)

count = detect_faces(str(latest_photo))

print("Faces Found:", count)
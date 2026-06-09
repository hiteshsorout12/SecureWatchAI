from services.evidence_service import create_evidence

print("Evidence Test Started")

create_evidence(
    event_id="TEST_EVENT_001",
    photo_path="E:/Evidence/Photos/photo1.jpg",
    video_path="E:/Evidence/Videos/video1.mp4",
    audio_path="E:/Evidence/Audio/audio1.wav"
)

print("Evidence Test Completed")
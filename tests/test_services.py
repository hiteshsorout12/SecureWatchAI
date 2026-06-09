from services.user_service import create_user
from services.event_service import create_event

print("Test Started")

create_user(
    "Hitesh",
    "hiteshsorout12@gmail.com",
    "OWNER"
)

create_event(
    "WAKE_EVENT",
    10,
    "ACTIVE"
)

print("Test Finished")
from services.alert_service import create_alert

print("Alert Test Started")

create_alert(
    event_id="TEST_EVENT_001",
    channel="EMAIL"
)

print("Alert Test Completed")
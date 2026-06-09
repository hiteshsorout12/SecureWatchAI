from services.audit_service import create_audit_log

print("Audit Test Started")

create_audit_log(
    action="PHOTO_CAPTURED",
    module="CAMERA",
    details="Intruder image captured",
    status="SUCCESS"
)

print("Audit Test Completed")
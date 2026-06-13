from remote.capture_action import remote_capture
from remote.alarm_action import remote_alarm
from remote.lock_action import remote_lock


def remote_panic():

    print("=" * 60)
    print("🚨 PANIC MODE ACTIVATED")
    print("=" * 60)

    try:

        print("📸 Capturing Evidence...")
        remote_capture()

        print("🔊 Starting Alarm...")
        remote_alarm()

        print("🔒 Locking Device...")
        remote_lock()

        print("✅ Panic Mode Completed")

        return {
            "status": "success",
            "message": "Panic Mode Activated"
        }

    except Exception as e:

        print(
            "❌ Panic Mode Error:",
            e
        )

        return {
            "status": "error",
            "message": str(e)
        }
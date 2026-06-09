from datetime import datetime
import time
import threading
import win32evtlog

from remote.capture_action import (
    remote_capture
)

SERVER = "localhost"
LOG_TYPE = "Security"

last_detected = None
last_login_time = None

print("✅ Successful Login Detector Started")

# Ignore all old login events at startup
initialized = False


def run_capture():

    try:

        print(
            "📸 Verifying Logged In User..."
        )

        time.sleep(5)

        remote_capture()

        print(
            "✅ Verification Complete"
        )

    except Exception as e:

        print(
            "❌ Verification Error:",
            e
        )


while True:

    try:

        hand = win32evtlog.OpenEventLog(
            SERVER,
            LOG_TYPE
        )

        flags = (
            win32evtlog.EVENTLOG_BACKWARDS_READ
            |
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
        )

        events = win32evtlog.ReadEventLog(
            hand,
            flags,
            0
        )

        if not events:

            time.sleep(3)
            continue

        found_new_event = False

        for event in events:

            event_id = (
                event.EventID & 0xFFFF
            )

            if event_id != 4801:
                continue

            current_time = str(
                event.TimeGenerated
            )

            # First run:
            # remember latest login and ignore it

            if not initialized:

                last_detected = current_time
                initialized = True

                print(
                    "Detector Initialized"
                )

                break

            if current_time == last_detected:
                continue

            event_time = datetime.now()

            # 30 second cooldown

            if (
                last_login_time is not None
                and
                (
                    event_time -
                    last_login_time
                ).total_seconds() < 30
            ):
                continue

            last_login_time = event_time

            last_detected = current_time

            print(
                "\n✅ SUCCESSFUL LOGIN DETECTED"
            )

            print(
                f"⏰ Time: {current_time}"
            )

            threading.Thread(
                target=run_capture,
                daemon=True
            ).start()

            print(
                "--------------------------------"
            )

            found_new_event = True

            break

        if not found_new_event:

            print(
                "Monitoring Successful Logins..."
            )

    except Exception as e:

        print(
            "Detector Error:",
            e
        )

    time.sleep(3)
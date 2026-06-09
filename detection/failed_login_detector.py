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
last_intrusion_time = None

print("🚀 Failed Login Detector Started")


def run_capture():

    try:

        print(
            "📸 Starting Capture..."
        )

        remote_capture()

        print(
            "✅ Capture Finished"
        )

    except Exception as e:

        print(
            "❌ Capture Error:",
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

        found_new_event = False

        for event in events:

            event_id = (
                event.EventID & 0xFFFF
            )

            if event_id != 4625:
                continue

            current_time = str(
                event.TimeGenerated
            )

            if current_time == last_detected:
                continue

            last_detected = current_time

            event_time = datetime.now()

            # Ignore repeated failed logins
            if (
                last_intrusion_time is not None
                and
                (
                    event_time -
                    last_intrusion_time
                ).total_seconds() < 30
            ):
                continue

            last_intrusion_time = event_time

            print(
                "\n🚨 FAILED LOGIN DETECTED"
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
                "Monitoring..."
            )

    except Exception as e:

        print(
            "Detector Error:",
            e
        )

    time.sleep(3)
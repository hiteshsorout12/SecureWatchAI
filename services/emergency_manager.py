from services.security_session_service import (
    get_active_session
)


class EmergencyManager:

    def start(self):

        print("🚨 Emergency Mode Started")

    def stop(self):

        print("🛑 Emergency Mode Stopped")

    def is_active(self):

        session = get_active_session()

        if session is None:
            return False

        return session.active


emergency_manager = EmergencyManager()
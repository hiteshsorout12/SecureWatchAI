from datetime import datetime

from sqlalchemy import desc

from database.connection import SessionLocal

from models.security_session import SecuritySession


# ---------------------------------
# Start Session
# ---------------------------------

def start_session(
    session_type="NORMAL",
    risk_score=0,
    status="NORMAL"
):

    db = SessionLocal()

    try:

        # Close previous active session
        db.query(SecuritySession).filter(
            SecuritySession.active == True
        ).update(
            {
                "active": False,
                "ended_at": datetime.utcnow()
            }
        )

        session = SecuritySession(

            session_type=session_type,

            active=True,

            status=status,

            risk_score=risk_score,

            camera_on=True,

            microphone_on=True,

            live_stream_on=False,

            owner_connected=False

        )

        db.add(session)

        db.commit()

        db.refresh(session)

        return session

    finally:

        db.close()


# ---------------------------------
# End Session
# ---------------------------------

def end_session():

    db = SessionLocal()

    try:

        session = (
            db.query(SecuritySession)
            .filter(SecuritySession.active == True)
            .first()
        )

        if session is None:

            return False

        session.active = False
        session.camera_on = False
        session.microphone_on = False
        session.live_stream_on = False
        session.owner_connected = False
        session.ended_at = datetime.utcnow()

        db.commit()

        return True

    finally:

        db.close()


# ---------------------------------
# Get Active Session
# ---------------------------------

def get_active_session():

    db = SessionLocal()

    try:

        return db.query(SecuritySession).filter(
            SecuritySession.active == True
        ).first()

    finally:

        db.close()


# ---------------------------------
# Update Camera
# ---------------------------------

def update_camera(status: bool):

    db = SessionLocal()

    try:

        session = (
            db.query(SecuritySession)
            .filter(SecuritySession.active == True)
            .first()
        )

        if session:

            session.camera_on = status

            db.commit()

    finally:

        db.close()


# ---------------------------------
# Update Microphone
# ---------------------------------

def update_microphone(status: bool):

    db = SessionLocal()

    try:

        session = (
            db.query(SecuritySession)
            .filter(SecuritySession.active == True)
            .first()
        )

        if session:

            session.microphone_on = status

            db.commit()

    finally:
        db.close()


# ---------------------------------
# Update Live Stream
# ---------------------------------

def update_live_stream(status: bool):

    db = SessionLocal()

    try:

        session = (
            db.query(SecuritySession)
            .filter(SecuritySession.active == True)
            .first()
        )

        if session:

            session.live_stream_on = status

            db.commit()

    finally:

        db.close()
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.audit_log import AuditLog

Session = sessionmaker(bind=engine)


def create_audit_log(
        action,
        module,
        details,
        status):

    session = Session()

    log = AuditLog(
        action=action,
        module=module,
        details=details,
        status=status
    )

    session.add(log)
    session.commit()

    print("Audit Log Created")

    session.close()
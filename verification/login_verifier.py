from verification.owner_verifier import verify_owner
from verification.retry_capture import capture_with_retry
from verification.verification_result import VerificationResult


def verify_login():

    print(
        "🔍 Starting Login Verification..."
    )

    photo_path = capture_with_retry()

    if photo_path is None:

        print(
            "❌ Unable to Capture Face"
        )

        return VerificationResult(
            status="NO_FACE",
            confidence=0,
            photo=None
        )

    result = verify_owner(
        photo_path
    )

    return result
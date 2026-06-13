from face_recognition_module.recognizer import (
    recognize_face
)

from verification.verification_result import (
    VerificationResult
)


def verify_owner(photo_path):

    try:

        is_owner = recognize_face(
            photo_path
        )

        if is_owner:

            print(
                "✅ OWNER VERIFIED"
            )

            return VerificationResult(

                status="OWNER",

                confidence=100,

                photo=photo_path,

                risk="LOW",

                message="Owner Verified"

            )

        print(
            "🚨 UNKNOWN PERSON"
        )

        return VerificationResult(

            status="UNKNOWN",

            confidence=0,

            photo=photo_path,

            risk="HIGH",

            message="Unknown Person"

        )

    except Exception as e:

        print(
            "Verification Error:",
            e
        )

        return VerificationResult(

            status="ERROR",

            confidence=0,

            photo=None,

            risk="HIGH",

            message=str(e)

        )
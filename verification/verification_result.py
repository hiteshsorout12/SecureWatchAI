class VerificationResult:

    def __init__(

        self,

        status,

        confidence,

        photo,

        risk="LOW",

        message=""

    ):

        self.status = status

        self.confidence = confidence

        self.photo = photo

        self.risk = risk

        self.message = message

    def to_dict(self):

        return {

            "status": self.status,

            "confidence": self.confidence,

            "photo": self.photo,

            "risk": self.risk,

            "message": self.message

        }

    def __str__(self):

        return (

            f"VerificationResult("

            f"status={self.status}, "

            f"confidence={self.confidence}, "

            f"risk={self.risk})"

        )
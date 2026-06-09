import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from services.risk_engine import calculate_risk

result = calculate_risk()

print(result)
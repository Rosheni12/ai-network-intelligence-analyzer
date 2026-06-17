from dashboard.core.schema import REQUIRED_KEYS

def validate_summary(summary: dict) -> dict:
    """
    Ensures summary always has required keys.
    Prevents KeyErrors everywhere.
    """

    safe_summary = REQUIRED_KEYS.copy()

    for key, default_value in REQUIRED_KEYS.items():
        if key in summary and summary[key] is not None:
            safe_summary[key] = summary[key]

    return safe_summary
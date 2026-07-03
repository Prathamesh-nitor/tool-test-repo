import re
def filter_pii(data: dict) -> dict:
    # Simple PII filter for demonstration
    filtered = {}
    for k, v in data.items():
        if isinstance(v, str) and re.match(r"[^@]+@[^@]+\.[^@]+", v):
            filtered[k] = "[FILTERED_EMAIL]"
        else:
            filtered[k] = v
    return filtered
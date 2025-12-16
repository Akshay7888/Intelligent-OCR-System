import re

def extract_entities(text):
    entities = {}

    patterns = {
        "INVOICE_NO": r"Invoice\s*No[:\s]*([A-Z0-9\-]+)",
        "DATE": r"Date\s*[:\s]*([0-9]{1,2}[\/\-][0-9]{1,2}[\/\-][0-9]{2,4})",
        "TOTAL_AMOUNT": r"Total\s*[:\s]*₹?\s*([0-9,.]+)",
        "GSTIN": r"GSTIN[:\s]*([0-9A-Z]{15})",
        "EMAIL": r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
        "PHONE": r"(\+91[-\s]?[6-9][0-9]{9})"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            entities[key] = match.group(1)

    return entities

import re
 
ENTITY_PATTERNS = {
 
    "SPEED":
        r"\b\d+(?:\.\d+)?\s*(?:km\s*/\s*h|km/h|kmh|mph)\b",
 
    "DISTANCE":
        r"\b\d+(?:\.\d+)?\s*(?:m|meter|meters|metre|metres)\b|\b\d+(?:\.\d+)?\s*km\b(?!/h)",
 
    "TIME":
        r"\b\d+(?:\.\d+)?\s*(?:s|sec|secs|second|seconds|min|mins|minute|minutes|hour|hours)\b",
 
    "LEVEL":
        r"\bLevel\s*[123]\b",
 
    "MODE":
        r"\b(?:FS|OS|SR|SH|LS|PT|SB|TR)\b",
 
    "RBC":
        r"\bRBC\b",
 
    "BALISE":
        r"\bbalise(?:\s+group)?\b",
 
    "MOVEMENT_AUTHORITY":
        r"\bMovement Authority\b|\bMA\b",
 
    "GRADIENT":
        r"\bgradient\s*[-+]?\d+(?:\.\d+)?\b|\b\d+(?:\.\d+)?\s*‰\b",
 
    "PERCENTAGE":
        r"\b\d+(?:\.\d+)?\s*%\b"
}
 
 
def normalize_entity(entity_name, value):
    """
    Normalize entity values to ensure consistency.
    """
 
    value = value.strip()
 
    value = re.sub(
        r"\s+",
        " ",
        value
    )
 
    if entity_name == "RBC":
        return "RBC"
 
    elif entity_name == "MOVEMENT_AUTHORITY":
 
        if value.upper() == "MA":
            return "MA"
 
        return "Movement Authority"
 
    elif entity_name == "LEVEL":
 
        match = re.search(
            r"(\d+)",
            value
        )
 
        if match:
            return f"Level {match.group(1)}"
 
        return value
 
    elif entity_name == "BALISE":
 
        value = value.lower()
 
        if value == "balise groups":
            return "balise group"
 
        return value
 
    elif entity_name == "MODE":
 
        return value.upper()
 
    return value
 
 
def extract_entities(text):
 
    if not text:
        return {}
 
    text = str(text)
 
    entities = {}
 
    for entity_name, pattern in ENTITY_PATTERNS.items():
 
        matches = re.finditer(
            pattern,
            text,
            flags=re.IGNORECASE
        )
 
        values = []
 
        for match in matches:
 
            value = match.group(0)
 
            value = normalize_entity(
                entity_name,
                value
            )
 
            values.append(value)
 
        # Remove duplicates while preserving order
        values = list(
            dict.fromkeys(values)
        )
 
        if values:
            entities[entity_name] = values
 
    return entities
 
 
if __name__ == "__main__":
 
    samples = [
 
        "The train shall stop within 800 m at 160 km/h.",
 
        "The RBC shall transmit a Movement Authority after 30 seconds.",
 
        "Level 2 shall be entered after Start of Mission.",
 
        "The balise group shall contain linking information.",
 
        "The train shall enter FS mode after receiving MA from the RBC.",
 
        "The braking distance shall be 1200 m with gradient 12.",
 
        "The train shall run at 90% braking performance."
    ]
 
    print("\n" + "=" * 60)
    print("RAILWAY NER TEST")
    print("=" * 60)
 
    for sample in samples:
 
        print("\nRequirement:")
        print(sample)
 
        print("\nEntities:")
        print(extract_entities(sample))
 
        print("-" * 60)
 
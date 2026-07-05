import re
 
ENTITY_PATTERNS = {
 
    "SPEED":
        r"\b\d+(?:\.\d+)?\s*(?:km/h|kmh|mph)\b",
 
    "DISTANCE":
        r"\b\d+(?:\.\d+)?\s*m\b|\b\d+(?:\.\d+)?\s*km\b(?!/h)",
 
    "TIME":
        r"\b\d+(?:\.\d+)?\s*(?:s|sec|seconds|min|minutes|hour|hours)\b",
 
    "LEVEL":
        r"\bLevel\s*[123]\b",
 
    "MODE":
        r"\b(FS|OS|SR|SH|LS|PT|SB|TR)\b",
 
    "RBC":
        r"\bRBC\b",
 
    "BALISE":
        r"\bbalise(?:\s+group)?\b",
 
    "MOVEMENT_AUTHORITY":
        r"\bMovement Authority\b|\bMA\b"
}
 
 
def extract_entities(text):
 
    entities = {}
 
    for entity_name, pattern in ENTITY_PATTERNS.items():
 
        matches = re.finditer(
            pattern,
            text,
            flags=re.IGNORECASE
        )
 
        values = [
            match.group(0)
            for match in matches
        ]
 
        if values:
            entities[entity_name] = values
 
    return entities
 
 
if __name__ == "__main__":
 
    samples = [
 
        "The train shall stop within 800 m at 160 km/h.",
 
        "The RBC shall transmit a Movement Authority after 30 seconds.",
 
        "Level 2 shall be entered after Start of Mission.",
 
        "The balise group shall contain linking information.",
 
        "The train shall enter FS mode after receiving MA from the RBC."
    ]
 
    for sample in samples:
 
        print("\nRequirement:")
        print(sample)
 
        print("Entities:")
        print(extract_entities(sample))
 
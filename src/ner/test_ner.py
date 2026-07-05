from railway_ner import extract_entities
 
samples = [
 
    "The train shall stop within 800 m at 160 km/h.",
 
    "The RBC shall transmit a Movement Authority after 30 seconds.",
 
    "Level 2 shall be entered after Start of Mission.",
 
    "The balise group shall contain linking information.",
 
    "The train shall enter FS mode after receiving MA from the RBC."
]
 
for text in samples:
 
    print("\n" + "=" * 60)
 
    print("Requirement:")
    print(text)
 
    print("\nEntities:")
 
    entities = extract_entities(text)
 
    for entity_type, values in entities.items():
 
        print(f"{entity_type}: {values}")
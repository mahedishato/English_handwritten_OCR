import spacy
from spacy.training import Example

# Load the English language model with NER capabilities
nlp = spacy.load("en_core_web_sm")


# Sample text for NER
text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. It is headquartered in Cupertino, California."

# Process the text
doc = nlp(text)

# Extract named entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the named entities
for entity in entities:
    print(entity)
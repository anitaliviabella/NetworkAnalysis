import pandas as pd
import json

# Given JSON data
json_data = '''
{
    "Hamlet": {
        "son_of": "Ghost",
        "nephew_of": "King Claudius",
        "friend_of": "Horatio",
        "love_interest_of": "Ophelia"
    },
    "King Claudius": {
        "brother_of": "Ghost",
        "uncle_of": "Hamlet",
        "husband_of": "Gertrude"
    },
    "Queen Gertrude": {
        "mother_of": "Hamlet",
        "wife_of": "King Claudius"
    },
    "Polonius": {
        "father_of": [
            "Laertes",
            "Ophelia"
        ]
    },
    "Laertes": {
        "brother_of": "Ophelia"
    },
    "Ophelia": {
        "sister_of": "Laertes",
        "fiancee_of": "Hamlet"
    },
    "Horatio": {
        "friend_of": "Hamlet"
    },
    "Rosencrantz": {
        "companion_of": "Guildenstern"
    },
    "Guildenstern": {
        "companion_of": "Rosencrantz"
    },
    "Reynalds": {
        "servant_of": "Polonius"
    },
    "Captain": {
        "messenger_of": "Fortinbras"
    }
}
'''

# Load JSON data
data = json.loads(json_data)

# Initialize lists to store data
characters = []
relationships = []
with_of_values = []

# Extract data from JSON
for character, relationships_dict in data.items():
    for relationship, with_of_value in relationships_dict.items():
        characters.append(character)
        relationships.append(relationship.replace("_", " ").title())  # Convert snake_case to title case
        with_of_values.append(with_of_value)

# Create DataFrame
df = pd.DataFrame({
    "Character": characters,
    "Type of Relationship": relationships,
    "With/Of": with_of_values
})

# Save DataFrame to CSV
df.to_csv("relationships/relationships.csv", index=False)

# Display the DataFrame
print(df)

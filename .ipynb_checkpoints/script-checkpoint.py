import pandas as pd
import networkx as nx
from itertools import combinations 
from matplotlib import pyplot
import matplotlib.pyplot as plt
import csv

#-----------------------------All characters ---------------------------------
#list of the characters 
characters_list = ['Hamlet', 'King Claudius', 'Queen Gertrude', 'Horatio', 'Polonius', 'Laertes', 'Ophelia', 'Bernardo', 'Francisco', 'Marcellus', 'Ghost', 'King Fortinbras', 'Voltimand', 'Lords', 'Attendants', 'Rosencrantz', 'Guildenstern', 'Ambassadors from Norway', 'Players', 'First Player', 'Reynaldo', 'Lucianus', 'Player King', 'Player Queen', 'Prince Fortinbras', 'Captain', 'Gentlemen', 'Servant', 'First Sailor', 'First Clown', 'Second Clown', 'Priest', 'First Ambassador', 'Osric', 'A Lord', 'Cornelius', 'Messenger', 'Fortinbras']

# Dizionario
genere_dict = {
    'Hamlet': 'Male',
    'King Claudius': 'Male',
    'Queen Gertrude' : 'Female',
    'Horatio': 'Male',
    'Polonius': 'Male',
    'Laertes': 'Male',
    'Ophelia': 'Female',
    'Bernardo': 'Male',
    'Francisco': 'Male',
    'Marcellus': 'Male',
    'Ghost': 'Male',
    'King Fortinbras': 'Male',
    'Voltimand': 'Male',
    'Lords': 'Male',
    'Attendants': 'Male',
    'Rosencrantz': 'Male',
    'Guildenstern': 'Male',
    'Ambassadors from Norway': 'Male',
    'Players': 'Male',
    'First Player': 'Male',
    'Reynaldo': 'Male',
    'Lucianus': 'Male',
    'Player King': 'Male',
    'Player Queen': 'Male', 
    'Prince Fortinbras': 'Male', 
    'Captain': 'Male', 
    'Gentlemen': 'Male',
    'Servant': 'Male',
    'First Sailor': 'Male',
    'First Clown': 'Male',
    'Second Clown': 'Male', 
    'Priest': 'Male',
    'First Ambassador': 'Male',
    'Osric': 'Male',
    'A Lord': 'Male',
    'Cornelius': 'Male',
    'Messenger': 'Male',
    'Fortinbras': 'Male',

}

# Creazione del DataFrame
attributes_df = pd.DataFrame(list(genere_dict.items()), columns=['Character', 'Gender'])

# Aggiunta delle colonne vuote 'role' e 'place'
attributes_df = attributes_df.assign(Role='', Place='')

# Salvataggio in un file CSV
attributes_df.to_csv('attributes/attributes.csv', index=False)



#--------------------------Couples of co-apperences---------------------------------
def process_scene_csv(file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Extract the 'Character' column
    characters = df['Character'].tolist()

    # Generate all possible combinations of characters (couples)
    character_combinations = list(combinations(characters, 2))

    return character_combinations

# Function to count occurrences of character pairs across all scenes
def count_character_pairs(scene_files):
    # Dictionary to store counts of character pairs
    character_counts = {}

    # Process each scene file
    for file_path in scene_files:
        scene_pairs = process_scene_csv(file_path)

        # Update counts based on character pairs in the current scene
        for pair in scene_pairs:
            # Sort the pair to handle cases where the order of characters doesn't matter
            sorted_pair = tuple(sorted(pair))
            
            # Update or initialize the count for the character pair
            character_counts[sorted_pair] = character_counts.get(sorted_pair, 0) + 1

    return character_counts

# Example usage:
scene_files = ['co/scene_1.csv', 'co/scene_2.csv', 'co/scene_3.csv', 'co/scene_4.csv', 'co/scene_5.csv', 'co/act2_scene_1.csv', 'co/act_2_scene_2.csv', 'co/act3_scene_1.csv', 'co/act3_scene_2.csv', 'co/act3_scene_3.csv', 'co/act3_scene_4.csv', 'co/act4_scene1.csv', 'co/act4_scene2.csv', 'co/act4_scene3.csv', 'co/act4_scene4.csv', 'co/act4_scene5.csv', 'co/act4_scene6.csv', 'co/act4_scene7.csv','co/act5_scene1.csv', 'co/act5_scene2.csv'] # Add your actual file paths here
result = count_character_pairs(scene_files)

# Print the results
#for pair, count in result.items():
    #print(f"Character Pair: {pair}, Count: {count}")

# Convert the result dictionary to a DataFrame for easier handling
result_df = pd.DataFrame(list(result.items()), columns=['Character Pair', 'Count'])
# Save the result to a CSV file
result_df.to_csv('co/character_pairs_counts.csv', index=False)

#-------------------------------TEST--------------------------------------
# Print the graph edges with weights
#for edge in G.edges(data=True):
    #print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]['weight']}")

    
#------------------------------INTERACTIONS--------------------------------- 

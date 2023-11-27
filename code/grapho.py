import pandas as pd
import networkx as nx
from itertools import combinations 
from matplotlib import pyplot
import matplotlib.pyplot as plt

#-----------------------------All characters ---------------------------------

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
attributes_df.to_csv('attributes.csv', index=False)



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
scene_files = ['all/scene_1.csv', 'all/scene_2.csv', 'all/scene_3.csv', 'all/scene_4.csv', 'all/scene_5.csv', 'all/act2_scene_1.csv', 'all/act_2_scene_2.csv', 'all/act3_scene_1.csv', 'all/act3_scene_2.csv', 'all/act3_scene_3.csv', 'all/act3_scene_4.csv', 'all/act4_scene1.csv', 'all/act4_scene2.csv', 'all/act4_scene3.csv', 'all/act4_scene4.csv', 'all/act4_scene5.csv', 'all/act4_scene6.csv', 'all/act4_scene7.csv','all/act5_scene1.csv', 'all/act5_scene2.csv'] # Add your actual file paths here
result = count_character_pairs(scene_files)

# Print the results
for pair, count in result.items():
    print(f"Character Pair: {pair}, Count: {count}")

# Convert the result dictionary to a DataFrame for easier handling
result_df = pd.DataFrame(list(result.items()), columns=['Character Pair', 'Count'])
# Save the result to a CSV file
result_df.to_csv('character_pairs_counts.csv', index=False)


#---------------------Create a Graph------------------------------------

import pandas as pd
import networkx as nx
from itertools import combinations 

# ... (your previous code)

# Load the character pairs and their counts from the CSV file
result_df = pd.read_csv('character_pairs_counts.csv')

# Create a directed graph
G = nx.DiGraph()

# Add nodes with gender information
for character, gender in genere_dict.items():
    G.add_node(character, gender=gender)

# Add edges with weights based on co-appearances
for _, row in result_df.iterrows():
    character_pair = eval(row['Character Pair'])  # Convert string representation to tuple
    weight = row['Count']
    G.add_edge(character_pair[0], character_pair[1], weight=weight)

# Print the graph edges with weights
for edge in G.edges(data=True):
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]['weight']}")




#-------------INTERACTIONS---------------
import pandas as pd
import networkx as nx
from itertools import combinations 

# Load the character pairs and their counts from the CSV file
result_df = pd.read_csv('character_pairs_counts.csv')

# Load the matrix of interactions from your CSV file (replace 'interaction_matrix.csv' with your actual file path)
interaction_matrix = pd.read_csv('interactions.csv', index_col=0)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with gender information
for character, gender in genere_dict.items():
    G.add_node(character, gender=gender)

# Add edges with weights based on co-appearances
for _, row in result_df.iterrows():
    character_pair = eval(row['Character Pair'])  # Convert string representation to tuple
    weight = row['Count']
    G.add_edge(character_pair[0], character_pair[1], weight=weight)

# Add edges based on interactions with weights from the interaction matrix
for (char1, char2), interaction_count in interaction_matrix.stack().items():
    if interaction_count != 0:
        G.add_edge(char1, char2, interaction_weight=interaction_count)

# Print the graph edges with weights
for edge in G.edges(data=True):
    co_appearance_weight = edge[2].get('weight', 0)
    interaction_weight = edge[2].get('interaction_weight', 0)
    print(f"Edge: {edge[0]} - {edge[1]}, Co-appearance Weight: {co_appearance_weight}, Interaction Weight: {interaction_weight}")


nodes_to_remove = ['Voltemand', 'Ambassadors from Norway', 'Players (Actors)', 'Queen Margaret', 'Gentleman', 'Lord', 'K', 'u', 'g', 's', 'i', 'd', 'The Servant', 'n', 'Laertes Hamlet', 'a', 'l', 'Guildenster', 'C', ' ']

# Remove nodes from the graph
G.remove_nodes_from(nodes_to_remove)
# Save the updated graph to a file




import pandas as pd

import pandas as pd

# Create an empty dataframe with characters as columns and index
characters = ['Hamlet', 'King Hamlet', 'Queen Gertrude', 'King Claudius', 'Ophelia', 'Horatio', 'Polonius', 'Laertes']
relationships_df = pd.DataFrame(0, index=characters, columns=characters)

# Update the dataframe based on relationships
relationships_df.loc['Hamlet', 'King Hamlet'] += 1  # type: fatherhood
relationships_df.loc['Hamlet', 'Queen Gertrude'] += 1  # type: motherhood
relationships_df.loc['Hamlet', 'King Claudius'] += 1  # type: unclehood
relationships_df.loc['Hamlet', 'Ophelia'] += 1  # type: relationship
relationships_df.loc['King Claudius', 'Queen Gertrude'] += 1  # type: marriage
relationships_df.loc['King Claudius', 'King Hamlet'] += 1  # type: brotherhood
relationships_df.loc['Polonius', 'Laertes'] += 1  # son
relationships_df.loc['Polonius', 'Ophelia'] += 1  # daughter
relationships_df.loc['Laertes', 'Ophelia'] += 1  # brotherhood
relationships_df.loc['Queen Gertrude', 'King Hamlet'] += 1  # ex husband
relationships_df.loc['Hamlet', 'Horatio'] += 1  # friendship

# Save the dataframe to a CSV file in the 'all' directory
relationships_df.to_csv('relationships_matrix.csv')

print("Relationships matrix has been saved to 'relationships_matrix.csv'")

for character1 in relationships_df.index:
    for character2 in relationships_df.columns:
        if relationships_df.loc[character1, character2] == 1:
            G.add_edge(character1, character2)


nx.write_gexf(G, 'final_graph.gexf')

# ... (your previous code)

# Draw the graph
pos = nx.spring_layout(G)

# Extract edge types for coloring
edge_types = nx.get_edge_attributes(G, 'type')

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)

# Draw edges with different colors based on their type
for edge, color in edge_types.items():
    nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=color, width=2, alpha=0.7)

# Draw labels
nx.draw_networkx_labels(G, pos)

# Add a legend
legend_labels = {'Co-appearance': 'red', 'Interaction': 'green', 'Relationship': 'blue'}
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for label, color in legend_labels.items()]
plt.legend(handles=legend_handles, title='Edge Types', loc='upper left')

# Display the plot
plt.show()

# Load the character pairs and their counts from the CSV file
result_df = pd.read_csv('character_pairs_counts.csv')

# Load the matrix of interactions from your CSV file (replace 'interaction_matrix.csv' with your actual file path)
interaction_matrix = pd.read_csv('interactions.csv', index_col=0)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with gender information
for character, gender in genere_dict.items():
    G.add_node(character, gender=gender)

# Add edges with weights based on co-appearances
for _, row in result_df.iterrows():
    character_pair = eval(row['Character Pair'])  # Convert string representation to tuple
    weight = row['Count']
    G.add_edge(character_pair[0], character_pair[1], weight=weight)

# Add edges based on interactions with weights from the interaction matrix
for (char1, char2), interaction_count in interaction_matrix.stack().items():
    if interaction_count != 0:
        G.add_edge(char1, char2, interaction_weight=interaction_count)

# Print the graph edges with weights
#for edge in G.edges(data=True):
    #co_appearance_weight = edge[2].get('weight', 0)
    #interaction_weight = edge[2].get('interaction_weight', 0)
    #print(f"Edge: {edge[0]} - {edge[1]}, Co-appearance Weight: {co_appearance_weight}, Interaction Weight: {interaction_weight}")


nodes_to_remove = ['Voltemand', 'Ambassadors from Norway', 'Players (Actors)', 'Queen Margaret', 'Gentleman', 'Lord', 'K', 'u', 'g', 's', 'i', 'd', 'The Servant', 'n', 'Laertes Hamlet', 'a', 'l', 'Guildenster', 'C', ' ']

# Remove nodes from the graph
G.remove_nodes_from(nodes_to_remove)
# Save the updated graph to a file


# Create an empty dataframe with characters as columns and index
characters = ['Hamlet', 'Ghost', 'Queen Gertrude', 'King Claudius', 'Ophelia', 'Horatio', 'Polonius', 'Laertes']
relationships_df = pd.DataFrame(0, index=characters, columns=characters)

# Update the dataframe based on relationships
relationships_df.loc['Hamlet', 'Ghost'] += 1  # type: fatherhood
relationships_df.loc['Hamlet', 'Queen Gertrude'] += 1  # type: motherhood
relationships_df.loc['Hamlet', 'King Claudius'] += 1  # type: unclehood
relationships_df.loc['Hamlet', 'Ophelia'] += 1  # type: relationship
relationships_df.loc['King Claudius', 'Queen Gertrude'] += 1  # type: marriage
relationships_df.loc['King Claudius', 'Ghost'] += 1  # type: brotherhood
relationships_df.loc['Polonius', 'Laertes'] += 1  # son
relationships_df.loc['Polonius', 'Ophelia'] += 1  # daughter
relationships_df.loc['Laertes', 'Ophelia'] += 1  # brotherhood
relationships_df.loc['Queen Gertrude', 'Ghost'] += 1  # ex husband
relationships_df.loc['Hamlet', 'Horatio'] += 1  # friendship

# Save the dataframe to a CSV file in the 'all' directory
relationships_df.to_csv('relationships_matrix.csv')

#print("Relationships matrix has been saved to 'relationships_matrix.csv'")

for character1 in relationships_df.index:
    for character2 in relationships_df.columns:
        if relationships_df.loc[character1, character2] == 1:
            G.add_edge(character1, character2)

# Save the updated graph to a GEXF file
nx.write_gexf(G, 'final_graph.gexf')

# Print node data to see attribute names
#for node, data in G.nodes(data=True):
   # print(f"Node: {node}, Data: {data}")

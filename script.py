#---------------------Create a Graph------------------------------------
import pandas as pd
import networkx as nx
import json
# Load the character pairs and their counts from the CSV file
result_df = pd.read_csv('co/character_pairs_counts.csv')


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
# Create a directed graph
G = nx.DiGraph()

# Add nodes with gender information
for character, gender in genere_dict.items():
    G.add_node(character, gender=gender)


#----------CO-APPEARENCE
# Add edges with weights based on co-appearances
for _, row in result_df.iterrows():
    character_pair = eval(row['Character Pair'])  # Convert string representation to tuple
    weight = row['Count']
    G.add_edge(character_pair[0], character_pair[1], weight=weight)

#---------INTERACTIONS-------
# Load the interactions data from the CSV file
interactions_df = pd.read_csv('interactions/interactions.csv')

# Add edges with weights based on interactions
for _, row in interactions_df.iterrows():
    character1 = row['Character1']
    character2 = row['Character2']
    weight = row['Number of Interactions']
    
    # Check if the nodes exist in the graph
    if G.has_node(character1) and G.has_node(character2):
        G.add_edge(character1, character2, weight=int(weight))


#------RELATIONSHIPS-----------
# Load relationships from JSON file
# Load the relationships data from the CSV file
relationships_df = pd.read_csv('relationships/relationships.csv')

# Add edges with labels based on relationships
for _, row in relationships_df.iterrows():
    character1 = row['Character']
    relationship_type = row['Type of Relationship']
    with_of = row['With/Of']

    # Check if the nodes exist in the graph
    if G.has_node(character1) and G.has_node(with_of):
        # Add edge with label
        G.add_edge(character1, with_of, relationship=relationship_type)


# Now you have a graph (G) with edges representing co-appearances, interactions, and relationships.
import matplotlib.pyplot as plt

# Set node positions for better visualization
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, font_size=8, node_size=2000, node_color='skyblue', arrowsize=10)

# Add labels for relationships
edge_labels = nx.get_edge_attributes(G, 'relationship')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)

# Check if 'weight' attribute exists for each edge
if all('weight' in G[u][v] for u, v in G.edges()):
    # Extract edge weights for drawing
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]

    # Draw edges with weights
    edge_collection = nx.draw_networkx_edges(G, pos, edge_color=edge_weights, edge_cmap=plt.cm.Blues, width=2)

    # Add colorbar for edge weights
    colorbar = plt.colorbar(edge_collection)
    colorbar.set_label('Co-Appearance Weight')

# Show the plot
plt.show()

# Specify the path where you want to save the Gephi file
gephi_file_path = 'graph/draft.gephi'

# Write the graph to a Gephi file
nx.write_gexf(G, gephi_file_path)

print(f"The graph has been exported to: {gephi_file_path}")


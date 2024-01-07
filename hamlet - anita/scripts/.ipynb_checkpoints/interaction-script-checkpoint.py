import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import pickle

# List of nodes
characters_list = [
    'Hamlet', 'King Claudius', 'Queen Gertrude', 'Horatio', 'Polonius', 'Laertes', 'Ophelia',
    'Bernardo', 'Francisco', 'Marcellus', 'Ghost', 'King Fortinbras', 'Voltimand', 'Lords',
    'Attendants', 'Rosencrantz', 'Guildenstern', 'Ambassadors from Norway', 'Players',
    'First Player', 'Reynaldo', 'Lucianus', 'Player King', 'Player Queen', 'Captain',
    'Gentlemen', 'Servant', 'First Sailor', 'First Clown', 'Second Clown', 'Priest',
    'First Ambassador', 'Osric', 'A Lord', 'Cornelius', 'Messenger', 'Fortinbras',
    'Ladies', 'Sailors'
]



# Load attributes from CSV
attributes_df = pd.read_csv('attributes/attributes.csv')  # Replace 'your_attributes_file.csv' with your actual CSV file path

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(characters_list, selfloop=True)

# Add attributes to nodes
for node in characters_list:
    if node in attributes_df['Character'].values:
        attributes = attributes_df[attributes_df['Character'] == node]
        gender = attributes['Gender'].values[0]
        role = attributes['Role'].values[0]
        G.nodes[node]['Gender'] = gender
        G.nodes[node]['Role'] = role

#---------INTERACTIONS-------
interactions_df = pd.read_csv("interactions/interactions.csv")
for index, row in interactions_df.iterrows():
    character1 = row['Character1']
    character2 = row['Character2']
    weight = row['Number of Interactions']

    if G.has_edge(character1, character2):
        # Edge already exists, update the weight
        G[character1][character2]['weight'] += weight
    else:
        # Edge doesn't exist, add it with the weight
        G.add_edge(character1, character2, weight=weight)

gephi_file_path = 'graphs/interaction-graph.gexf'
nx.write_gexf(G, gephi_file_path)

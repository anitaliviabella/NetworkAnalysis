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


#CO-OCCURRENCES EDGES
#----------CO-APPEARENCE
# Add edges with weights based on co-appearances
result_df = pd.read_csv('co/character_pairs_counts.csv')
for _, row in result_df.iterrows():
    character_pair = eval(row['Character Pair'])  # Convert string representation to tuple
    weight = row['Count']
    G.add_edge(character_pair[0], character_pair[1], weight=weight)

    
# Specify the path where you want to save the Gephi file
gephi_file_path = 'graphs/co-graph.gexf'

# Write the graph to a Gephi file
nx.write_gexf(G, gephi_file_path)



#-----------------------------------
#----------VISUALIZATION------------


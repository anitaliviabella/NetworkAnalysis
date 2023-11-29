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

gephi_file_path = 'graphs/relationships-graph.gexf'
nx.write_gexf(G, gephi_file_path)

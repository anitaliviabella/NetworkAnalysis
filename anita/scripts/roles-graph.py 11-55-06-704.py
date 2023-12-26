import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

# List of tuples representing interactions
role_dict = {
'Hamlet': 'Protagonist',
'King Claudius': 'Antagonist', 
'Queen Gertrude': 'Contagonist',
'Horatio': 'Confidant', 
'Polonius': 'Confidant',
'Laertes': 'Foil', 
'Ophelia': 'Love Intrest', 
'Bernardo': 'Supporting Character', 
'Francisco': 'Supporting Character', 
'Marcellus': 'Supporting Character', 
'Ghost': 'Guide',
'King Fortinbras': 'Background Character', 
'Voltimand': 'Supporting Character',
'Lords': 'Secondary Character',
'Attendants': 'Secondary Character',
'Rosencrantz': 'Henchmen', 
'Guildenstern': 'Henchmen',
'Ambassadors from Norway': 'Secondary Character',
'Players': 'Supporting Character',
'First Player': 'Supporting Character',
'Reynaldo': 'Supporing Character',
'Lucianus': 'Supporting Character',
'Player King': 'Secondary Charachter',
'Player Queen': 'Secondary Character',
'Captain': 'Secondary Character',
'Gentlemen': 'Background Character',
'Servant': 'Secondary Character',
'First Sailor': 'Secondary Character',
'First Clown': 'Secondary Character',
'Second Clown': 'Secondary Character',
'Priest': 'Secondary Character',
'First Ambassador': 'Secondary Character',
'Osric': 'Supporting Character', 
'A Lord': 'Secondary Character',
'Cornelius': 'Supporting Character',
'Messenger': 'Secondary Character',
'Fortinbras' : 'Deuntagonist',
'Ladies': 'Background Character',
'Sailors': 'Background Character',
}




interactions = [
    ("Bernardo", "Francisco", 1),
    ("Bernardo", "Ghost", 1),
    ("Francisco", "Ghost", 1),
    ("Horatio", "Marcellus", 1),
    ("Horatio", "Hamlet", 3),
    ("King Claudius", "Queen Gertrude", 6),
    ("King Claudius", "Laertes", 5),
    ("Hamlet", "Queen Gertrude", 3),
    ("King Claudius", "Hamlet", 4),
    ("Hamlet", "Ghost", 2),
    ("Laertes", "Ophelia", 1),
    ("Polonius", "Ophelia", 2),
    ("Polonius", "Laertes", 1),
    ("Polonius", "Reynaldo", 1),
    ("Rosencrantz", "Guildenstern", 5),
    ("Hamlet", "Players", 3),
    ("King Claudius", "Ambassadors from Norway", 1),
    ("Polonius", "King Claudius", 3),
    ("Hamlet", "Ophelia", 3),
    ("Hamlet", "Polonius", 3),
    ("Hamlet", "Hamlet", 6),
    ("Hamlet", "First Player", 1),
    ("Hamlet", "Rosencrantz", 4),
    ("Hamlet", "Guildenstern", 4),
    ("King Claudius", "King Claudius", 3),
    ("Polonius", "Queen Gertrude", 1),
    ("King Claudius", "Rosencrantz", 1),
    ("King Claudius", "Guildenstern", 1),
    ("The Servant", "Horatio", 1),
    ("First Sailor", "Horatio", 1),
    ("Messenger", "King Claudius", 1),
    ("Queen Gertrude", "Laertes", 1),
    ("Clowns", "Clowns", 1),
    ("Hamlet", "Clowns", 1),
    ("Laertes", "Hamlet", 2),
    ("Hamlet", "Osric", 1),
    ("Hamlet", "Fortinbras", 1)
]

# Create a DataFrame
df = pd.DataFrame(interactions, columns=["Character1", "Character2", "Number of Interactions"])

# Map character names to roles using the role_dict
df["Role1"] = df["Character1"].map(role_dict)
df["Role2"] = df["Character2"].map(role_dict)

# Create a role interaction matrix
interaction_matrix = pd.pivot_table(df, values="Number of Interactions", index="Role1", columns="Role2", aggfunc=np.sum, fill_value=0)



# Create a graph from the interaction matrix
G = nx.from_pandas_adjacency(interaction_matrix, create_using=nx.Graph())
# Visualize the graph
pos = nx.spring_layout(G)  # You can change the layout if needed
nx.draw(G, pos, with_labels=True, font_size=8, node_size=500, node_color="skyblue", font_color="black", font_weight="bold", edge_color="gray", linewidths=0.5)
gephi_file_path = 'graphs/roles-graph.gexf'
nx.write_gexf(G, gephi_file_path)
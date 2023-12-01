import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "role analysis/roles_interactions.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path, index_col=0)

# Create a directed graph
G = nx.DiGraph()

# Add nodes
roles = df.index.tolist()
G.add_nodes_from(roles)

# Add edges with weights
for role1, role2 in zip(df.index, df.columns):
    weight = df.loc[role1, role2]
    if weight > 0:
        G.add_edge(role1, role2, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', arrowsize=20)

# Draw edge labels
edge_labels = {(role1, role2): df.loc[role1, role2] for role1, role2 in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()

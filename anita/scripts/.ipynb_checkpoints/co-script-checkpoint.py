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
# Visualization using Matplotlib
pos = nx.spring_layout(G)  # You can choose a different layout if needed
nx.draw(G, pos, with_labels=True, font_size=8, node_size=300, node_color='skyblue', font_color='black', font_weight='bold')
plt.title('Co-occurrence Network Visualization (Matplotlib)')
plt.show()

# Visualization using Plotly
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        )
    )
)

node_adjacencies = []
node_text = []
for adjacencies, node_text_iter in zip(G.adjacency(), G.nodes()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                showlegend=False,
                hovermode='closest',
                margin=dict(b=0,l=0,r=0,t=0),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.update_layout(title_text='Co-occurrence Network Visualization (Plotly)', showlegend=False)
fig.show()
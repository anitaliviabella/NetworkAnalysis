import networkx as nx
import matplotlib.pyplot as plt
from macbeth import param  # Assuming param is defined in macbeth.py

# Create a directed graph
G = nx.Graph()

class SceneCharacterCooccurrences:
    def __init__(self, gender_mapping, all_characters):
        self.cooccurrences = {}
        self.gender_mapping = gender_mapping
        self.all_characters = all_characters

    def add_cooccurrence(self, character1, character2):
        gender1 = self.gender_mapping.get(character1, 'Unknown')
        gender2 = self.gender_mapping.get(character2, 'Unknown')

        pair = tuple(sorted([character1, character2]))
        self.cooccurrences[pair] = self.cooccurrences.get(pair, 0) + 1
        G.add_nodes_from(pair, gender=gender1)  # Add 'gender' attribute to nodes
        G.add_nodes_from(pair, gender=gender2)

        if G.has_edge(*pair):
            G[character1][character2]['weight'] += 1
        else:
            G.add_edge(*pair, weight=1)

    def add_all_nodes(self):
        # Add all nodes to the graph, even those without occurrences
        for character in self.all_characters:
            G.add_node(character, gender=self.gender_mapping.get(character, 'Unknown'))

# Example usage
gender_mapping = dict(zip(param['Character'], param['Gender']))
all_characters = param['Character']

all_scenes_cooccurrences = SceneCharacterCooccurrences(gender_mapping, all_characters)

# Adding co-occurrences based on the provided information
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Donalbain", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Lady Macbeth")
# Adding co-occurrences from the latest scene
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Duncan")
# Adding co-occurrences from Act II, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Fleance")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Fleance")

# Adding co-occurrences from Act II, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")

# Adding co-occurrences from Act II, Scene 3
all_scenes_cooccurrences.add_cooccurrence("Porter", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Porter", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Porter", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
# Adding co-occurrences from Act II, Scene 4
all_scenes_cooccurrences.add_cooccurrence("Ross", "Old man")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Old man", "Macduff")
# Adding co-occurrences from Act III, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Ross")

# Adding co-occurrences from Act III, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First murderer")
all_scenes_cooccurrences.add_cooccurrence("First murderer", "Second murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second murderer")
# Adding co-occurrences from Act III, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")
# Adding co-occurrences from Act III, Scene 3
all_scenes_cooccurrences.add_cooccurrence("First murderer", "Third murderer")
all_scenes_cooccurrences.add_cooccurrence("First murderer", "Second murderer")
all_scenes_cooccurrences.add_cooccurrence("Third murderer", "Second murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "First murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Second murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Third murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Fleance")
# Adding co-occurrences from Act III, Scene 4
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ghost of Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "First murderer")
# Adding co-occurrences from Act III, Scene 5
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Third Witch", "Hecate")
# Adding co-occurrences from Act III, Scene 6
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Fleance")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Old Siward")
# Adding co-occurrences from Act IV, Scene 1
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Third Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
# Adding co-occurrences from Act IV, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "Son")
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "First murderer")
all_scenes_cooccurrences.add_cooccurrence("Son", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Son", "First murderer")
all_scenes_cooccurrences.add_cooccurrence("Ross", "First murderer")
# Adding co-occurrences from Act V, Scene 3
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Doctor")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macduff")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Doctor")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Lady Macduff")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Son")
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "Son")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "GentleWoman")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("GentleWoman", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("GentleWoman", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Caithness")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Old Siward")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Old Siward")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Old Siward")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Old Siward")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macduff")
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Doctor')
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Seyton', 'Macbeth')
# Act V, Scene 4
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Old Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Young Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Menteith')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Old Siward')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Angus', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Angus', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Lennox', 'Ross')

# Act V, Scene 5
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Seyton', 'Macbeth')
# Act V, Scene 6
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Old Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Macduff')

# Act V, Scene 7
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Young Siward')
all_scenes_cooccurrences.add_cooccurrence('Young Siward', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Macduff', 'Macbeth')
# Act V, Scene 8
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Old Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Old Siward', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')


# Add all nodes to the graph
all_scenes_cooccurrences.add_all_nodes()

# Export the graph to Gephi
nx.write_gexf(G, 'occurrences.gexf')

centrality_measures = {
    'degree_centrality': nx.degree_centrality(G),
    'betweenness_centrality': nx.betweenness_centrality(G),
    'closeness_centrality': nx.closeness_centrality(G),
    'eigenvector_centrality': nx.eigenvector_centrality(G, max_iter=1000),
    'degree': dict(G.degree()),
    'closeness': dict(nx.closeness_centrality(G)),
    'betweenness': dict(nx.betweenness_centrality(G)),
    'eigenvector': dict(nx.eigenvector_centrality(G, max_iter=1000)),
}

for measure, values in centrality_measures.items():
    nx.set_node_attributes(G, values, measure)

# Map gender to numerical values
gender_mapping = {'Male': 0, 'Female': 1}
node_colors = [gender_mapping[G.nodes[node]['gender']] for node in G.nodes]

# Draw the graph with different colors for male and female nodes
pos = nx.spring_layout(G)  # You can choose a different layout if needed

# Plot the graph
nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.Blues, font_color='white')
plt.show()

# Export the graph to Gephi
nx.write_gexf(G, 'weighted_occurrences.gexf')

# Calculate and add clique measures
cliques = list(nx.find_cliques(G))

# Flatten the list of cliques to create a list of nodes in each clique
flattened_cliques = [node for clique in cliques for node in clique]

# Create a dictionary to map each node to its clique index
clique_dict = {node: idx for idx, nodes in enumerate(cliques) for node in nodes}
nx.set_node_attributes(G, clique_dict, 'clique_membership')
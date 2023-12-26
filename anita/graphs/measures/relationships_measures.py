import networkx as nx
import matplotlib.pyplot as plt
import json 
import community

# Load your Interactions Graph from the Gephi file or any other format
G = nx.read_gexf("graphs/relationships-graph.gexf")

# Calculate Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Calculate Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Calculate Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)

communities = community.best_partition(G)

# Local Clustering Coefficient
local_clustering = nx.clustering(G)

results = {
    "Degree Centrality": degree_centrality,
    "Betweenness Centrality": betweenness_centrality,
    "Closeness Centrality": closeness_centrality,
    "Communities": communities,
    "Local clustering": local_clustering
}

# Specify the file path where you want to store the results in JSON format
output_json_path = "graphs/measures/relationships-results.json"

# Write the results to a JSON file
with open(output_json_path, "w") as json_file:
    json.dump(results, json_file, indent=4)



print(f"Centrality measures saved to {output_json_path}")

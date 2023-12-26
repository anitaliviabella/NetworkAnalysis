import networkx as nx
import matplotlib.pyplot as plt
import json





# Sostituisci 'G' con il tuo grafo effettivo
Gc = nx.read_gexf("graphs/co-graph.gexf")
Gi = nx.read_gexf("graphs/interaction-graph.gexf")

#---------Archi x Ophelia e Queen Gertrude

# Nodi di interesse
nodi_interesse = ["Ophelia", "Queen Gertrude"]

# Estrai tutti gli archi collegati ai nodi di interesse
archi_interesse_co = [(nodo, vicino) for nodo in nodi_interesse for vicino in Gc.neighbors(nodo)]
archi_interesse_i = [(nodo, vicino) for nodo in nodi_interesse for vicino in Gi.neighbors(nodo)]
# Stampa gli archi
#co-occurrences edges
#[('Ophelia', 'Hamlet'), ('Ophelia', 'King Claudius'), ('Ophelia', 'Queen Gertrude'), ('Ophelia', 'Horatio'), ('Ophelia', 'Polonius'), ('Ophelia', 'Laertes'), ('Ophelia', 'Reynaldo'), ('Ophelia', 'Rosencrantz'), ('Ophelia', 'Guildenstern'), ('Ophelia', 'First Player'), ('Ophelia', 'Lucianus'), ('Ophelia', 'Player King'), ('Ophelia', 'Player Queen'), ('Ophelia', 'Gentleman'), ('Queen Gertrude', 'Hamlet'), ('Queen Gertrude', 'King Claudius'), ('Queen Gertrude', 'Polonius'), ('Queen Gertrude', 'Laertes'), ('Queen Gertrude', 'Voltimand'), ('Queen Gertrude', 'Cornelius'), ('Queen Gertrude', 'Lords'), ('Queen Gertrude', 'Attendants'), ('Queen Gertrude', 'Horatio'), ('Queen Gertrude', 'Marcellus'), ('Queen Gertrude', 'Bernardo'), ('Queen Gertrude', 'Rosencrantz'), ('Queen Gertrude', 'Guildenstern'), ('Queen Gertrude', 'Ambassadors'), ('Queen Gertrude', 'Players'), ('Queen Gertrude', 'First Player'), ('Queen Gertrude', 'Ophelia'), ('Queen Gertrude', 'Lucianus'), ('Queen Gertrude', 'Player King'), ('Queen Gertrude', 'Player Queen'), ('Queen Gertrude', 'Ghost'), ('Queen Gertrude', 'Gentleman'), ('Queen Gertrude', 'Messenger'), ('Queen Gertrude', 'First Clown'), ('Queen Gertrude', 'Second Clown'), ('Queen Gertrude', 'Priest'), ('Queen Gertrude', 'Osric'), ('Queen Gertrude', 'A Lord'), ('Queen Gertrude', 'Fortinbras'), ('Queen Gertrude', 'First Ambassador')]

#interactions edges
#[('Ophelia', 'Hamlet'), ('Ophelia', 'Polonius'), ('Ophelia', 'Laertes'), ('Queen Gertrude', 'Hamlet'), ('Queen Gertrude', 'King Claudius'), ('Queen Gertrude', 'Polonius'), ('Queen Gertrude', 'Laertes')]




#density
density_c = nx.density(Gc)
density_i = nx.density(Gi)

assortativity_c = nx.degree_assortativity_coefficient(Gc)
assortativity_i = nx.degree_assortativity_coefficient(Gi)

degree_distribution_c = dict(Gc.degree())
degree_distribution_i = dict(Gi.degree())



transitivity_c = nx.transitivity(Gc)
transitivity_i = nx.transitivity(Gi)

reciprocity_c = nx.algorithms.reciprocity(Gc)
reciprocity_i = nx.algorithms.reciprocity(Gi)






# Compute Average Clustering Coefficient
average_clustering_coefficient_c = nx.average_clustering(Gc)
average_clustering_coefficient_i = nx.average_clustering(Gi)


# Compute Total Triangles
total_triangles_c = sum(nx.triangles(Gc).values()) / 3  # Divide by 3 to avoid counting each triangle three times
total_triangles_i = sum(nx.triangles(Gi).values()) / 3  # Divide by 3 to avoid counting each triangle three times



print("Density co-occurrences", density_c)
print("Density interactions", density_i)
print("Assortativity co-occurrences", assortativity_c)
print("Assortativity  Interactions", assortativity_i,)
print("degree distribution co-occurrences", degree_distribution_c)
print("degree distribution interactions", degree_distribution_i)
print("transitivity co-occurrences", transitivity_c)
print("transitivity interactions", transitivity_i)
print('averagec', average_clustering_coefficient_c)
print('averagei', average_clustering_coefficient_i)



print('triangles_c',total_triangles_c )
print('traingles_i', total_triangles_i)

node1 = "Queen Gertrude"
node2 = "Ophelia"
jaccard_coefficients_c = list(nx.jaccard_coefficient(Gc, [(node1, node2)]))
jaccard_coefficients_i = list(nx.jaccard_coefficient(Gi, [(node1, node2)]))

# Extract Jaccard coefficients
jaccard_coefficient_c = jaccard_coefficients_c[0][2] if jaccard_coefficients_c else None
jaccard_coefficient_i = jaccard_coefficients_i[0][2] if jaccard_coefficients_i else None

print("Jaccard coefficient co-occurrences:", jaccard_coefficient_c)
print("Jaccard coefficient interactions:", jaccard_coefficient_i)

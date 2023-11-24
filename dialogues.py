import pandas as pd
# Existing interactions
interactions = [
    ('Bernardo', 'Francisco'),
    ('Bernardo', 'Francisco', 'Ghost'),
    ('Horatio', 'Marcellus', 'Ghost'),
    ('Horatio', 'Marcellus'),
    ('Hamlet', 'Queen Gertrude'),
    ('King Claudius', 'Laertes'),
    ('King Claudius', 'Hamlet'),
    ('Hamlet', 'Horatio'),
    ('Horatio', 'Marcellus', 'Bernardo'),
    ('Hamlet', 'Ghost'),
    ('Laertes', 'Ophelia'),
    ('Polonius', 'Ophelia', 'Laertes'),
    ('Hamlet', 'Horatio', 'Marcellus'),
    ('Hamlet', 'Horatio', 'Marcellus', 'Ghost'),
    ('Horatio', 'Marcellus'),
    ('Hamlet', 'Ghost'),
    ('Hamlet', 'Ghost'),
    ('Horatio', 'Marcellus'),
    ('Hamlet', 'Horatio', 'Marcellus', 'Ghost'),
    ('Hamlet', 'Horatio', 'Marcellus'),
    ('King Claudius', 'Queen Gertrude'),
    ('Rosencrantz', 'Guildenstern'),
    ('Hamlet', 'Players'),
    ('Hamlet', 'King Claudius'),
    ('King Claudius', 'Ambassadors from Norway'),
    ('Polonius', 'King Claudius'),
]

# Additional interactions
additional_interactions = [
    ('King Claudius', 'Queen Gertrude'),
    ('Rosencrantz', 'Guildenstern'),
    ('Hamlet', 'Ophelia'),
    ('Hamlet', 'Polonius'),
    ('Hamlet', 'Ophelia'),
    ('King Claudius', 'Polonius'),
    ('Hamlet', 'Players'),
    ('Hamlet', 'First Player'),
    ('Hamlet', 'Horatio'),
    ('Hamlet', 'Players'),
    ('Hamlet', 'Ophelia'),
    ('Hamlet', 'Queen Gertrude'),
    ("Hamlet", "Hamlet"),
    ('Hamlet', 'Guildenster', 'Rosencrantz'),
    ("Hamlet", 'Hamlet'),
    ('King Claudius', 'Rosencrantz', 'Guildenstern'),
    ('Rosencrantz', 'Guildenstern'),
    ('Polonius', 'King Claudius'),
    ('King Claudius', 'King Claudius'),
    ('Hamlet', 'Hamlet'),
    ('King Claudius', 'King Claudius'),
    ('Hamlet', 'Hamlet'),
    ('King Claudius'),
    ('Hamlet', 'Queen Gertrude'),
    ('Hamlet', 'Ghost'),
    ('Polonius', 'Queen Gertrude'),
    ('Hamlet', 'Polonius'),
]

# Additional interactions
additional_interactions_2 = [
    ('King Claudius', 'Queen Gertrude'),
    ('King Claudius', 'Rosencrantz', 'Guildenstern'),
    ('Hamlet', 'Rosencrantz', 'Guildenstern'),
    ('King Claudius', 'Hamlet'),
    ('Hamlet', 'Ophelia'),
    ('King Claudius', 'Laertes'),
    ('Horatio', 'The Servant'),
    ('First Sailor', 'Horatio'),
    ('King Claudius', 'Laertes Hamlet'),
    ('Messenger', 'King Claudius', 'Laertes'),
    ('King Claudius', 'Laertes'),
    ('Queen Gertrude', 'King Claudius', 'Laertes'),
]

# Additional interactions
additional_interactions_3 = [
    ('Hamlet', 'Horatio'),
    ('Hamlet', 'Osric'),
    ('Hamlet', 'Laertes'),
    ('King Claudius', 'Queen Gertrude'),
    ('Hamlet', 'King Claudius'),
    ('Laertes', 'King Claudius'),
    ('Hamlet', 'Fortinbras'),
]

# Unisci tutte le liste di interazioni
all_interactions = interactions + additional_interactions + additional_interactions_2 + additional_interactions_3

# Rimuovi duplicati
unique_interactions = list(set(tuple(sorted(pair)) for pair in all_interactions))

# Stampa l'elenco di coppie uniche
for pair in unique_interactions:
    print(pair)


from collections import defaultdict

# Unisci tutte le liste di interazioni
all_interactions = interactions + additional_interactions + additional_interactions_2 + additional_interactions_3

# Crea un dizionario per contare le occorrenze delle coppie di nomi
pair_count = defaultdict(int)

# Conta le occorrenze delle coppie di nomi
for pair in all_interactions:
    sorted_pair = tuple(sorted(pair))
    pair_count[sorted_pair] += 1

# Stampa l'elenco di coppie di nomi uniche e il numero di occorrenze
for pair, count in pair_count.items():
    print(f"{pair}: {count} times")

import pandas as pd
import numpy as np
from collections import defaultdict

# Unisci tutte le liste di interazioni
all_interactions = interactions + additional_interactions + additional_interactions_2 + additional_interactions_3

# Crea un dizionario per contare le occorrenze delle coppie di nomi
pair_count = defaultdict(int)

# Conta le occorrenze delle coppie di nomi
for interaction in all_interactions:
    sorted_pair = tuple(sorted(interaction))
    pair_count[sorted_pair] += 1

# Estrai l'elenco di tutti i nomi unici
unique_names = list(set([name for pair in pair_count.keys() for name in pair]))

# Crea una matrice vuota inizializzata a zero
matrix = np.zeros((len(unique_names), len(unique_names)), dtype=int)

# Riempie la matrice con il numero di interazioni tra ciascuna coppia di nomi
for pair, count in pair_count.items():
    indices = [unique_names.index(name) for name in pair]
    matrix[indices, indices] = count

# Crea un DataFrame con la matrice
df_matrix = pd.DataFrame(matrix, index=unique_names, columns=unique_names)

# Stampa il DataFrame con la matrice delle interazioni
print(df_matrix)
df_matrix.to_csv('interactions.csv')

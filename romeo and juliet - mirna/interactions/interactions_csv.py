import csv

attributes_interactions = [
    ("Character1", "Character2", "Number of Interactions"),
    ("Romeo", "Juliet", 6),
    ("Romeo", "Mercutio", 3),
    ("Romeo", "Benvolio", 4),
    ("Romeo", "Nurse", 2),
    ("Juliet", "Nurse", 4),
    ("Juliet", "Paris", 1),
    ("Paris", "Romeo", 1),
    ("Friar Lawrence", "Romeo", 5),
    ("Friar Lawrence", "Juliet", 3),
    ("Lord Capulet", "Romeo", 3),
    ("Lord Capulet", "Juliet", 1),
    ("Paris", "Lord Capulet", 4),
    ("Lady Capulet", "Juliet", 1),
    ("Lady Capulet", "Nurse", 2),
    ("Lady Montague", "Lord Montague", 3),
    ("Lord Montague", "Lord Capulet", 2),
    ("Friar Lawrence", "Paris", 1),
    ("Tybalt", "Lord Capulet", 2),
    ("Tybalt", "Benvolio", 3),
    ("Tybalt", "Mercutio", 2),
    ("Tybalt", "Romeo", 3)

]

# Nome del file CSV
csv_filename = 'interactions.csv'

# Apertura del file CSV in modalità scrittura
with open(csv_filename, 'w', newline='') as csv_file:
    # Creazione dell'oggetto scrittore CSV
    csv_writer = csv.writer(csv_file)

    # Scrittura dei dati nel file CSV
    csv_writer.writerows(attributes_interactions)
import csv

# Sample data with more characters
data = [
    ["Character", "Gender", "Role"],
    ["Romeo", "Male", "Protagonist"],
    ["Juliet", "Female", "Protagonist"],
    ["Mercutio", "Male", "Friend of Romeo"],
    ["Tybalt", "Male", "Romeo's Enemy"],
    ["Friar Lawrence", "Male", "Franciscan Friar"],
    ["Nurse", "Female", "Juliet's Nurse"],
    ["Benvolio", "Male", "Romeo's Cousin"],
    ["Paris", "Male", "Juliet's Suitor"],
    ["Lord Capulet", "Male", "Juliet's Father"],
    ["Lady Capulet", "Female", "Juliet's Mother"],
    ["Lord Montague", "Male", "Romeo's Father"],
    ["Lady Montague", "Female", "Romeo's Mother"],
    ["Prince Escalus", "Male", "Prince of Verona"],
]

# Specify the CSV file path
csv_file_path = "romeo_and_juliet_characters.csv"

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(data[0])
    
    # Write the data rows
    writer.writerows(data[1:])

print(f"The data has been successfully written to the CSV file: {csv_file_path}")

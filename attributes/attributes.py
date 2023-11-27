import pandas as pd
genere_dict = {
    'Hamlet': 'Male',
    'King Claudius': 'Male',
    'Queen Gertrude' : 'Female',
    'Horatio': 'Male',
    'Polonius': 'Male',
    'Laertes': 'Male',
    'Ophelia': 'Female',
    'Bernardo': 'Male',
    'Francisco': 'Male',
    'Marcellus': 'Male',
    'Ghost': 'Male',
    'King Fortinbras': 'Male',
    'Voltimand': 'Male',
    'Lords': 'Male',
    'Attendants': 'Male',
    'Rosencrantz': 'Male',
    'Guildenstern': 'Male',
    'Ambassadors from Norway': 'Male',
    'Players': 'Male',
    'First Player': 'Male',
    'Reynaldo': 'Male',
    'Lucianus': 'Male',
    'Player King': 'Male',
    'Player Queen': 'Male', 
    'Prince Fortinbras': 'Male', 
    'Captain': 'Male', 
    'Gentlemen': 'Male',
    'Servant': 'Male',
    'First Sailor': 'Male',
    'First Clown': 'Male',
    'Second Clown': 'Male', 
    'Priest': 'Male',
    'First Ambassador': 'Male',
    'Osric': 'Male',
    'A Lord': 'Male',
    'Cornelius': 'Male',
    'Messenger': 'Male',
    'Fortinbras': 'Male',

}

# Create a DataFrame from the dictionary
df = pd.DataFrame(list(genere_dict.items()), columns=['Character', 'Gender'])

# Save the DataFrame to a CSV file
df.to_csv('attributes/attributes.csv', index=False)

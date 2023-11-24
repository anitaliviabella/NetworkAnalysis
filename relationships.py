import pandas as pd

import pandas as pd

# Create an empty dataframe with characters as columns and index
characters = ['Hamlet', 'King Hamlet', 'Queen Gertrude', 'King Claudius', 'Ophelia', 'Horatio', 'Polonius', 'Laertes']
relationships_df = pd.DataFrame(0, index=characters, columns=characters)

# Update the dataframe based on relationships
relationships_df.loc['Hamlet', 'King Hamlet'] += 1  # type: fatherhood
relationships_df.loc['Hamlet', 'Queen Gertrude'] += 1  # type: motherhood
relationships_df.loc['Hamlet', 'King Claudius'] += 1  # type: unclehood
relationships_df.loc['Hamlet', 'Ophelia'] += 1  # type: relationship
relationships_df.loc['King Claudius', 'Queen Gertrude'] += 1  # type: marriage
relationships_df.loc['King Claudius', 'King Hamlet'] += 1  # type: brotherhood
relationships_df.loc['Polonius', 'Laertes'] += 1  # son
relationships_df.loc['Polonius', 'Ophelia'] += 1  # daughter
relationships_df.loc['Laertes', 'Ophelia'] += 1  # brotherhood
relationships_df.loc['Queen Gertrude', 'King Hamlet'] += 1  # ex husband
relationships_df.loc['Hamlet', 'Horatio'] += 1  # friendship

# Save the dataframe to a CSV file in the 'all' directory
relationships_df.to_csv('relationships_matrix.csv')

print("Relationships matrix has been saved to 'relationships_matrix.csv'")

import pandas as pd

#-------------FIRST ACT--------------
# Creating a DataFrame
data1 = {'Character': ['Francisco', 'Bernardo', 'Marcellus', 'Horatio', 'Ghost', 'King Fortinbras', 'Hamlet']}
df1 = pd.DataFrame(data1)

# Exporting the DataFrame to a CSV file
df1.to_csv('co/scene_1.csv', index=False)


#2
characters2 = [
    "King Claudius",
    "Queen Gertrude",
    "Hamlet",
    "Polonius",
    "Laertes",
    "Voltimand",
    "Cornelius",
    "Lords",
    "Attendants",
    "Horatio",
    "Marcellus",
    "Bernardo"]

# Create a data frame from the list
df2 = pd.DataFrame({"Character": characters2})

# Convert the data frame to a CSV file
df2.to_csv("co/scene_2.csv", index=False)


#3
# Updated list of characters
characters3 = ['Laertes', 'Ophelia', 'Polonius']

# Creating a data frame
df3 = pd.DataFrame({'Character': characters3})

# Saving the data frame to a CSV file
df3.to_csv('co/scene_3.csv', index=False)

#4
# Updated list of characters
characters4 = ['Hamlet', 'Horatio', 'Marcellus', 'Ghost']

# Creating a data frame
df4 = pd.DataFrame({'Character': characters4})

# Saving the data frame to a CSV file
df4.to_csv('co/scene_4.csv', index=False)

#5
# Updated list of characters
characters_scene_5 = ['Hamlet', 'Ghost', 'Horatio', 'Marcellus']

# Creating a data frame
df_scene_5 = pd.DataFrame({'Character': characters_scene_5})

# Saving the data frame to a CSV file
df_scene_5.to_csv('co/scene_5.csv', index=False)



#------------SECOND ACT-------------
# Updated list of characters
characters_scene_2 = ['Polonius', 'Reynaldo', 'Ophelia']

# Creating a data frame
df_scene_2 = pd.DataFrame({'Character': characters_scene_2})

# Saving the data frame to a CSV file
df_scene_2.to_csv('co/act2_scene_1.csv', index=False)


# Creating a DataFrame
data = {
    "Character": ["King Claudius", "Queen Gertrude", "Rosencrantz", "Guildenstern", "Attendants",
                   "Polonius", "Voltimand", "Cornelius", "Ambassadors", "Hamlet",
                   "Players", "First Player"],
}

df = pd.DataFrame(data)

# Converting DataFrame to CSV
df.to_csv('co/act_2_scene_2.csv', index=False)

#-------THIRD ACT---------
#scene1
# Creating a DataFrame with the characters
characters_act3_1 = ['King Claudius', 'Queen Gertrude', 'Polonius', 'Ophelia', 'Rosencrantz', 'Guildenstern', 'Hamlet']
df_characters_3_1 = pd.DataFrame({'Character': characters_act3_1})

# Convert to CSV
df_characters_3_1.to_csv('co/act3_scene_1.csv', index=False)

#scene2
# List of characters
characters_3_2 = ["Hamlet", "First Player", "Polonius", "Rosencrantz", "Guildenstern", 
              "Horatio", "Queen Gertrude", "Lucianus", "Player King", 
              "Player Queen", "King Claudius", "Ophelia"]

# Create a DataFrame
df_characters_3_2 = pd.DataFrame({"Character": characters_3_2})

# Convert to CSV
df_characters_3_2.to_csv("co/act3_scene_2.csv", index=False)


#scene3
# List of characters
characters_3_3 = ["King Claudius", "Rosencrantz", "Guildenstern", "Polonius", "Hamlet"]

# Creating a DataFrame
df_3_3 = pd.DataFrame({"Character": characters_3_3})

# Save the DataFrame to a CSV file
df_3_3.to_csv("co/act3_scene_3.csv", index=False)

#scene4
# List of characters
characters_scene4 = ["Polonius", "Hamlet", "Queen Gertrude", "Ghost"]

# Creating a DataFrame
df_scene4 = pd.DataFrame({"Character": characters_scene4})

# Save the DataFrame to a CSV file
df_scene4.to_csv("co/act3_scene_4.csv", index=False)



#-------FORTH ACT--------
#scene1
# List of characters
characters_scene1 = ["King Claudius", "Queen Gertrude", "Rosencrantz", "Guildenstern"]

# Creating a DataFrame
df_scene1 = pd.DataFrame({"Character": characters_scene1})

# Save the DataFrame to a CSV file
df_scene1.to_csv("co/act4_scene1.csv", index=False)

#scene2
# List of characters
characters_scene2 = ["Hamlet", "Rosencrantz", "Guildenstern"]

# Creating a DataFrame
df_scene2 = pd.DataFrame({"Character": characters_scene2})

# Save the DataFrame to a CSV file
df_scene2.to_csv("co/act4_scene2.csv", index=False)

#scene3
# List of characters
characters_scene3 = ["King Claudius", "Rosencrantz", "Hamlet", "Guildenstern"]

# Creating a DataFrame
df_scene3 = pd.DataFrame({"Character": characters_scene3})

# Save the DataFrame to a CSV file
df_scene3.to_csv("co/act4_scene3.csv", index=False)

#scene4
# List of characters
characters_scene4 = ["Fortinbras", "Captain", "Hamlet", "Rosencrantz", "Guildenstern"]

# Creating a DataFrame
df_scene4 = pd.DataFrame({"Character": characters_scene4})

# Save the DataFrame to a CSV file
df_scene4.to_csv("co/act4_scene4.csv", index=False)


#scene5
# List of characters
characters_scene5 = ["Queen Gertrude", "Horatio", "Gentleman", "Ophelia", "King Claudius", "Laertes"]

# Creating a DataFrame
df_scene5 = pd.DataFrame({"Character": characters_scene5})

# Save the DataFrame to a CSV file
df_scene5.to_csv("co/act4_scene5.csv", index=False)

#scene6
# List of characters
characters_scene6 = ["Horatio", "Servant", "First Sailor"]

# Creating a DataFrame
df_scene6 = pd.DataFrame({"Character": characters_scene6})

# Save the DataFrame to a CSV file
df_scene6.to_csv("co/act4_scene6.csv", index=False)

#scene7
# List of characters
characters_scene7 = ["King Claudius", "Laertes", "Messenger", "Queen Gertrude"]

# Creating a DataFrame
df_scene7 = pd.DataFrame({"Character": characters_scene7})

# Save the DataFrame to a CSV file
df_scene7.to_csv("co/act4_scene7.csv", index=False)

#scene1
# List of characters
characters_scene1 = ["First Clown", "Second Clown", "Hamlet", "Horatio", "Priest", "Laertes", "King Claudius", "Queen Gertrude"]

# Creating a DataFrame
df_scene1 = pd.DataFrame({"Character": characters_scene1})

# Save the DataFrame to a CSV file
df_scene1.to_csv("co/act5_scene1.csv", index=False)

#scene2
# Create a DataFrame with the characters
characters_data = {
    "Character": ["Hamlet", "Horatio", "King Claudius", "Queen Gertrude", "Laertes", "Osric", "A Lord", "Fortinbras", "First Ambassador"],
}

characters_df = pd.DataFrame(characters_data)

# Save the DataFrame to a CSV file
characters_df.to_csv("co/act5_scene2.csv", index=False)
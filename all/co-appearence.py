import pandas as pd
from itertools import combinations

# Function to read CSV file and generate character pairs
def process_scene_csv(file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Extract the 'Character' column
    characters = df['Character'].tolist()

    # Generate all possible combinations of characters (couples)
    character_combinations = list(combinations(characters, 2))

    return character_combinations

# Function to count occurrences of character pairs across all scenes
def count_character_pairs(scene_files):
    # Dictionary to store counts of character pairs
    character_counts = {}

    # Process each scene file
    for file_path in scene_files:
        scene_pairs = process_scene_csv(file_path)

        # Update counts based on character pairs in the current scene
        for pair in scene_pairs:
            # Sort the pair to handle cases where the order of characters doesn't matter
            sorted_pair = tuple(sorted(pair))
            
            # Update or initialize the count for the character pair
            character_counts[sorted_pair] = character_counts.get(sorted_pair, 0) + 1

    return character_counts

# Example usage:
scene_files = ['all/scene_1.csv', 'all/scene_2.csv', 'all/scene_3.csv', 'all/scene_4.csv', 'all/scene_5.csv', 'all/act2_scene_1.csv', 'all/act_2_scene_2.csv', 'all/act3_scene_1.csv', 'all/act3_scene_2.csv', 'all/act3_scene_3.csv', 'all/act3_scene_4.csv', 'all/act4_scene1.csv', 'all/act4_scene2.csv', 'all/act4_scene3.csv', 'all/act4_scene4.csv', 'all/act4_scene5.csv', 'all/act4_scene6.csv', 'all/act4_scene7.csv','all/act5_scene1.csv', 'all/act5_scene2.csv'] # Add your actual file paths here
result = count_character_pairs(scene_files)

# Print the results
for pair, count in result.items():
    print(f"Character Pair: {pair}, Count: {count}")

# Convert the result dictionary to a DataFrame for easier handling
result_df = pd.DataFrame(list(result.items()), columns=['Character Pair', 'Count'])
# Save the result to a CSV file
result_df.to_csv('character_pairs_counts.csv', index=False)
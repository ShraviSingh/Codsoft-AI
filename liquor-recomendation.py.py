# Sample liquor data: [name, type, sweetness, bitterness, strength]
liquor_data = [
    ["Whiskey", "Spirit", 2, 1, 5],
    ["Gin", "Spirit", 1, 2, 4],
    ["Rum", "Spirit", 3, 2, 4],
    ["Vodka", "Spirit", 1, 1, 3],
    ["Tequila", "Spirit", 2, 3, 4],
    ["Red Wine", "Wine", 3, 2, 3],
    ["White Wine", "Wine", 2, 1, 2],
    ["Beer", "Beer", 1, 1, 1],
    ["Cider", "Beer", 2, 2, 2],
    ["Champagne", "Wine", 1, 1, 3],
    ["Brandy", "Spirit", 2, 1, 4],
    ["Sake", "Spirit", 3, 1, 2],
    ["Port Wine", "Wine", 4, 3, 3],
    ["Scotch", "Spirit", 2, 1, 5],
    ["Irish Whiskey", "Spirit", 1, 1, 4],
    ["Margarita", "Cocktail", 2, 3, 4],
    ["Martini", "Cocktail", 1, 2, 3],
    ["Mojito", "Cocktail", 3, 2, 3],
    ["Cosmopolitan", "Cocktail", 2, 1, 4],
    ["Negroni", "Cocktail", 1, 3, 4]
]

# Function to calculate cosine similarity
def cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude_v1 = sum(x * x for x in v1) ** 0.5
    magnitude_v2 = sum(y * y for y in v2) ** 0.5
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0
    return dot_product / (magnitude_v1 * magnitude_v2)

# Function to recommend liquors based on user preferences
def recommend_liquors(preferences, liquor_data, num_recommendations=3):
    user_profile = [preferences["sweetness"], preferences["bitterness"], preferences["strength"]]
    similarities = [cosine_similarity(user_profile, liquor[2:]) for liquor in liquor_data]
    sorted_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    recommended_liquors = []
    seen_liquors = set()
    
    for idx in sorted_indices:
        liquor_name = liquor_data[idx][0]
        if liquor_name not in seen_liquors:
            recommended_liquors.append((liquor_name, liquor_data[idx][1], liquor_data[idx][2], liquor_data[idx][3], liquor_data[idx][4]))
            seen_liquors.add(liquor_name)
            if len(recommended_liquors) >= num_recommendations:
                break
    
    return recommended_liquors

# Function to search for liquors based on keywords
def search_liquors(keyword, liquor_data):
    matches = []
    for liquor in liquor_data:
        if keyword.lower() in liquor[0].lower() or keyword.lower() == liquor[1].lower():
            matches.append(liquor)
    return matches

# User preferences (sweetness, bitterness, strength)
user_preferences = {"sweetness": 2, "bitterness": 1, "strength": 4}

# Get liquor recommendations for the user
recommendations = recommend_liquors(user_preferences, liquor_data)

# User input for keyword search
search_keyword = input("Search for a liquor by keyword: ")
search_results = search_liquors(search_keyword, liquor_data)

print("\nRecommended liquors based on user preferences:")
for liquor, liquor_type, sweetness, bitterness, strength in recommendations:
    print(f"{liquor:<15} | Type: {liquor_type:<10} | Sweetness: {sweetness}/10 | Bitterness: {bitterness}/10 | Strength: {strength}/10")

print("\nLiquors matching your search:")
if search_results:
    for liquor in search_results:
        print(f"{liquor[0]:<15} | Type: {liquor[1]:<10} | Sweetness: {liquor[2]}/10 | Bitterness: {liquor[3]}/10 | Strength: {liquor[4]}/10")
else:
    print("No matching liquors found.")

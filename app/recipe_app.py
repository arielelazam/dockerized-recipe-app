# Inventory and business logic of the application

import os
from flask import Flask, jsonify

app = Flask(__name__) # Initialize the Flask server application

USER_NAME = os.environ.get("USER_NAME", "Guest") # Retrieve the username from environment variables

# Available recipes
RECIPES = {
    "Omelette": ["eggs", "butter", "salt"],
    "Pasta": ["pasta", "tomatoes", "garlic"],
    "Cheese Toast": ["bread", "cheese", "butter", "tomatoes"],
    "Salad": ["tomato", "cucumber", "olive oil"],
    "Fried Eggs": ["eggs", "oil", "salt"],
    "Rice with vegetables": ["rice", "carrot", "onion"]
}

# Function to read the inventory file and return available items
def read_inventory():
    try:
        with open("/data/inventory.txt", "r") as f:
            items = [line.strip().lower() for line in f if line.strip()]
        return items
    except FileNotFoundError:
        return []

# Function that receives the available inventory and recommends the recipe
# with the highest number of ingredients, provided all its ingredients are in stock
# (prioritizing richer meals)
def suggest_recipe(inventory):
    best_recipe = None
    best_score = 0

    for recipe, ingredients in RECIPES.items():
        if all(i in inventory for i in ingredients):
            score = len(ingredients)
            if score > best_score:
                best_score = score
                best_recipe = recipe
    return best_recipe, best_score

@app.route("/api") # Define the endpoint for requests directed to /api
def api():
    inventory = read_inventory() # Retrieve available inventory
    recipe, score = suggest_recipe(inventory) # Get the recommended recipe and its score

    if not recipe or score == 0: # If no suitable recipe is found, return a fallback message
        return jsonify({"user": USER_NAME, "message": "No ingredients found to suggest a recipe", "inventory": inventory})
    return jsonify({"user": USER_NAME, "recipe": recipe, "matched_ingredients": score, "inventory": inventory}) # Return the recommended recipe details to the client

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
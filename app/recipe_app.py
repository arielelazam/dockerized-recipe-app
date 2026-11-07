# קובץ המלאי והלוגיקה של התוכנית

import os
from flask import Flask, jsonify

app = Flask(__name__) # יצרת השרת שישמש אותנו

USER_NAME = os.environ.get("USER_NAME", "Guest") # שליפת שם המשתמש

# המתכונים הקיימים
RECIPES = {
    "Omelette": ["eggs", "butter", "salt"],
    "Pasta": ["pasta", "tomatoes", "garlic"],
    "Cheese Toast": ["bread", "cheese", "butter", "tomatoes"],
    "Salad": ["tomato", "cucumber", "olive oil"],
    "Fried Eggs": ["eggs", "oil", "salt"],
    "Rice with vegetables": ["rice", "carrot", "onion"]
}

# הפונקציה שניגשת למלאי ומחזירה את המוצרים הזמינים
def read_inventory():
    try:
        with open("/data/inventory.txt", "r") as f:
            items = [line.strip().lower() for line in f if line.strip()]
        return items
    except FileNotFoundError:
        return []

# הפונקציה שתקבל את המוצרים הזמינים ומבין המתכונים שכל מוצריהם קיימים במלאי, תמליץ על זה שמורכב מכמה שיותר מוצרים - ארוחה עשירה יותר
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

@app.route("/api") # נגדיר שאם מישהו פונה לכתובת ה-IP של הקונטיינר בפורט 5000 עם סיומת api/ הפונקציה api תופעל
def api():
    inventory = read_inventory() # נשלוף את המלאי הזמין
    recipe, score = suggest_recipe(inventory) # נקבל את המתכון המומלץ ואת הניקוד שלו

    if not recipe or score == 0: # אם לא התקבל מתכון מומלץ תוחזר ללקוח הודעה שלא נמצא מתכון זמין
        return jsonify({"user": USER_NAME, "message": "No ingredients found to suggest a recipe", "inventory": inventory})
    return jsonify({"user": USER_NAME, "recipe": recipe, "matched_ingredients": score, "inventory": inventory}) # נחזיר ללקוח הודעה שתכיל את פרטי המתכון

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
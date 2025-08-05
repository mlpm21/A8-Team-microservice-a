# A8-Team-microservice-a
Nutrition Macros Microservice A

This microservice returns nutrition information (protein, fat, carbs) for a given menu item using data from a local CSV file.

GET http://localhost:5001/nutrition

------------------------------------------------------------------------------------------------------
-- How to REQUEST Data
must send a GET request to the `/nutrition` endpoint with a query parameter named 'menu_item_name'.
### Example Request (Python)

import requests

response = requests.get(
    "http://localhost:5001/nutrition",
    params={"menu_item_name": "Chicken"}
)

------------------------------------------------------------------------------------------------------
-- How to RECEIVE Data
- If the menu item exists, the microservice responds with a JSON:

{
  "item": "Chicken",
  "protein": "15g",
  "fat": "3g",
  "carbs": "0g"
}

- If the item is not found, it responds with:
{
  "error": "Item not found"
}

- To acess the data in the code:

data = response.json()
if "error" in data:
    print("Item not found.")
else:
    print("Protein:", data["protein"])

------------------------------------------------------------------------------------------------------

This service runs locally on port 5001

You must have Flask installed: pip install flask

The microservice loads data from menu.csv

------------------------------------------------------------------------------------------------------


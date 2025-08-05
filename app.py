from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# load the CSV data
def load_menu_data():
    data = {}

    with open('menu.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            item = row['item'].lower()

            data[item] = {
                'item': row['item'],
                'protein': row['protein'],
                'fat': row['fat'],
                'carbs': row['carbs']
            }
    return data

menu_data = load_menu_data()

@app.route('/nutrition', methods=['GET'])
def get_nutrition():
    item_name = request.args.get('menu_item_name', '').lower()

    if item_name in menu_data:
        return jsonify(menu_data[item_name])
    
    else:
        return jsonify({"error": "Item not found"}), 404


@app.route('/')
def home():
    return '''
        <h2>Nutrition Macros Microservice A</h2>
        <p>Use endpoint: /nutrition?menu_item_name=Chicken</p>
        <a href="/categories">Back to Categories</a>
    '''


@app.route('/categories')
def categories():
    return '''
        <h3>Categories Page (Placeholder)</h3>
        <p>This is a mock categories page.</p>
    '''


if __name__ == '__main__':
    app.run(port=5001)

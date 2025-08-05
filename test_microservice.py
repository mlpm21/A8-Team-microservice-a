import requests

# example item
item = "Chicken"
url = "http://localhost:5001/nutrition"
params = {"menu_item_name": item}


try:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Correct Nutrition Info for ", item)
        print(response.json())

    else:
        print("Error:", response.status_code)
        print(response.json())

except Exception as e:
    print("Could not connect to microservice: ", e)


# test an invalid item
invalid_item = "Unicorn"
params = {"menu_item_name": invalid_item}
response = requests.get(url, params=params)

print("\nTesting invalid item:", invalid_item)
print("Response:", response.json())

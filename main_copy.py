import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "pixela_token"
GRAPH_ID = "graph_name"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Log in:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "First cycling graph",  # can be anything
    "unit": "Km",  # can be any measures, read the documentation for details
    "type": "float",
    "color": "ajisai"  # special colors, see documentation
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response2.text)

# Add a Pixel to the Graph - POST
pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# the string f time - strftime
today = datetime.now()
today = today.strftime("%Y%m%d")

yesterday = datetime(year=2023, month=1, day=18)
yesterday = yesterday.strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": input("How many kilometers have you cycled today? "),
    }

response3 = requests.post(url=pixel_add_endpoint, headers=headers, json=pixel_config)
print(response3.text)

# Update data - PUT
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
pixel_update_config = {
    "quantity": "4",

}
# response4 = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update_config)
# print(response4.text)


# Delete data - DELETE
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

# response5 = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response5.text)

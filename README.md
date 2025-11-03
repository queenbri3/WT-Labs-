# WT-Labs-


## Section 1: Webex Messaging API (7 marks)✅
| Criteria | Details |
|---------|---------|
| API Base URL | https://webexapis.com/v1 |
| Authentication Method | `_______________________________` |
| Endpoint to list rooms | https://webexapis.com/v1/rooms |
| Endpoint to get messages | https://webexapis.com/v1/messages |
| Endpoint to send message | https://webexapis.com/v1/messages |
| Required headers |  |headers = {"Authorization": "Bearer " + accessToken})
| Sample full GET or POST request | import requests import json

headers = {"Authorization": f"Bearer {accessToken}", "Content-Type": "application/json; charset=utf-8"}

r = requests.get("https://webexapis.com/v1/rooms", headers = {"Authorization": "Bearer " + accessToken})

if not r.status_code == 200:
    raise Exception ("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

print("\nList of available rooms:")

rooms = r.json()["items"]
for room in rooms:
    print(f"Type: '{room.get('type')}' Name: {room.get('title')}") |
---
## Section 2: ISS Current Location API (3 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `_______________________________` |
| Endpoint for current ISS location | `_______________________________` |
| Sample response format (example JSON) |
```
```
|
---
## Section 3: Geocoding API (LocationIQ or Mapbox or other) (6 marks)
| Criteria | Details |
|---------|---------|
| Provider used (circle one) | **LocationIQ / Mapbox/ other -provide detail** |
| API Base URL | `_______________________________` |
| Endpoint for reverse geocoding | `_______________________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample request with latitude/longitude | `_______________________________` |
| Sample JSON response (formatted example) |
```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## 🚀 Section 5: Web Architecture & MVC Design Pattern (12 marks)
### 🚀 Web Architecture – Client-Server Model
- **Client**:
- **Server**:
- (Explain the communication between them & include a block diagram )
### 🚀 RESTful API Usage
-
-
-
### 🚀 MVC Pattern in Space Bot
| Component | Description |
|------------|-------------|
| **Model** | |
| **View** | |
| **Controller** | |
#### Example:
- Model:
- View:
- Controller:
---
### 🚀 Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---

# WT-Labs-


## Section 1: Webex Messaging API (7 marks)✅
| Criteria | Details |
|---------|---------|
| API Base URL | https://webexapis.com/v1 |
| Authentication Method | Bearer Token |
| Endpoint to list rooms | https://webexapis.com/v1/rooms |
| Endpoint to get messages | https://webexapis.com/v1/messages |
| Endpoint to send message | https://webexapis.com/v1/messages |
| Required headers | headers = {"Authorization": "Bearer " + accessToken}) |
| Sample full GET or POST request |  |
---
## Section 2: ISS Current Location API (3 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | http://api.open-notify.org |
| Endpoint for current ISS location | http://api.open-notify.org/iss-now.json |
| Sample response format (example JSON) |
```
```
|
---
## Section 3: Geocoding API (LocationIQ or Mapbox or other) (6 marks)
| Criteria | Details |
|---------|---------|
| Provider used (circle one) | OpenWeatherMap|
| API Base URL | http://api.openweathermap.org/geo/1.0 |
| Endpoint for reverse geocoding |http://api.openweathermap.org/geo/1.0/reverse |
| Authentication method | API key (appid) |
| Required query parameters | lat, lon, limit, appid |
| Sample request with latitude/longitude | |
| Sample JSON response (formatted example) |
```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | import time|
| Function used to convert epoch | time.ctime(epoch)|
| Sample code to convert timestamp |  timestamp = json_data, ["timestamp"] timeString = time.ctime(timestamp)
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## 🚀 Section 5: Web Architecture & MVC Design Pattern (12 marks)
### 🚀 Web Architecture – Client-Server Model
- **Client**: Visual Studio Code was running so that the bot code can be executed
- **Server**: Webex API server, OpenWeatherMap, Postman, ISS API server
-  **Communication**: The bot sends a GET request to the Webex API to get the messages from the room. The server then responds with the data in JSON. The bot reads the messages, processes them and gets the ISS location via the GET request to ISS API. The bot then sends a POST request to the Webex API to post the ISS message.
## Block Diagram 

<img width="502" height="401" alt="image" src="https://github.com/user-attachments/assets/968b2750-735e-463e-a53c-f731b2cb88c8" />


### 🚀 RESTful API Usage
- The bot communicates with Webex API, ISS location and OpenWeatherMap using HTTP GET and POST
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

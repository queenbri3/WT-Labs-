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
| Sample full GET or POST request |<img width="538" height="423" alt="image" src="https://github.com/user-attachments/assets/6d881aa7-1cf6-474a-9486-61f142d4226e" />
  |
---
## Section 2: ISS Current Location API (3 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | http://api.open-notify.org |
| Endpoint for current ISS location | http://api.open-notify.org/iss-now.json |
| Sample response format (example JSON) | <img width="459" height="222" alt="image" src="https://github.com/user-attachments/assets/055c968b-4eae-4fd9-89f6-f14df5672379" />


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
| Sample request with latitude/longitude |<img width="244" height="115" alt="image" src="https://github.com/user-attachments/assets/0913e066-3592-4dc6-9b5c-6b5059ff74e4" />
 |
| Sample JSON response (formatted example) | <img width="919" height="267" alt="image" src="https://github.com/user-attachments/assets/0601b386-6b88-43c0-ad05-615608d65e5a" />

```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | import time|
| Function used to convert epoch | time.ctime(epoch)|
| Sample code to convert timestamp | <img width="285" height="48" alt="image" src="https://github.com/user-attachments/assets/236aa443-8e53-4728-a956-9a232af73d54" />

```
```
|
| Output (human-readable time) | <img width="325" height="15" alt="image" src="https://github.com/user-attachments/assets/5dc13097-dfc6-4a3c-b690-786dd1aab4ec" />
 |
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
- Uses URL endpoints, stateless requests and HTTP verbs
- APIs return JSON responses that the bot processes
### 🚀 MVC Pattern in Space Bot
| Component | Description |
|------------|-------------|
| **Model** |Holds data and business logic |
| **View** | Displays information to the user|
| **Controller** |Handles user input and API interaction |
#### Example:
- Model: lat = json_data["iss_position"]["latitude"]
lng = json_data["iss_position"]["longitude"]

- View: print("Received message:", message)
print("Sending to Webex:" + responseMessage)

- Controller: if message.find("/") == 0:
    seconds = int(message[1:])
    time.sleep(seconds)
    

---
### 🚀 Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---

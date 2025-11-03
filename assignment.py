#Importing libraries 

import requests
import json
import time
import re 
import sys 
import pycountry

#Asking for Token 


choice = input("Do you want to use the hard-coded access token? (y/n)? ")

if choice == "y":
    accessToken = "Bearer MjlhN2UyNzktMWFiZi00ZTY4LTlkODEtZTRlOTE0ZDQzYjQ1OTg0YzYzY2YtYTk0_P0A1_bdd2aed2-da17-481d-bd6f-b43037ee90b7"
    if not accessToken:
        accessToken = input("Enter Webex Token: ").strip()
else:
    accessToken = input("Enter Webex token: ").strip()

if not accessToken:
    print ("No token provided. Exiting")
    sys.exit(1)

headers = {"Authorization": f"Bearer {accessToken}", "Content-Type": "application/json; charset=utf-8"}


#Webex rooms API URL

r = requests.get("https://webexapis.com/v1/rooms", headers = {"Authorization": "Bearer " + accessToken})


if not r.status_code == 200:
    raise Exception ("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

# Loop to print the type and title of each room 

print("\nList of available rooms:")

rooms = r.json()["items"]
for room in rooms:
    print(f"Type: '{room.get('type')}' Name: {room.get('title')}")


#Search for Webex room to monitor 
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages?").strip()
    roomIdToGetMessages = None


    for room in rooms:
        if(room["title"].find(roomNameToSearch) != -1):
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break


    if(roomIdToGetMessages == None) : 
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")

    else:
        break

Last_message_id = None

while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }

    r = requests.get("https://webexapis.com/v1/messages", params = GetParameters, headers = {"Authorization": "Bearer " + accessToken})
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))
    
    json_data = r.json ()

    if len(json_data["items"]) == 0:
        print("No messages found in the room.")
        continue


    messages = json_data["items"]
    message = messages[0]["text"]
    message_id = messages[0]["id"]

    if message_id != Last_message_id:
        print("Received message:", message)
        Last_message_id = message_id

    if message.find("/") == 0:
        if(message[1:].isdigit()):
            seconds = int(message[1:])
        
        else:
            print("Error: Message after '/' is not a number.")
            continue

        if seconds > 5:
                seconds = 5 
            
        time.sleep(seconds)


        r = requests.get("http://api.open-notify.org/iss-now.json")
        json_data = r.json()

        if r.status_code != 200:
            print("Error: Failed to retreive ISS location.")
            print("Status code:", r.status_code)
            print("Response text:", r.text)
        else:
        
            lat = json_data ["iss_position"]["latitude"]
            lng = json_data ["iss_position"]["longitude"]

            timestamp = json_data ["timestamp"]
            timeString = time.ctime(timestamp)

            OpenWeathermapkey = "4b60b277f44bb1c395d8d3fefd1fc983"

            print(f"On {timeString}, the ISS was at {lat}, {lng}")

            mapsAPIGetParameters = {
                "lat": lat,
                "lon": lng,
                "limit": 1,
                "appid": OpenWeathermapkey
             }
            
            r = requests.get("http://api.openweathermap.org/geo/1.0/reverse", params = mapsAPIGetParameters)

            json_data = r.json()

            responseMessage = f"On {timeString}, the ISS was flying over a body of water at latitude {lat}* and longitude {lng}*."

            if r.status_code != 200 or len(json_data) == 0:
                print("Error: No valid response received from Geocoding API.")
                print("Status code:", r.status_code)
                print("Response text:", r.text)
            
            else:
                print("Reverse geocode data retrieved successfully.")
                print(json_data)

            
                CountryResult = json_data [0].get("country", "Unknown")
                StateResult = json_data [0].get("state", "N/A")
                CityResult = json_data [0].get("name", "N/A")
                StreetResult = "Unavailable"

                CountryResult = CountryResult
            

                if CountryResult =="XZ": 
                    responseMessage = "On {}, the ISS was flying over a body of water at latitude {}* and longitude {}*.".format(timeString, lat, lng)

            
                elif CityResult != "N/A" and StateResult != "N/A":
                    responseMessage = "On {}, the ISS was flying over {}, {} in {}. ({:.4f}*, {:.4f}*)".format(timeString, CityResult, StateResult, CountryResult, float(lat), float(lng))

                elif CityResult != "N/A":
                    responseMessage = "On {}, the ISS was flying over {} in {}. ({:.4f}*, {:.4f}*)".format(timeString, CityResult, CountryResult, float(lat), float(lng))

            
                elif StateResult != "N/A":
                    responseMessage = "On {}, the ISS was flying over {} in {}. ({:.4f}*, {:.4f}*)".format(timeString, StateResult, CountryResult, float(lat), float(lng))

                else: 
                    responseMessage = "On {}, the ISS was flying over {}. ({:.4f}*, {:.4f}*)".format(timeString, CountryResult, float(lat), float(lng))


                print("Sending to Webex:" + responseMessage)


            HTTPHeaders = { "Authorization": "Bearer " + accessToken, "Content-Type": "application/json"}

            PostData = { "roomId": roomIdToGetMessages, "text": responseMessage}


            r = requests.post("https://webexapis.com/v1/messages", data = json.dumps (PostData), headers = HTTPHeaders)

            if r.status_code != 200:
                print("Error: Unable to send message to Webex.")
                print("Status code:", r.status_code)
                print("Response text:", r.text)

            else:
                print("Message successfully sent to Webex room!") 












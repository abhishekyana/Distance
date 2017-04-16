import json, sys, requests
import os

def distances(place1,place2):
    origin_city = place1
    destination_city = place2

    api_key = "AIzaSyDlx_bbdCwiAzIsYHLb4ka5ZwlRN8u1Haw"

    send_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={0}&destinations={1}&key={2}"

    try:
        j = json.loads(requests.get(send_url.format(str(origin_city),str(destination_city),str  (api_key))).text)
        if j["status"] == "OK":
            if j["rows"][0]["elements"][0]["status"] == "OK":
                print(j["rows"][0]["elements"][0]["distance"]["text"]) # + "\n" + j["rows"][0]["elements"][0]["duration"]["text"])
                os.system('say '+'"'+'the distance is '+str(j["rows"][0]["elements"][0]["distance"]["text"])+'"')
            else:
                print("Data not found")
                os.system("say Sorry Couldn't find")
        else:
            print("Error")
    except BaseException as e:
        print("Failed to request: " + str(e))
#distances('visakhapatnam','mumbai')

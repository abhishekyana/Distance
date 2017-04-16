import json, sys, requests
import os

def distances(place1,place2):
    key= "AIzaSyDlx_bbdCwiAzIsYHLb4ka5ZwlRN8u1Haw"

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={0}&destinations={1}&key={2}"

    try:
        j = json.loads(requests.get(url.format(str(place1),str(place2),str(key))).text)
        if j["status"] == "OK":
            if j["rows"][0]["elements"][0]["status"] == "OK":
                print(j["rows"][0]["elements"][0]["distance"]["text"]) + "\n" + j["rows"][0]["elements"][0]["duration"]["text"])
                #os.system('say '+'"'+'the distance is '+str(j["rows"][0]["elements"][0]["distance"]["text"])+'"') still in beta.
            else:
                print("Something Went Wrong")
               # os.system("say Sorry Couldn't find")
        else:
            print("Error")
    except BaseException as e:
        print("Failed the request :" + str(e))
distances('visakhapatnam','mumbai')

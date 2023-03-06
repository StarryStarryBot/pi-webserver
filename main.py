#  TODO LATER
#  https://stackoverflow.com/questions/11604653/how-to-add-command-line-arguments-with-flags-in-python3

## create two runnings modes
# run the server.py
# run locally (with local GUI)

# example command
# python3 main.py --mode gui --server false
# python3 main.py --mode cli --server true

from data.DataHandler import StarData
from pynput.keyboard import Key, Listener
import paho.mqtt.client as mqtt
import time 

calibrated = False
repeatFlag = False
theta = 0
phi = 0

def on_press(key):
    global calibrated
    if key == Key.left:
        client.publish("starryStarry/calibrate", "left")
    elif key == Key.right:
        client.publish("starryStarry/calibrate", "right")
    elif key == Key.enter:
        print("StarryStarryBot calibrated to North!")
        calibrated = True
        return False

def on_release(key):
    if key == Key.left or key == Key.right: 
        client.publish("starryStarry/calibrate", "release")


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    with Listener(
            on_press=on_press, on_release=on_release) as listener:
        listener.join()

    while True: 
        if calibrated == True:  
            # coords = input("Enter coordinates: ")
            mySky = StarData()
            star = mySky.find_star(attribute = "hd", value = "12929")

            sky_coordinates = star.get_sky_coordinates()
            print(f"Location of Star {star.data['hd']}: Altitude: {sky_coordinates.alt.degree:,.3}, Azimuth: {sky_coordinates.az.degree:,.3}")

            coords = f"{abs(sky_coordinates.az.degree):,.3}, {abs(sky_coordinates.alt.degree):,.3}"
            print(coords)
            if coords != '':
                client.publish("starryStarry/coordinates", coords)

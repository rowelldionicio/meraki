#!/usr/bin/env python3

"""
Written by Rowell Dionicio (@rowelldionicio)
Created on: August 20, 2020
This script will print out enabled SSIDs on a specific Meraki network.
The API key is stored in a .env file and is called by the dotenv library.
"""

import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

# Enter the network ID
networkId = "enter-network-id"
url = "https://api.meraki.com/api/v1/networks/{}/wireless/ssids".format(networkId)

# Using dotenv to grab the API key from a .env file
apikey = os.getenv("apikey")

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': apikey
}

response = requests.request("GET", url, headers=headers, data = payload)

ssids = json.loads(response.text)

# Function looping over list of SSIDs and only printing out the enabled SSIDs
def getSSIDs():
    for ssid in ssids:
        if ssid['enabled'] != False:
            print("SSID: {}".format(ssid['name']))

if __name__ == '__main__':
    start_time = time.time()
    print('** Getting enabled SSIDs...\n')
    getSSIDs()

    run_time = time.time() - start_time
    print(f"\n** Time to run: {round(run_time, 2)} sec")

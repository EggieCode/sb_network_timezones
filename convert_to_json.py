#!/usr/bin/python3

import json

timezones = {}
with open("network_timezones.txt") as f:
    line = f.readline().strip()
    while line != "":
        try:
            network, zone = line.rsplit(":",1)
            if network in timezones:
                print ("Duplicute Network: " + network)
            else:
                timezones[network] = zone
            line = f.readline().strip()
        except:
            print ("Error readling: " + line)

with open("network_timezones.json","w") as f:
    f.write(json.dumps(timezones))

from access_points import get_scanner
import os
import json


#Using library n get wireless AP as objects
wifi_scanner = get_scanner()
my_wifi = wifi_scanner.get_access_points()

#Serialize obj to a JSON formatted str
wifi_list = json.dumps(my_wifi,ensure_ascii=True)
with open(os.path.expanduser("~/Desktop/wifi_result.txt"),"r+") as f:
	f.write('{}\n'.format(wifi_list))
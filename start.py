from pulsesensor import Pulsesensor
import time
import requests

p = Pulsesensor()
p.startAsyncBPM()

ip = 'yourIPhere'
address = 'http://' + ip + ':8080/pi'

try:
    while True:
        bpm = p.BPM
        if bpm > 0:
            r = requests.post(address, data = {'heartbeat': bpm})
            print("BPM: %d" % bpm)
        else:
            r = requests.post(address, data = {'heartbeat': 0})
            print("No Heartbeat found")
        time.sleep(1)
except:
    p.stopAsyncBPM()

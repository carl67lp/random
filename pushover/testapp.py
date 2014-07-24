from pushover import Pushover
import requests, json

po_api_token = "aFERV6CYg8UQYjgGm1bMAfU9TurQYf"
po_user_kay = "uYCpaffsy7YGQDTiqPFd88Cu1sRdh9"
wug_api_key = "4a079b9b1c39e4fc"

# Do a weather lookup
wx_url = 'http://api.wunderground.com/api/4a079b9b1c39e4fc/geolookup/conditions/q/MI/Ann_Arbor.json'
raw = requests.get(wx_url)
info = json.loads(raw.text)
location = info['location']['city']
temp_f = info['current_observation']['temp_f']

message = "Temp: %s" % (temp_f)
title = "Wx update for %s" % (location)

po = Pushover(po_api_token)
po.user(po_user_kay)

msg = po.msg(message)
msg.set("title", title)

po.send(msg)
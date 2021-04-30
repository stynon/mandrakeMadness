import request
import time

username = 'TiboKdG'
feed_name = 'mandrakeMadness'
aio_key = 'aio_VXFw92Lxqbs74Y33MApLCS85O7uU'
url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'

def sendDataWifi(data):
    body = {'value': str(data)}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = request.post(url, json=body, headers=headers)
        print(r.text)
        time.sleep(5)
    except Exception as e:
        print(e)

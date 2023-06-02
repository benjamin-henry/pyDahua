# pyDahua

```python
from pyDahua import Api, Camera
from datacls import VideoInModeParams

api = Api()
camera = Camera("admin","password","192.168.1.108")

req = api.init_request(camera)
req = api.VideoInMode.setVideoInModeConfig(req)
req = api.VideoInMode.switchToNight(req)
response = req.send()

print(response.text)
```

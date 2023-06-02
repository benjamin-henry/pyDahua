# pyDahua

```python
from pyDahua import Api, Camera
from datacls import VideoInModeParams

api = Api()
camera = Camera("admin","**4290$$","10.1.1.65")

req = api.init_request(camera)
req = api.VideoInMode.setVideoInModeConfig(req)
req = api.VideoInMode.switchToNight(req)
response = req.send()

print(response.text)
```

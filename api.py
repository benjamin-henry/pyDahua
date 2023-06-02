import requests
from requests.auth import HTTPDigestAuth
from .utils import add_args

from .camera import Camera
from .datacls import AudioEncodeParams, VideoInOptionsParams, VideoInModeParams
from .request import Request

class Api:
    def __init__(self):
        pass

    def init_request(self, cam_instance: Camera):
        req = Request()
        req.cam = cam_instance
        return req
    
    def make_request(self,req:Request):
        response = requests.get(req, auth=HTTPDigestAuth(req.cam.username, req.cam.password))
        return response

    class AudioEncode:
        def __init__(self):
            pass

        def getAudioConfigCaps(req: Request):
            path = "/cgi-bin/encode.cgi?"
            action = "getConfigCaps"
            if req.check(path, action):
                return req

        def getAudioEncodeConfig(req: Request):
            path = "/cgi-bin/configManager.cgi?"
            action = "getConfig"
            if req.check(path, action):
                return req
            
        def setAudioEncodeConfig(req: Request):
            path = "/cgi-bin/configManager.cgi?"
            action = "setConfig"
            if req.check(path, action):
                if req.args is None:
                    req.args = dict({})
            return req
    
        def setBitRate(req:Request, bitrate, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.Audio.bitrate]): str(bitrate)})
            return req
        
        def setCompression(req:Request, compression, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.Audio.compression]): str(compression)})
            return req

        
        def setDepth(req:Request, depth, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.Audio.depth]): str(depth)})
            return req

        
        def setFrequency(req:Request, frequency, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.Audio.frequency]): str(frequency)})
            return req

        
        def setMode(req:Request, mode, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.Audio.mode]): str(mode)})
            return req

        
        def setAudioEnabled(req:Request, enabled, channelNo=0, recordType:AudioEncodeParams.RecordType=None, extraStream:AudioEncodeParams.ExtraStream=None):
            assert recordType is not None or extraStream is not None
            if recordType is not None:
                    req.head = ''.join(['Encode[',str(channelNo),"].MainFormat[",str(recordType),"]."])
            else:
                    req.head = ''.join(['Encode[',str(channelNo),"].Extraformat[",str(extraStream),"]."])
            req.args.update({''.join([req.head, AudioEncodeParams.audio_enabled]): str(enabled).lower()})
            return req

    class VideoInMode:
        def __init__(self):
            pass

        def getVideoInModeConfig(req:Request):
            path = "/cgi-bin/configManager.cgi?"
            action = "getConfig"
            if req.check(path, action):
                if req.args is None:
                    req.args = dict({})
                req.args.update({"name": VideoInModeParams.prefix})
                return req

        def setVideoInModeConfig(req:Request):
            path = "/cgi-bin/configManager.cgi?"
            action = "setConfig"
            if req.check(path, action):
                if req.args is None:
                    req.args = dict({})
                return req

        def switchToDay(req:Request):
            req.args.update({VideoInModeParams.prefix: VideoInModeParams.Day})
            return req

        def switchToNight(req:Request):
            req.args.update({VideoInModeParams.prefix: VideoInModeParams.Night})
            return req

        def Auto(req:Request):
            req.args.update({VideoInModeParams.prefix: VideoInModeParams.Auto})
            return req
            

    class VideoInOptions:
        def __init__(self):
            pass
        
        def getVideoInputCaps(req:Request, channelNo=0):
            path = "/cgi-bin/devVideoInput.cgi?"
            action = "getCaps"
            if req.check(path, action):
                req.args = {"channel": channelNo}
                return req

        def getVideoInOptions(req:Request):
            path = "/cgi-bin/configManager.cgi?"
            action = "getConfig"
            if req.check(path, action):
                req.args = {"name": "VideoInOptions"}
                return req

        def setVideoInOptionsConfig(req:Request):
            path = "/cgi-bin/configManager.cgi?"
            action  = "setConfig"
            if req.check(path=path, action=action):
                req.path = path
                req.action = action
                if req.args is None:
                    req.args = dict({})
            return req

        def setBacklight(req:Request, backlight, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.Backlight]): str(backlight)})
            return req

        def setDayNightColor(req:Request, dayNightColor, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.DayNightColor]): str(dayNightColor)})
            return req

        def setExposureSpeed(req:Request, exposureSpeed, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ExposureSpeed]): str(exposureSpeed)})
            return req

        def setExposureValue1(req:Request, exposureValue1, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ExposureValue1]): str(exposureValue1)})
            return req

        def setExposureValue2(req:Request, exposureValue2, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ExposureValue2]): str(exposureValue2)})
            return req

        def setExternalSync(req:Request, externalSync, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ExternalSync]): str(externalSync)})
            return req

        def setExternalSyncPhase(req:Request, externalSyncPhase, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ExternalSyncPhase]): str(externalSyncPhase)})
            return req

        def setFlashControl_Mode(req:Request, flashControlMode, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.FlashControl.Mode]): str(flashControlMode)})
            return req

        def setFlashControl_Pole(req:Request, flashControlPole, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.FlashControl.Pole]): str(flashControlPole)})
            return req

        def setFlashControl_Value(req:Request, flashControlValue, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.FlashControl.Value]): str(flashControlValue)})
            return req

        def setFlashControl_PreValue(req:Request, flashControlPreValue, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.FlashControl.PreValue]): str(flashControlPreValue)})
            return req

        def setFlip(req:Request, flip, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.Flip]): str(flip)})
            return req

        def setGain(req:Request, gain, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.Gain]): str(gain)})
            return req

        def setGainBlue(req:Request, gainBlue, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.GainBlue]): str(gainBlue)})
            return req

        def setGainRed(req:Request, gainRed, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.GainRed]): str(gainRed)})
            return req

        def setGainGreen(req:Request, gainGreen, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.GainGreen]): str(gainGreen)})
            return req

        def setGainAuto(req:Request, gainAuto, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.GainAuto]): str(gainAuto)})
            return req

        def setIrisAuto(req:Request, irisAuto, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.IrisAuto]): str(irisAuto)})
            return req

        def setMirror(req:Request, mirror, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.Mirror]): str(mirror)})
            return req

        def setWhiteBalance(req:Request, whiteBalance, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.WhiteBalance]): str(whiteBalance)})
            return req

        def setReferenceLevel(req:Request, referenceLevel, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.ReferenceLevel]): str(referenceLevel)})
            return req

        def setRotate90(req:Request, rotate90, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.Rotate90]): str(rotate90)})
            return req

        def setSignalFormat(req:Request, signalFormat, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.SignalFormat]): str(signalFormat)})
            return req

        def setNightOptions_BrightnessThreshold(req:Request, nightOptionsBrightnessThreshold, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.BrightnessThreshold]): str(nightOptionsBrightnessThreshold)})
            return req

        def setNightOptions_IrisAuto(req:Request, nightOptionsIrisAuto, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.IrisAuto]): str(nightOptionsIrisAuto)})
            return req

        def setNightOptions_SunriseHour(req:Request, nightOptionsSunriseHour, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunriseHour]): str(nightOptionsSunriseHour)})
            return req

        def setNightOptions_SunriseMinute(req:Request, nightOptionsSunriseMinute, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunriseMinute]): str(nightOptionsSunriseMinute)})
            return req

        def setNightOptions_SunriseSecond(req:Request, nightOptionsSunriseSecond, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunriseSecond]): str(nightOptionsSunriseSecond)})
            return req

        def setNightOptions_SunsetHour(req:Request, nightOptionsSunsetHour, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunsetHour]): str(nightOptionsSunsetHour)})
            return req

        def setNightOptions_SunsetMinute(req:Request, nightOptionsSunsetMinute, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunsetMinute]): str(nightOptionsSunsetMinute)})
            return req

        def setNightOptions_SunsetSecond(req:Request, nightOptionsSunsetSecond, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SunsetSecond]): str(nightOptionsSunsetSecond)})
            return req

        def setNightOptions_SwitchMode(req:Request, nightOptionsSwitchMode, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.SwitchMode]): str(nightOptionsSwitchMode)})
            return req

        def setNightOptions_ExposureSpeed(req:Request, nightOptionsExposureSpeed, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.ExposureSpeed]): str(nightOptionsExposureSpeed)})
            return req

        def setNightOptions_ExposureValue1(req:Request, nightOptionsExposureValue1, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.ExposureValue1]): str(nightOptionsExposureValue1)})
            return req

        def setNightOptions_ExposureValue2(req:Request, nightOptionsExposureValue2, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.ExposureValue2]): str(nightOptionsExposureValue2)})
            return req

        def setNightOptions_Gain(req:Request, nightOptionsGain, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.Gain]): str(nightOptionsGain)})
            return req

        def setNightOptions_GainAuto(req:Request, nightOptionsGainAuto, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.GainAuto]): str(nightOptionsGainAuto)})
            return req

        def setNightOptions_GainBlue(req:Request, nightOptionsGainBlue, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.GainBlue]): str(nightOptionsGainBlue)})
            return req

        def setNightOptions_GainGreen(req:Request, nightOptionsGainGreen, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.GainGreen]): str(nightOptionsGainGreen)})
            return req

        def setNightOptions_GainRed(req:Request, nightOptionsGainRed, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.GainRed]): str(nightOptionsGainRed)})
            return req

        def setNightOptions_WhiteBalance(req:Request, nightOptionsWhiteBalance, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.WhiteBalance]): str(nightOptionsWhiteBalance)})
            return req

        def setNightOptions_ReferenceLevel(req:Request, nightOptionsReferenceLevel, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.ReferenceLevel]): str(nightOptionsReferenceLevel)})
            return req

        def setNightOptions_ExternalSyncPhase(req:Request, nightOptionsExternalSyncPhase, channelNo=0):
            req.head = ''.join(['VideoInOptions[',str(channelNo),"]."])
            req.args.update({''.join([req.head, VideoInOptionsParams.NightOptions.ExternalSyncPhase]): str(nightOptionsExternalSyncPhase)})
            return req

    class VideoStandard:
        def __init__(self):
            pass

        def getVideoStandardConfig(url):
            return ''.join([url, "/cgi-bin/configManager.cgi?", add_args({
                "action": "getConfig",
                "name": "VideoStandard"   
            })])


        def setVideoStandardConfig(url, video_standard="PAL"):
            assert video_standard == "PAL" or video_standard == "NTSC"
            args = dict({
                "action": "setConfig",
                "VideoStandard": video_standard
            })
            return ''.join([url, "/cgi-bin/configManager.cgi?", add_args(args)])
            


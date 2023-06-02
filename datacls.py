from dataclasses import dataclass

@dataclass
class AudioEncodeParams:
    audio_enabled = "AudioEnable"
    @dataclass
    class Audio:
        bitrate = "Audio.Bitrate"
        compression = "Audio.Compression"
        depth = "Audio.Depth"
        frequency = "Audio.Frequency"
        mode = "Audio.Mode"
    @dataclass
    class RecordType:
        regular = "0"
        motion_detection = "1"
        alarm = "2"
    @dataclass
    class ExtraStream:
        extra_stream_1 = "0"
        extra_stream_2 = "1"
        extra_stream_3 = "2"

@dataclass
class VideoInOptionsParams:
    Day="0"
    AutoSwitch="1"
    Night="2"
    Backlight="Backlight"
    DayNightColor="DayNightColor"
    ExposureSpeed="ExposureSpeed"
    ExposureValue1="ExposureValue1"
    ExposureValue2="ExposureValue2"
    ExternalSync="ExternalSync"
    ExternalSyncPhase="ExternalSyncPhase"
    Flip="Flip"
    Gain="Gain"
    GainBlue="GainBlue"
    GainRed="GainRed"
    GainGreen="GainGreen"
    GainAuto="GainAuto"
    IrisAuto="IrisAuto"
    Mirror="Mirror"
    WhiteBalance="WhiteBalance"
    ReferenceLevel="ReferenceLevel"
    Rotate90="Rotate90"
    SignalFormat="SignalFormat"
    @dataclass
    class FlashControl:
        Mode="FlashControl.Mode"
        Pole="FlashControl.Pole"
        Value="FlashControl.Value"
        PreValue="FlashControl.PreValue"
    @dataclass
    class NightOptions:
        BrightnessThreshold="NightOptions.BrightnessThreshold"
        IrisAuto="NightOptions.IrisAuto"
        SunriseHour="NightOptions.SunriseHour"
        SunriseMinute="NightOptions.SunriseMinute"
        SunriseSecond="NightOptions.SunriseSecond"
        SunsetHour="NightOptions.SunsetHour"
        SunsetMinute="NightOptions.SunsetMinute"
        SunsetSecond="NightOptions.SunsetSecond"
        SwitchMode="NightOptions.SwitchMode"
        ExposureSpeed="NightOptions.ExposureSpeed"
        ExposureValue1="NightOptions.ExposureValue1"
        ExposureValue2="NightOptions.ExposureValue2"
        Gain="NightOptions.Gain"
        GainAuto="NightOptions.GainAuto"
        GainBlue="NightOptions.GainBlue"
        GainGreen="NightOptions.GainGreen"
        GainRed="NightOptions.GainRed"
        WhiteBalance="NightOptions.WhiteBalance"
        ReferenceLevel="NightOptions.ReferenceLevel"
        ExternalSyncPhase="NightOptions.ExternalSyncPhase"

@dataclass
class VideoInModeParams:
    prefix = "VideoInMode[0].Config[0]"
    Day = "0"
    Night = "1"
    Auto = "2"
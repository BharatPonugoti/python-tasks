#Smart Home Devices (Multiple Inheritance)#
class WiFiDevice:
    def wifi(self):
        print("Connected to WiFi")

class VoiceAssistant:
    def voice(self):
        print("Voice control enabled")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    pass

s = SmartSpeaker()
s.wifi()
s.voice()
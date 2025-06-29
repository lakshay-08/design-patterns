# Adaptee
class EuropeanPlug:
    def connect_european(self):
        return "Powering using European plug"

# Target
class USPlugInterface:
    def connect(self):
        pass

# Adapter
class PlugAdapter(USPlugInterface):
    def __init__(self, european_plug):
        self.european_plug = european_plug

    def connect(self):
        return self.european_plug.connect_european()

# Client
def power_device(plug: USPlugInterface):
    print(plug.connect())

european_plug = EuropeanPlug()
adapter = PlugAdapter(european_plug)
power_device(adapter)

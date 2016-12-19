from .devices import BluepyDevice


class BluetoothBaseProvider:

    def get_devices(self):
        raise NotImplemented


class BluepyProvider(BluetoothBaseProvider):

    def __init__(self, hwdev=0, timeout=5):
        self.hwdev = hwdev
        self.timeout = timeout

    def get_devices(self):
        from bluepy.btle import Scanner
        devices = []
        for device in list(Scanner(self.hwdev).scan(self.timeout)):
            devices.append(
                BluepyDevice(device.addr, device.getValueText(9), device)
            )
        return devices

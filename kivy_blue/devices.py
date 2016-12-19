class BaseDevice:

    def __init__(self, addr, name, scanned_entry):
        self.addr = addr
        self.name = name
        self._device = scanned_entry

    def __str__(self):
        str_repr = '{s.addr}'
        if self.name:
            str_repr = "{s.name} ({s.addr})"
        return str_repr.format(s=self)

    def __repr__(self):
        return "<{s.__module__}.{s.__class__.__name__} {name} at {hex}>".format(
            s=self, name=self.__str__(), hex=hex(id(self)))


class BluepyDevice(BaseDevice):

    def __init__(self, addr, name, scanned_entry):
        from bluepy.btle import Peripheral
        super().__init__(addr, name, scanned_entry)
        self.addr_type = self._device.addrType
        self._peripheral = Peripheral()

    def connect(self):
        self._peripheral.connect(self.addr, addrType=self.addr_type)

    def prepare(self):
        self.connect()
        if not self._peripheral.discoveredAllServices:
            self._peripheral.discoverServices()

    @property
    def services(self):
        self.prepare()
        return list(self._peripheral.services)

    def service_by_UUID(self, uuid):
        self.prepare()
        return self._peripheral.getServiceByUUID(uuid)

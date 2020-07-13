class NetworkDevice:
    def __init__(self,mac_no,cache_size):
        self.mac_no = mac_no
        self.cache_size = cache_size
    def transmit(self):
        print("requesting to download")
    def receive(self,data_size):
        if data_size > self.cache_size:
            print("Aborted: Packet size to large")
            return False
        else:
            print("Recieved the Data Packet")
            return True

class Television:
    def __init__(self,screen, volume_tuner):
        self.screen = screen
        self.volume_tuner = volume_tuner
    def display_video(self):
        print("Display on " + self.screen)
    def change_volume(self,amount):
        if amount < 0:
            print("Reducing sound by "+ str(-amount)+ " unit(s).")
        if amount > 0:
            print("Increasing the sound by "+ str(amount)+ " unit(s)")

class InternetTV(Television, NetworkDevice):
    def __init__(self,screen, volume_tuner, mac_no, cache_size, cpu):
        self.cpu = cpu
        NetworkDevice.__init__(self,mac_no,cache_size)
        Television.__init__(self,screen,volume_tuner)
    def watch_network_tv(self,data_size):
        NetworkDevice.transmit(self)
        is_received = NetworkDevice.receive(self,data_size)
        if is_received:
            Television.display_video(self)

a_tv = InternetTV('LED screen', 'digital tuner','789-345',2,'qualcom')
a_tv.watch_network_tv(1)
a_tv.change_volume(-1)
a_tv.watch_network_tv(3)

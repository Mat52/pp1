class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels=[]

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            try:
                print("TV is on, channel ", self.channel_no, self.channels[self.channel_no-1])
            except:
                print("TV is on, channel ", self.channel_no)
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print(self.channels)

tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_channels(['TVP1', 'TVP2','Polsat','TVN','Filmbox', 'Discovery', 'Polsat Sport 1', 'Polsat Sport 2'])
tv1.show_channels()
tv1.show_status()
tv1.set_channel(2)
tv1.show_status()
tv1.set_channel(8)
tv1.show_status()
tv1.set_channel(10)
tv1.show_status()
tv1.turn_off()


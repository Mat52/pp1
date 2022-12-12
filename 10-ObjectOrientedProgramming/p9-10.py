class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print("TV is on, channel ", self.channel_no)
        else:
            print("TV is off")
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.turn_off()
tv1.show_status()
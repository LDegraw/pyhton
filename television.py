



class Television:
    MAX_VOLUME = 2
    MIN_VOLUME = 0
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0
    def __init__(self):
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if(self.power == True):
            self.power = False
        else:
            self.power = True
    def channel_up(self):
        if self.__channel

    def channel_dow(self):
        pass

    def mute(self):
        pass

    def volume_up(self):
        pass
    
    def volume_down(self):
        pass


    def __str__(self) -> str:
        if self.__muted == False:
            return f'Volume = {Television.MAX_VOLUME}'
        else:
            return f'xxx'

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
        self.__status = not(self.__status)

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel  = Television.MAX_CHANNEL

    def mute(self):
        if self.__status:
            self.__muted = not(self.__muted)


    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if(self.__volume > self.MIN_VOLUME):
                self.__volume -= 1
            else:
                self.__volume = self.MIN_VOLUME

    def __str__(self) -> str: 
        temp = self.__volume
        if(self.__muted):
            temp = 0
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {temp}'
        
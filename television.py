
class Television:
    Min_vol = 0
    Max_vol = 2
    Min_Channel = 0
    Max_Channel = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.Min_vol
        self.__channel = Television.Min_Channel

    def power(self):
        self.__status = not self.__status

    def mute(self):
        self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.Max_Channel:
                self.__channel += 1
            else:
                self.__channel = Television.Min_Channel


    def channel_down(self):
        if self.__status:
            if self.__channel > Television.Min_Channel:
                self.__channel -= 1
            else:
                self.__channel = Television.Max_Channel

    def volume_up(self):
        if self.__status:
            if self.__volume < Television.Max_vol:
                self.__volume += 1
            else:
                self.__volume = Television.Max_vol

        if self.__muted:
            self.__muted = not self.__muted

    def volume_down(self):
        if self.__status:
            if self.__volume > Television.Min_vol:
                self.__volume -= 1
            else:
                self.__volume = Television.Min_vol

        if self.__muted:
            self.__muted = not self.__muted

    def __str__(self):
        return f"Power=[{self.__status}], Channel=[{self.__channel}], Volume=[{self.__volume}]"


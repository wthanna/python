
class Television:
    """
    class to simulate a television's basic function
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set values of television object
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        function to revers status
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        function to revers mute
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        function to increase channel by one
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        function to decrease channel by one
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        function to increase volume by one
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

        if self.__muted:
            self.__muted = not self.__muted

    def volume_down(self) -> None:
        """
        function to decrease volume by one
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

        if self.__muted:
            self.__muted = not self.__muted

    def __str__(self) -> str:
        """
        returns a string for the TV's current state
        :return: Power = [status], Channel = [channel], Volume pytest= [__volume]
        """
        if self.__muted:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{Television.MIN_VOLUME}]"
        else:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"


import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv
    
    def test_init(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    
    def test_power(self):
        # power is on
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # power is off
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    
    def test_mute(self):
        # on volume increased and muted
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # unmuted
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # tv is off and muted
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

        # tv is off and unmuted
        self.tv.power()
        self.tv.mute()
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_volume_up(self):
        #off and volume increased
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #on and volume increased
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #on and muted and volume increased
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

        #on and volume at max value
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        #off and volume decreased
        self.tv.power()
        self.tv.volume_up()
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

        #on and muted and volume decreased
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #on and volume decreased
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'


    def test_channel_up(self):
        # tv is off and channel increased
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # tv is on and channel increased
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # tv is on and at max value
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # tv is off and channel decreased
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 3, Volume = 0'

        # tv is on and at min value
        self.tv.power()
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

def test_power(tv):
    tv.power()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
    tv.power()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

def test_mute(tv):
    tv.power()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"

def test_channel_up(tv):
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"

def test_channel_down(tv):
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = [True], Channel = [3], Volume = [0]"

def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"

def test_volume_down(tv):
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"


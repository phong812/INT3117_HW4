import pytest
import Main
def test_01():
    assert Main.Calculate_ticket_price(15, 110, 1000) == -1
def test_02():
    assert Main.Calculate_ticket_price(18, 130, 1000) == 700
def test_03():
    assert Main.Calculate_ticket_price(20, 150, 1000) == 800
def test_04():
    assert Main.Calculate_ticket_price(25, 130, 1000) == 850
def test_05():
    assert Main.Calculate_ticket_price(27, 160, 1000) == 1000

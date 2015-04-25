# -*- coding: utf-8 -*-
from threatbutt import ThreatButt


def test_ioc():
    tb = ThreatButt()
    response = tb.clown_strike_ioc('127.0.0.1')
    assert len(response)


def test_md5():
    tb = ThreatButt()
    response = tb.bespoke_md5('d41d8cd98f00b204e9800998ecf8427e')
    assert len(response)

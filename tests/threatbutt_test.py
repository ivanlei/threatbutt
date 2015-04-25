# -*- coding: utf-8 -*-
from io import StringIO

from mock import patch

from threatbutt import ThreatButt


def test_ioc():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tb = ThreatButt()
        tb.clown_strike_ioc('127.0.0.1')
        assert len(fake_out.getvalue())


def test_md5():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tb = ThreatButt()
        tb.bespoke_md5('d41d8cd98f00b204e9800998ecf8427e')
        assert len(fake_out.getvalue())


def test_ioc_maltego():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tb = ThreatButt(maltegofy=True)
        tb.clown_strike_ioc('127.0.0.1')
        assert len(fake_out.getvalue())


def test_md5_maltego():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tb = ThreatButt(maltegofy=True)
        tb.bespoke_md5('d41d8cd98f00b204e9800998ecf8427e')
        assert len(fake_out.getvalue())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

import requests

from .MaltegoTransform import MaltegoTransform

__version__ = '1.0.7'


class ThreatButt(object):

    """Issues requests to ThreatButt API."""

    def __init__(self, maltegofy=False):
        self._maltegofy = maltegofy

    def clown_strike_ioc(self, ioc):
        """Performs Clown Strike lookup on an IoC.

        Args:
            ioc - An IoC.
        """
        r = requests.get('http://threatbutt.io/api', data='ioc={0}'.format(ioc))
        self._output(r.text)

    def bespoke_md5(self, md5):
        """Performs Bespoke MD5 lookup on an MD5.

        Args:
            md5 - A hash.
        """
        r = requests.post('http://threatbutt.io/api/md5/{0}'.format(md5))
        self._output(r.text)

    def _output(self, text):
        if self._maltegofy:
            xform = MaltegoTransform()
            xform.addEntity('maltego.Phrase', text)
            xform.returnOutput()
        else:
            sys.stdout.write(text)
            sys.stdout.write('\n')


def main():
    """                                   /// WARNING ///
    The ThreatButt API tool embarks on a high speed, turbulent voyage with sudden turns and sharp drops.
    This tool employs safety restraints which may restrict certain guests from using due to their mental shape and size.
    You must posses the ability to remain in an upright position at all times while laying down.
    Persons with the following conditions should not use this tool:
    - Heart Condition or Abnormal Blood Pressure
    - Back, Neck or Similar Physical Condition
    - Expectant Parents
    - Motion Sickness or Dizziness
    - Media Sensitivity to Strobe Effects
    - Claustrophobia
    - Recent Surgery or Other Conditions That May Be Aggravated By This Tool
    """

    parser = ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-i', '--ioc', dest='ioc', default=None,
                        help='[OPTIONAL] An IoC to attribute.')
    parser.add_argument('-m', '--md5', dest='md5', default=None,
                        help='[OPTIONAL] An MD5 hash.')
    parser.add_argument('--maltego', dest='maltego', default=False, action='store_true',
                        help='[OPTIONAL] Run in Maltego compatibility mode.')
    args, _ = parser.parse_known_args()

    tb = ThreatButt(args.maltego)

    if args.ioc:
        tb.clown_strike_ioc(args.ioc)

    elif args.md5:
        tb.bespoke_md5(args.md5)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()

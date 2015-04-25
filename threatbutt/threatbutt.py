#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

import requests

__version__ = '1.0.3'


class ThreatButt(object):

    """Issues requests to ThreatButt API."""

    def clown_strike_ioc(self, ioc):
        """Performs Clown Strike lookup on an IoC.

        Args:
            ioc - An IoC.
        Returns:
            string - Clown Strike IoC Resolution
        """
        r = requests.get('http://threatbutt.io/api', data='ioc={0}'.format(ioc))
        return r.text

    def bespoke_md5(self, md5):
        """Performs Bespoke MD5 lookup on an MD5.

        Args:
            md5 - A hash.
        Returns:
            string - Bespoke MD5 Resolution
        """
        r = requests.post('http://threatbutt.io/api/md5/{0}'.format(md5))
        return r.text


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
    args, _ = parser.parse_known_args()

    tb = ThreatButt()

    if args.ioc:
        attrib = tb.clown_strike_ioc(args.ioc)
        sys.stdout.write(attrib)

    elif args.md5:
        attrib = tb.bespoke_md5(args.md5)
        sys.stdout.write(attrib)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()

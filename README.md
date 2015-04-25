# threatbutt  [![Build Status: master](https://travis-ci.org/ivanlei/threatbutt.svg?branch=master)](https://travis-ci.org/ivanlei/threatbutt)

### Defense in derpth
#### Maximum protection from hacker threats like 4Chan and Reddit.


## Supported APIs
For detailed info on the ThreatButt API see [the docs](http://docs.threatbutt.com).

This package contains an all in one API wrapper for:
* Clown Strike IoC Resolution
* Bespoke MD5 IoC

----

## Install with `pip`
Installation is easy with pip.
```shell
$ pip install threatbutt
```

## ThreatButt Commandline
```shell
$ threatbutt --ioc 127.0.0.1
["China"]
$ threatbutt --md5 d41d8cd98f00b204e9800998ecf8427e
["Really China"]
```

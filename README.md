python-gsmmodem - GSM modem module for Python
=============================================

python-gsmmodem is a module that allows easy control of a GSM modem attached
to the system. It also includes a couple of useful commandline utilities for
interacting with a GSM modem. 

Its features include:
- simple methods for sending SMS messages, checking signal level, etc
- easy-to-use API for starting and responding to USSD sessions and making voice calls
- handling incoming phone calls and received SMS messages via callback methods
- support for SMS PDU and text mode
- wraps AT command errors into Python exceptions by default
- modular design; you easily issue your own AT commands to the modem (with error checking), or read/write directly from/to the modem if you prefer
- comprehensive test suite

Bundled utilities:
- GSMTerm: an easy-to-use serial terminal for communicating with an attached GSM
  modem. It features command completion, built-in help for many AT commands, 
  history, context-aware prompt, etc.
- sendsms.py: a simple command line script to send SMS messages
- identify-modem.py: simple utility to identify attached modem. Can also be used to
  provide debug information used for development of python-gsmmodem. 

Requirements
============

- Python 2.6 or later
- pyserial


How to install this package
===========================

To install, do:

> $ python setup.py install

Note that python-gsmmodem relies on pyserial for 
serial communications: http://pyserial.sourceforge.net


License information
===================

Copyright (C) 2013 Francois Aucamp
See AUTHORS for all authors and contact information. 

License: GNU Lesser General Public License, version 3 or later; see COPYING
         included in this archive for details.
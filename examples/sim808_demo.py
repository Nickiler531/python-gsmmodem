#!/usr/bin/env python

"""\
Demo: handle incoming calls

Simple demo app that listens for incoming calls, displays the caller ID,
optionally answers the call and plays sone DTMF tones (if supported by modem), 
and hangs up the call.
"""

from __future__ import print_function

import time, logging

PORT = '/dev/ttyS1'
BAUDRATE = 115200
PIN = None # SIM card PIN (if any)

from gsmmodem.modem import GsmModem
from gsmmodem.exceptions import InterruptedException
global modem

def handleSms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
    print('Replying to SMS...')
    sms.reply(u'SMS received: "{0}{1}"'.format(sms.text[:20], '...' if len(sms.text) > 20 else ''))
    print('SMS sent.\n')

def handleIncomingCall(call):
    if call.ringCount == 1:
        print('Incoming call from:', call.number)
    elif call.ringCount >= 2:
        if call.dtmfSupport:
            print('Answering call and playing some DTMF tones...')
            call.answer()
            # Wait for a bit - some older modems struggle to send DTMF tone immediately after answering a call
            time.sleep(2) 
            try:
                call.sendDtmfTone('1')
                call.sendDtmfTone('2')
                call.sendDtmfTone('3')
            except InterruptedException as e:
                # Call was ended during playback
                print('DTMF playback interrupted: {0} ({1} Error {2})'.format(e, e.cause.type, e.cause.code))                
            finally:
                if call.answered:
                    print('Hanging up call.')
                    call.hangup()
        else:            
            print('Modem has no DTMF support - hanging up call.')
            call.hangup()
    else:
        print(' Call from {0} is still ringing...'.format(call.number))

def handleIncomingGPS(gps):
    global modem
    location = gps.get_location()
    print(location)
    print(modem.signalStrength)
  
def main():
    global modem
    print('Initializing modem...')
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, incomingCallCallbackFunc=handleIncomingCall, smsReceivedCallbackFunc=handleSms, gpsStatusReportCallbackFunc=handleIncomingGPS)
    modem.connect()
    print('Waiting for incoming calls or SMS messages')
    try:    
        modem.rxThread.join(2**31) # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    finally:
        modem.close()

if __name__ == '__main__':
    main()



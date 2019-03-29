#http://www.klozoff.ms11.net/maxstream/xbee-bootloader-info.txt
import logging

import os, sys
import time
import serial
from xmodem import XMODEM

logging.basicConfig(level=logging.DEBUG)

layout = """
************ XBEE LAYOUT ***********
*
*   This layout represents the XBee S2B module selected
*   for the project with its pin distribution:
*                       _________________
*                      /     ________    \\
*                     /     |   __   |    \\
*                    /      | //  \\\\ |     \\
* RED VCC - XPIN1  -|       | \\\\__// |      |- XPIN20
* YEL RXD - XPIN2  -|       |________|      |- XPIN19
* ORA TXD - XPIN3  -|                       |- XPIN18
*           XPIN4  -| ===================== |- XPIN17
*           XPIN5  -| #   # ####  #### #### |- XPIN16 - RTS GRE
*           XPIN6  -|  # #  #   # #    #    |- XPIN15
*           XPIN7  -|   #   ####  ###  ###  |- XPIN14
*           XPIN8  -|  # #  #   # #    #    |- XPIN13
* GRE DTR - XPIN9  -| #   # ####  #### #### |- XPIN12 - CTS BRO
* BLA GND - XPIN10 -| ===================== |- XPIN11
*                   |_______________________|
*
************ Serial bridge  ***********
  esp_easy set2net
  socat -vvvv pty,link=$HOME/ttyV0 tcp:xbee:2323
"""

def getc(size, timeout=1):
  return s.read(size) or None

def putc(data, timeout=1):
  return s.write(data)  # note that this ignores the timeout

def init_bootloader():
  s.dtr = True
  s.rts = False
  s.break_condition = True
  c = raw_input("Reset device and press ENTER\n")
  s.break_condition = False
  return

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print layout
    print 'Usage:\n\t%s /dev/ttyUSB0 bypass_bootloader_menu.abs.bin\n' % sys.argv[0]
    sys.exit('eeror args')

  s = serial.Serial(port=sys.argv[1],
                      baudrate=115200,
                      bytesize=8,
                      parity='N',
                      stopbits=1,
                      timeout=None,
                      xonxoff=0,
                      rtscts=0
                    )

  init_bootloader()

  time.sleep(1)
  print 'Send F command'
  putc('F')
  time.sleep(1)
  print 'Send file %s' % sys.argv[2]

  modem = XMODEM(getc, putc)

  with open(sys.argv[2], 'rb') as f:
    modem.send(f, quiet=True)


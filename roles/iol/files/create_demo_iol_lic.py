#!/usr/bin/env python3

import os
import socket
import hashlib
import struct

hostid = os.popen('hostid').read().strip()
hostname = socket.gethostname()
ioukey = int(hostid,16)
for x in hostname:
    ioukey = ioukey + ord(x)

iou_pad1 = b'\x4B\x58\x21\x81\x56\x7B\x0D\xF3\x21\x43\x9B\x7E\xAC\x1D\xE6\x8A'
iou_pad2 = b'\x80' + 39*b'\0'
md5_input = iou_pad1 + iou_pad2 + struct.pack('!L', ioukey) + iou_pad1
iou_license = hashlib.md5(md5_input).hexdigest()[:16]

fpath = '/opt/gns3/iourc'
with open(fpath, 'wt') as f:
    f.write('[license]\n')
    f.write(hostname + ' = ' + iou_license + ';\n')

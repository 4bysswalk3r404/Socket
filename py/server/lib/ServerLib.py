import sys
import caps
import os
import random
import encrypt
import zlib

def _ServerTransferSmallData(to, from):
    #_SendDataSmall
    to.send(from.recv(3))
    Charreddatabuffer = from.recv(1)
    to.send(Charreddatabuffer)
    to.send(from.recv(charcoal.uncharcoal(Charreddatabuffer)))

def _ServerTransferData(to, from):
    to.send(from.recv(3))
    charredBBL = from.recv(4)
    charredEBL = from.recv(2)
    to.send(charredBBL)
    to.send(charredEBL)

    basebufferlen = encrypt.uncharcoal(charredBBL)
    endbufferlen = encrypt.uncharcoal(charredEBL)
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    for buffer in buffers:
        to.send(from.recv(buffer))
        from.send(b'\x00')

def ServerTransferString(to, from, fromaddr):
    to.send(b'\x01')
    to.send(from.recv(18))

    _ServerTransferData(to, from)

def ServerTransferFile(to, from, fromaddr):
    to.send(b'\x02')
    to.send(from.recv(18))

    _ServerTransferSmallData(to, from)
    _ServerTransferData(to, from)

#!/usr/bin/env python3 


import asyncio
import ssl
import websockets 

def test_url(url, data=""):
    async def inner():
        # ctx = ssl.create_default_context()
        # ctx.check_hostname = False
        # ctx.verify_mode = ssl.CERT_NONE
        # async with websockets.connect(url, ssl=ctx) as websocket:
        async with websockets.connect(url) as websocket:
            await websocket.send(data)
    return asyncio.get_event_loop().run_until_complete(inner())

test_url("ws://127.0.0.1:8000/")
#!/usr/bin/env python
# client.py

import asyncio
import websockets
import ssl
import pathlib

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_verify_locations(localhost_pem)

async def hello(uri):
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        await websocket.send("ping")
        message = await websocket.recv()
        print(message)

asyncio.run(hello("wss://localhost:9696"))

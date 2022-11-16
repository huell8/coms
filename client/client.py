#!/usr/bin/env python
# client.py

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("ping")
        while True: 
            received = await websocket.recv()
            print(received)

asyncio.run(hello("ws://localhost:9696/"))

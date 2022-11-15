#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("ping")
        message = await websocket.recv()
        print(message)

asyncio.run(hello("ws://localhost:9696"))

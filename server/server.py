#!/usr/bin/env python
# server.py

import asyncio
import websockets

CONNECTIONS = set()

async def loop(websocket):
    global CONNECTIONS
    try:
        CONNECTIONS.add(websocket)
        await websocket.send("connected")
        async for message in websocket:
            websockets.broadcast(CONNECTIONS, message)
            print(message)
    finally:
        CONNECTIONS.remove(websocket)

async def main():
    async with websockets.serve(loop, "localhost", 9696):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

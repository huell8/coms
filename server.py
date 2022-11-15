#!/usr/bin/env python

import asyncio
from websockets import serve

async def echo(websocket):
    async for message in websocket:
        if message == "ping":
            await websocket.send("pong")

async def main():
    async with serve(echo, "localhost", 9696):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python
# server.py

import asyncio
import websockets
import sys

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

async def main(hostname, port):
    async with websockets.serve(loop, hostname, port):
        await asyncio.Future()

if __name__ == "__main__":
    # if usage info was requested using --help or the # of arguments is wrong
    if len(sys.argv) != 3 or sys.argv[1] == '--help':
        print("Usage:\n\tserver.py hostname port")
        exit()
    asyncio.run(main(sys.argv[1], sys.argv[2]))

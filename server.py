#!/usr/bin/env python
# server.py

import asyncio
import websockets
import ssl
import pathlib

async def echo(websocket):
    message = await websocket.recv()
    await websocket.send("pong")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_cert_chain(localhost_pem)

async def main():
    async with websockets.serve(echo, "localhost", 9696, ssl=ssl_context):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

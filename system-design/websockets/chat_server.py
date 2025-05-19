# pip install websockets

import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Broadcast message to all clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, '0.0.0.0', 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

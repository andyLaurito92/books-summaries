import asyncio
import websockets

async def chat():
    uri = "ws://SERVER_IP:6789" 
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("You: ")
            await websocket.send(msg)
            reply = await websocket.recv()
            print(f"Friend: {reply}")

asyncio.run(chat())

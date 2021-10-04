import asyncio
import websockets
from datetime import datetime
from random import random

async def sendMsg(websocket, path):
    while True:
        try:
            msg = "message: {}".format(random())
            await websocket.send(msg)
            print(msg)
        except Exception:
            pass
        finally:
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(sendMsg, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

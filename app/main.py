from loguru import logger
import socketio
import asyncio

from models.field import Field

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './frontend/'
})


@sio.event
async def connect(sid, environ) -> None:
    logger.debug(f'Connected {sid}')
    logger.debug(f'Environ {environ}')


@sio.event
async def disconnect(sid) -> None:
    logger.debug(f'Disconnected {sid}')


@sio.event
async def change_direction(sid, direction) -> None:
    logger.debug(f'Change direction to {direction} for {sid}')

# field = Field(width=20, height=20)
# while True:
#     await sio.emit('drawMap', data=field.get_map())
#     await asyncio.sleep(0.2)

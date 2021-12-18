from loguru import logger
import socketio
import asyncio
from app.field import game_field

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


@sio.event
async def draw_map(sid) -> None:
    while True:
        await sio.emit('draw_map', data=game_field.get_map(), to=sid)
        await asyncio.sleep(0.1)

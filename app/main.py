from loguru import logger
import socketio
import asyncio

from app.const import Direction
from app.field import game_field

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './frontend/'
})


async def start_game():
    while True:
        game_field.next_step()
        await asyncio.sleep(0.2)


@sio.event
async def connect(sid, environ) -> None:
    if not game_field.is_game_started:
        asyncio.create_task(start_game())
    game_field.add_snake(sid)
    game_field.add_mouse()
    logger.debug(f'Connected {sid}')
    logger.debug(f'Environ {environ}')


@sio.event
async def disconnect(sid) -> None:
    logger.debug(f'Disconnected {sid}')


@sio.event
async def change_direction(sid, direction) -> None:
    snake = game_field.get_snake_by_sid(sid)
    snake.direction = Direction(direction)
    logger.debug(f'Change direction to {direction} for {sid}')


@sio.event
async def check_game_state(sid) -> None:
    while True:
        snake = game_field.get_snake_by_sid(sid)
        if snake.is_dead:
            await sio.emit('game_over', data=len(snake.coordinates), to=sid)
            break
        await sio.emit('check_game_state', data=game_field.get_map(), to=sid)
        await asyncio.sleep(0.1)

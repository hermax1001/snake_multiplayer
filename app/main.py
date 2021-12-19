from collections import deque
from datetime import datetime

from loguru import logger
import socketio
import asyncio

from app.const import Direction
from app.field import game_field
from app.models.snake import Snake

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './frontend/'
})


async def start_game():
    while True:
        game_field.next_step()
        await asyncio.sleep(0.175)


@sio.event
async def connect(sid, environ) -> None:
    if not game_field.is_game_started:
        asyncio.create_task(start_game())
        game_field.is_game_started = True

    height = game_field.height
    snake = Snake(
        direction=Direction.UP,
        birth_time=datetime.now(),
        coordinates=deque([(0, height - 1), (0, height - 2), (0, height - 3)]),
        sid=sid
    )
    game_field.add_snake(sid, snake)
    game_field.add_mouse()
    logger.debug(f'Connected {sid}')
    logger.debug(f'Environ {environ}')


@sio.event
async def disconnect(sid) -> None:
    logger.debug(f'Disconnected {sid}')


@sio.event
async def restart(sid) -> None:
    height = game_field.height
    snake = game_field.get_snake_by_sid(sid)
    snake.is_dead = False
    snake.direction = Direction.UP
    snake.birth_time = datetime.now()
    snake.coordinates = deque([(0, height - 1), (0, height - 2), (0, height - 3)])
    game_field.add_snake(sid, snake)


@sio.event
async def change_direction(sid, direction) -> None:
    snake = game_field.get_snake_by_sid(sid)
    if snake:
        snake.direction = Direction(direction)
        logger.debug(f'Change direction to {direction} for {sid}')


@sio.event
async def check_game_state(sid) -> None:
    while True:
        logger.debug(f'CHECK STATE for {sid}')
        snake = game_field.get_snake_by_sid(sid)
        if snake.is_dead:
            await sio.emit('game_over', data=len(snake.coordinates), to=sid)
            break
        await sio.emit('check_game_state', data=game_field.get_map(), to=sid)
        await asyncio.sleep(0.175)

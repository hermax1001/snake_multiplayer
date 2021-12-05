const socket = io();

socket.on("connect", () => {
    console.log("connected")
});

socket.on("disconnect", () => {
    console.log("disconnected")
});

socket.on("draw_map", (field) => {
    for (let arr of field) {
        for (let point of arr) {

        }
    }
});

document.addEventListener('keydown', (event) => {
    let direction_map = {
        'ArrowUp': 'UP',
        'ArrowDown': 'DOWN',
        'ArrowRight': 'RIGHT',
        'ArrowLeft': 'LEFT'
    };

    let direction = direction_map[event.key];

    if (!!direction) {
        socket.emit('change_direction', direction);
    }
});

socket.emit('draw_map');

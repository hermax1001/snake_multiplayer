const socket = io();

socket.on("connect", () => {
    console.log("connected")
});

socket.on("disconnect", () => {
    console.log("disconnected")
});

socket.on("game_over", () => {
    alert('Game Over!!!')
});

socket.on("draw_map", (mainMap) => {
    let old_map = document.getElementById("mainMap");
    if (!!old_map) {
        old_map.remove()
    }

    let table = document.createElement('table');
    table.setAttribute("id", "mainMap");
    table.style.border = "thick solid #0000FF";

    for (let arr of mainMap) {
        let tr = document.createElement('tr');
        for (let point of arr) {
            let td = document.createElement('td');
            if (point === 1) {
                td.style.border = "thick solid #000000";
            }
            else if (point === -1) {
                td.style.border = "thick solid #0000FF"
            }
            else if (point === 2) {
                td.style.border = "thick solid #FF0000"
            }
            else {
                td.style.border = "thick solid #FFFFFF";
            }
            // td.appendChild(document.createTextNode(point))
            tr.appendChild(td)
        }
        table.appendChild(tr)
    }
    document.body.appendChild(table);
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

socket.emit('check_game_state');

const socket = io();

socket.on("connect", () => {
    console.log("connected")
});

socket.on("disconnect", () => {
    console.log("disconnected")
});

socket.on("draw_map", (mainMap) => {
    let old_map = document.getElementById("mainMap");
    if (!!old_map) {
        old_map.remove()
    }

    let table = document.createElement('table');
    table.setAttribute("id", "mainMap");

    for (let arr of mainMap) {
        let tr = document.createElement('tr');
        for (let point of arr) {
            let td = document.createElement('td');
            td.appendChild(document.createTextNode(point))
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

socket.emit('draw_map');

const socket = io();

socket.on("connect", () => {
    console.log("connected")
});

socket.on("disconnect", () => {
    console.log("disconnected")
});

socket.on("game_over", (length) => {
    if (confirm(`Game Over! Do  you want to play again?`)) {
        socket.emit('restart');
        socket.emit('check_game_state');
    } else {
        window.close();
    }
});

socket.on("check_game_state", (data) => {

    let old_map = document.getElementById("mainMap");
    if (!!old_map) {
        old_map.remove()
    }

    let table = document.createElement('table');
    table.setAttribute("id", "mainMap");
    // table.style.border = "thick solid black";
    table.style.marginLeft = "auto";
    table.style.marginRight = "auto";


    for (let arr of data['main_map']) {
        let tr = document.createElement('tr');
        for (let point of arr) {
            let td = document.createElement('td');
            td.style.width = '5px'
            td.style.height = '5px'
            td.style.borderRadius = '7px'
            if (point === 1) {
                td.className = "snake"
            } else if (point === -1) {
                td.className = "snake"
                td.style.backgroundColor = "#41403E";
            } else if (point >= 10) {
                td.style.border = "solid #FFFFFF"
                if (point === 10) {
                    td.style.backgroundColor = "#339966";
                } else if (point === 11) {
                    td.style.backgroundColor = "#DC143C";
                } else if (point === 12) {
                    td.style.backgroundColor = "#4169E1";
                } else if (point === 13) {
                    td.style.backgroundColor = "#FFD700";
                } else if (point === 14) {
                    td.style.backgroundColor = "#8B4513";
                } else if (point === 15) {
                    td.style.backgroundColor = "#696969";
                }

            } else {
                td.style.border = "thick solid #FFFFFF";
            }
            // td.appendChild(document.createTextNode(point))
            tr.appendChild(td)
        }
        table.appendChild(tr)
    }
    let oldLengthCounter = document.getElementById("lengthCounter");
    if (!!oldLengthCounter) {
        oldLengthCounter.remove()
    }
    let lengthCounter = document.createElement("p");
    lengthCounter.setAttribute("id", "lengthCounter");
    lengthCounter.appendChild(
        document.createTextNode(`Your length: ${data['length']}. Best on map ${data['max_length']}`)
    )
    document.body.appendChild(table);
    document.body.appendChild(lengthCounter);


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


const date = d.toLocaleString('en-gb',
    {
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hourCycle: "h24"
    }
);

let divDate2 = document.getElementById("date");

document.getElementById("date").innerText = date;
divDate2.innerText = date;

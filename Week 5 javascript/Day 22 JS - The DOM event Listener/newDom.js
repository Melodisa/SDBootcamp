//Gathering the paragraphs
let p1 = document.getElementById('p1');
let p2 = document.getElementById('p2');
let p3 = document.getElementById('p3');
let p4 = document.getElementById('p4');
let p5 = document.getElementById('p5');
let p3Btn = document.getElementById('p3Btn');

//Creating the Event and Event Listener
//        (event type, function)
p1.addEventListener('mouseover', function run(){
    p1.style.backgroundColor = "orange"
}) 

p1.addEventListener('mouseleave', function run(){
    p1.style.backgroundColor = ""
}) 


// Create event that changes the second paragraph on click
p2.addEventListener('click', function run(){
    p2.style.backgroundColor = "yellow"
}) 


// Create event that reverts the second paragraph on mouseout

p2.addEventListener('mouseout', function run(){
    p2.style.backgroundColor = "white"
}) 

// p3
p3.style.color = "blue"

p3Btn.addEventListener('click', function run(){
    if (p3.style.display != 'block'){
        p3.style.display = "block"
        console.log("p3 showing")
        p4.style.display = "none"
    }
    else{
        p3.style.display = "none"
        console.log("p3 hidden")
        p4.style.display = "block"
    }
})
//p4
p4.style.color = "crimson"

function changeOrange(){
    if (p5.style.color != "orange"){
     p5.style.color = "orange"   
    }
    else{
     p5.style.color = "black"   
    }
}






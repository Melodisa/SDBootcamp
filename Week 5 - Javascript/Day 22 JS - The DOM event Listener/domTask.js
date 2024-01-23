//Task 1
let food = document.getElementById("food")
let drink = document.getElementById("drink")
let btn = document.getElementById("btn")

btn.addEventListener("click", function run(){
    if (food.style.display == "block"){
        food.style.display = "none"
        drink.style.display = "block"
        btn.innerText = "Food Menu"
    }
    else{
        food.style.display = "block"
        drink.style.display = "none"
        btn.innerText = "Drink Menu"
    }
})

//Task 2
let links = document.querySelectorAll("nav a"); // creates an array

for (let i = 0; i<links.length; i++){
   
    links[i].addEventListener("mouseover", function run(){
        links[i].style.backgroundColor = "pink"
        links[i].style.fontFamily = "Impact"
    })
}

for (let i = 0; i<links.length; i++){
    links[i].addEventListener("mouseout", function run(){
        links[i].style.backgroundColor = "white"
        links[i].style.fontFamily = "arial"
    })
}
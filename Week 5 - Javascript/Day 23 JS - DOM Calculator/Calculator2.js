// Basic Calculator - 
//an example to how we can link functions to HTML elements and get user input values

// sumUp will take 2 values and add them together
function add(valueOne, valueTwo) {

    return Number(valueOne) + Number(valueTwo);
};

// define some basic variables we need for the calculate function
//const operator = ?  operation
const numberOne = document.getElementById('numberone') //INPUT 1
const numberTwo = document.getElementById('numbertwo') //INPUT 2
const result = document.getElementById('result') //Output



function calculate() {

    let sum = sumUp(numberOne.value, numberTwo.value); //

    result.value = sum.toString();
};





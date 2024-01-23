
/*
!Tasks:
1: Write a function that takes in a first name and a surname as arguments and returns a message greeting them.
2: Write a function that takes in a string as an argument and sorts the string into alphabetical order and returns the result.
3: Write a cash machine / atm function that takes in a withdrawal amount and a pin number as an argument and compares the pin and withdrawal amount against a stored pin and account balance. If the pin matches and the balance is sufficient approve the transaction, if not decline the transaction.
*/

let subject = "JavaScript";
//Declaring a function
function greeting() {
    console.log("Hello World!");
}

//Call or Invoke a function
greeting();

//User login // Log out function
let userOnline = true;
function userStatus() {
    if (userOnline == true) {
        console.log("User Signed In!")
        console.log(userOnline);
    }
    else {
        console.log("User Signed Out!")
        console.log(userOnline);
    }
}
userStatus();

// Function with parameters // Arguments

// Parameters are defined when we declare the function. Data that is expected.

// Arguments are the data we pass to the function when we call it

function atm(accountNumber, amount) {
    console.log(`Account Number: ${accountNumber}. Amount: ${amount}`);
}

atm(343847345, 300);
atm(1234567, 500);
function sum(num1, num2) {
    return num1 + num2;
}
console.log(sum(20, 10));
console.log(sum(50, 50));

//Create a function which will Hello 'PersonName',How are you, tha you pass as argument.

console.clear();
//! Scope in JavaScript
//block scope
//let, const
//local scope
//var, let, const
//global scope
// if you declare a variable outside a function, it has global scope
//let name="Matt";
{
    const name = "John";
}

//var keyword doesn't have block scope
console.log(`Hello ${name}`);//Hello Matt
function scope() {
    console.log(subject);
}
scope();

// Functions that call another function
function double(num1) {
    return num1 * 2;
}
function quadruple(num2) {
    return double(num2) * 2;
}
console.log(quadruple(20));

// Function Can be hoisted - Called before they are declared
//Arrow Function
//omit the return statement// explicit return
//omit the function keyword
//when there is only 1 parameter, brackets is optional
let add2 = num => num * 2;
console.log(add2(10));


let multiply = (x, y) => x * y;
console.log(multiply(7, 7));



function multiplication(number) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${i} * ${number} = ${i * number}`);
    }
}
multiplication(5);




// document.getElementById('heading').innerHTML="First Day";

// single line comment
/*
Multi line
Comment
*/

console.log("Welcome to JavaScript");
console.log(10/5);
console.warn("Warning");
console.error("Error message");
alert("Do you want to continue");
console.clear();
/*
1. Display 'Welcome to JavaScript' message in the cosole of browser.
2. display the above message as error and warning.
3. clear the console
    Note: Use external JavaScript
*/
console.log("Welcome to JavaScript");
console.error("Welcome to JavaScript");
console.warn("Welcome to JavaScript");
console.clear();

let num1; //declaration
num1=30; //initialization
console.log(num1);
//
console.clear();
let num2=50;
console.log(num2);
console.clear();
//ways of creating variable in JS
//four ways to create a variable in JS
//!Ways to declare a variable
var number1=10;
{
    var number1=30;
}

console.log(number1)//30
//var was old way of declaring variable not recommended
// use let in such cases
const number=20;
const value=50;
//const variable value can not be changed

//! ***  TASK ***

 /*
 1. I would like you to Create a variable called fastFood and assign the value Pizza,
    another variable called favColor with the value Red and a third 
    variable called favDrink with the value lemonade.

 2. Console log the favDrink variable to show it's value.

 3. Change the value of the fastFood variable to "Pasta", console log it's value.

 4. Create a variable, call it whatever you want and assign the value of your brithday.
 */
let fastFood="Pizza";
let favColor="Red";
let favDrink="Lemonade";

//2.
console.log(favDrink);

//3.
fastFood="Pasta";
console.log(fastFood);

//4.
const dateOfBirth="01/01/1995";
console.log(dateOfBirth);

let a=30;
let A=50;
console.log(a);


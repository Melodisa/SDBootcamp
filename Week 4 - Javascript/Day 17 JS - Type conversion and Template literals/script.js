let num1=100; // this is number value //
let name="Zak"; //string
//typeof - is a property which return data type of a value or a variable
console.log(typeof num1);
console.log(typeof name);
console.log(typeof 50);


// boolean has two values = true, false
//They can be used to compare a condition and perform an action depending on the outcome whether it's true or fales. 
let education=true;
console.log(typeof education);
let a=10;
console.log(a==10);

/*
!important 
Null -- is used to decalare a value as empty.
!it is different than undefined.
undefine is a variable which is not defined a values.
Null -- is a variable which is defined Null value.
*/
let b;
console.log(typeof b);
let c=null;

console.log(typeof c);
let e=958.609;
console.log(typeof e);
let bigInt=981983542n;
console.log(typeof bigInt);

// search on type conversion in JS for 5 minutes
console.clear();
//String:
//Syntax = String(ValueToConvert)*/
let f=3;
console.log(typeof String(f))//"3"
let g=String(100);
console.log(typeof g)//"100"

let h=String(true);
console.log(typeof h);
console.log(h)
//why to do type conversion
// any user input will be in string type
//!convert to Number
//Syntax= Number(ValueToConvert)
let i="Zak";//
console.log(Number)//NaN
let myName="100";
console.log(Number(myName));//100
//true=1, false=0;
console.log(Number(false));//0
console.log(Number(true));
console.log(Number("1"));
console.clear();
// Boolean:
// Syntax = Boolean(ValueToConvert)
console.log(Boolean(0));//false
console.log(Boolean(1));//true
console.log(Boolean("JavaScript"))//true
console.log(Boolean(""))//false
console.log(Boolean(" "))//true
console.log(Number(String(Number(true))));//1


let number=100; //true
let zeroNumber=0; //false
// boolean => true or false

//!   Coercion
//Automatic type conversion is happening


// TRY THESE IN YOUR JS FILE: */

console.log('12' / 2); //6
console.log(2 * '2');  //4
console.log('10' / 2); //5
console.log(true * 7); //7
console.log(true+3);





/*
after the string all the + will act as concatenation

*/

//TRY THESE IN YOUR JS FILE:
console.log('1' + 2+2); //122
console.log('1' + 2 + true);//12true
console.log('12' + undefined);//12undefined
console.log('12' + null); //12null
console.log(2 +'1'); //21
console.log(2 + true); //3
//String in Java Script
let firstMessage="Welcome to JavaScript";
let secondMessage='Welcome to its JavaScript';
let thirdMessage=`Welcome to JavaScript`
let firstName="Zak";

console.log(`Hello ${firstName} how are `);

console.log("Hello,", firstName, " How are you?")

console.log(4/false);
4/0

/*
Syntax:

if(condition){task to do}
else if(condition){task to do}
else if(condition){task to do}
else{task to do}

*/
let weather="Sunny";

if(weather=="Raining")
{
    console.log("Take umbrella, it's raining!");
}
else if(weather=="Sunny")
{
    console.log("It's sunny, take your sun glasses!");
}
else
{
    console.log("The weather would be foggy or cloudy, wear a jacket");
}

/* //!OPERATOR
+   addition
-   subtraction
/   devision
*   multiply
%   moduler
++  increment
--  decrement
=       assignment
==      equal too -> comparison
===     ->equal value and equal data type.
! in === both the data type and value should be equal
! in == only the value should be equal
> greater
< less than
>= greater or equal
<= less than equal
!Logical Operators
&& ----- and
|| ----- or

*/
let a="10";
console.log(a===10);//false
// + 

let trafficLight="Amber";
if(trafficLight=="Red")
{
    console.log("Stop behind the line, the light is red");
}
else if(trafficLight=="Amber")
{
    console.log("Stop behind the line")
}
else if(trafficLight="brown")
{}

else{
    console.log("The light could be green, You can cross!")
}



/*
I would like you all to write a code to check a if a person is eligible for voting or not.
if the person age is under 18, log a message that he/she can't vote, otherwise they can vote

*/
let age=30;
if(age>=18)
{
    console.log("You are eligible for voting!");
}
else{
    console.log("Sorry, You can't vote!")
}

// Switch Statement
// Usefull when you have one condtion being checked against multiple cases

let day="Monday"
switch(day){
    case "Monday":
        console.log(`Happy Monday!`);
        break;
    case "Tuesday":
        console.log("Second day of the week!");
        break;
    case "Wednesday":
        console.log("Midway through the week!");
        break;
    case "Thursday":
        console.log(`It's almost Friday!`);
        break;
    case "Friday":
        console.log("Happy Friday!");
        break;
    case "Saturday":
    case "Sunday":
        console.log("It's the weekend!");
        break;
    default:
        console.log("Day not recognized, try again!")
}
// Switch Statement 2 - Grading Example
let testScore=70;
switch(true)
{
case testScore>=75:
    console.log(`Distinction`);
    break;
case testScore>=60:
    console.log(`Merit`);
    break;
case testScore>=50:
    console.log(`Pass`);
    break;
default:
    console.log(`Fail`);
}


let customerAge=17;
if(customerAge>=18)
{
    console.log("Which drink would you like?")
}
else{
    console.log("You are too young!")
}
let password="safewk";
if(password.length<8)
{
    console.log("Your password is short!");
}
else{
    console.log(password)
}

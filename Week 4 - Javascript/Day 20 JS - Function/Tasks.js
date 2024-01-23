Function Greeting(personName) {
    console.log("Hiyaaa ${personName} how are ya?");
}
Greeting("Mel");

Function Greeting(personName) {
    console.log("Hiyaaa ${personName} how are ya?");
}
Greeting("Mel");


function greeting(firstName, lastName) {
    console.log(`Hello ${firstName} ${lastName}`)
}
greeting("Mel", "Isa")


// last task code

let accBal = 100
let myPin = 1111
const withdraw = (withdrawAmount, pinNum) => {
    if (accBal >= withdrawAmount && withdrawAmount <= 250 && pinNum === myPin) {
        console.log(`Transaction Approved. Please collect your £${withdrawAmount}.00.`)
        console.log(`Remaining Amount: ${accBal - withdrawAmount}`)
    } else if (accBal >= withdrawAmount && pinNum !== myPin) {
        console.log(`Transaction Denied. Incorrect Pin Number.`)
    }
    else if (withdrawAmount > 250) {
        console.log(`Transaction Denied. You can't take more than £250.`)
    }
    else {
        console.log("Transaction Denied. Insufficient Funds.")
    }
}

withdraw(150, 1111)
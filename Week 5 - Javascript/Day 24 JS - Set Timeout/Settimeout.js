function hiya() {
    console.log('Hiya!')

}

hiya();
setTimeout(hiya, 10000);


function greet(name) {
    console.log('Good morning', name)

}

greet('Mel', 'see you');
let timeOutID = setTimeout(greet, 5000, 'bye')

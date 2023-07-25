// go to local storage, try to get counter, will run if there is no counter
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    // get counter item from local storage
    let counter = localStorage.getItem('counter');

    counter++;
    document.querySelector('h1').innerHTML = counter;   // sets 'h1' content to counter variable

    // set local storage counter to be current counter
    localStorage.setItem('counter',counter);
}

// whole page event listener
// 1st argument is the event listener; looks for when all the page content is loaded
// 2nd argument is what function to be executed; executes function() (doesn't need name since it's in the actual event listener)
document.addEventListener('DOMContentLoaded', function() {

    // set inital value of counter to actual counter upon page load
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    
    // event listener for button
    document.querySelector('button').onclick = count;

    // can be alternatively written as:
    // document.querySelector('button').addEventListener('click', count);

    // calls count function every second: setInterval(count, 1000);
})
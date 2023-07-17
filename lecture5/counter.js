// initalize counter, increments on click and displays alert to user
let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;   // sets 'h1' content to counter variable

    // checks if counter is divisble by 10
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`); // ` and $ allows you to place variable in the string
    }
}

// whole page event listener
// 1st argument is the event listener; looks for when all the page content is loaded
// 2nd argument is what function to be executed; executes function() (doesn't need name since it's in the actual event listener)
document.addEventListener('DOMContentLoaded', function() {
    
    // event listener for button
    document.querySelector('button').onclick = count;

    // can be alternatively written as:
    // document.querySelector('button').addEventListener('click', count);
})
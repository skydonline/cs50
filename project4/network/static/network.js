// get username and ID
let currentUsername;
let currentUserID;
function getUserInfo() {
    currentUser = document.querySelector('#current-user');
    currentUsername = currentUser.dataset.user;
    currentUserID = parseInt(currentUser.dataset.id, 10);
    console.log(`Current User: ${currentUsername}`);
    console.log(`Current UserID: ${currentUserID}`);
}

// Change likes icon and amount
function changeLikes(container) {
    const likeIcon = container.querySelector('.like-icon');
    const postID = container.dataset.postid;
    const likeCount = container.querySelector('.amount-of-likes');
    const likeAmount = parseInt(likeCount.innerHTML, 10);

    // Gets likes on post
    fetch(`/api/likes/${postID}`)
    .then(response => response.json())
    .then(data => {
        const users = data.usersid;

        // If they have already liked it, unlike it
        if (users.includes(currentUserID)) {
            likeIcon.innerHTML = '🤍';
            likeIcon.style.animation = 'growAndShrink 1s';
            likeCount.innerHTML = `${likeAmount - 1}`;

            fetch(`/api/likes/${postID}`, {
                method: 'PUT',
                body: JSON.stringify({
                    user: currentUserID,
                    action: 'remove'
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            });

        // If they haven't liked it, like it
        } else if (!users.includes(currentUserID)) {
            likeIcon.innerHTML = '❤️';
            likeIcon.style.animation = 'growAndShrink 1s';
            likeCount.innerHTML = `${likeAmount + 1}`;
            fetch(`/api/likes/${postID}`, {
                method: 'PUT',
                body: JSON.stringify({
                    user: currentUserID,
                    action: 'add'
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            });
        }
        
    })
};

let layoutFirstVisit = true;
// Changes dark mode preference
function darkMode() {
    const darkModeToggle = document.querySelector('#dark-mode-toggle');
    const darkModePref = darkModeToggle.dataset.darkmode;
    const noColorChange = document.querySelectorAll('.no-color-change');

    // Don't change dark mode preference on first visit
    if (layoutFirstVisit) {
        layoutFirstVisit = false;

        if (darkModePref == 'True') {
            darkModeToggle.src = 'https://cdn3.iconfinder.com/data/icons/meteocons/512/moon-symbol-512.png';
        } else if (darkModePref == 'False') {
            noColorChange.forEach(element => {
                element.style.filter = 'invert(1)';
            })
            document.body.classList.toggle('light-mode');
            darkModeToggle.src = 'https://cdn4.iconfinder.com/data/icons/biticon-weather-line/24/weather_sun_sunny_day-512.png';
        }
        return
    }

    const body = document.body;
    body.classList.toggle('light-mode');

    if (darkModePref == 'True') {
        // Turn from true to false
        darkModeToggle.setAttribute('data-darkmode', 'False');
        darkModeToggle.src = 'https://cdn4.iconfinder.com/data/icons/biticon-weather-line/24/weather_sun_sunny_day-512.png';

        noColorChange.forEach(element => {
            element.style.filter = 'invert(1)';
        })
    } else {
        // Turn from false to true
        darkModeToggle.setAttribute('data-darkmode', 'True');
        darkModeToggle.src = 'https://cdn3.iconfinder.com/data/icons/meteocons/512/moon-symbol-512.png';

        noColorChange.forEach(element => {
            element.style.filter = 'invert(0)';
        })
    }

    fetch(`/api/darkmode/${currentUserID}`, {
        method: 'PUT',
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    });
};

document.addEventListener('DOMContentLoaded', function() { 
    getUserInfo();
    setTimeout(darkMode,20);
});


function delay() {
    console.log("Delay.");
}
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


document.addEventListener('DOMContentLoaded', function() { 
    getUserInfo();
});


// Get username and ID
let currentUsername;
let currentUserID;
function getUserInfo() {
    currentUser = document.querySelector("#current-user");
    currentUsername = currentUser.dataset.user;
    currentUserID = parseInt(currentUser.dataset.id, 10);
    console.log(`Current User: ${currentUsername}`);
    console.log(`Current UserID: ${currentUserID}`);
}

// Change likes icon and amount
function changeLikes(container) {
    const likeIcon = container.querySelector(".like-icon");
    const postID = container.dataset.postid;
    const likeCount = container.querySelector(".amount_of_likes");
    const likeAmount = parseInt(likeCount.innerHTML, 10);

    // Gets likes on post
    fetch(`/api/likes/${postID}`)
        .then((response) => response.json())
        .then((data) => {
            const users = data.usersid;

            // If they have already liked it, unlike it
            if (users.includes(currentUserID)) {
                likeIcon.src =
                    "https://pixlok.com/wp-content/uploads/2021/12/Instagram-Like-Icon-83nfc3.png";
                likeCount.innerHTML = `${likeAmount - 1}`;

                fetch(`/api/likes/${postID}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        user: currentUserID,
                        action: "remove",
                    }),
                })
                    .then((response) => response.json())
                    .then((result) => {
                        console.log(result);
                    });

                // If they haven't liked it, like it
            } else if (!users.includes(currentUserID)) {
                likeIcon.src =
                    "https://www.nicepng.com/png/full/778-7786050_download-instagram-like-icon-png.png";
                likeIcon.classList.add("liked");
                setTimeout(() => {
                    likeIcon.classList.remove("liked");
                }, 300);
                likeCount.innerHTML = `${likeAmount + 1}`;

                fetch(`/api/likes/${postID}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        user: currentUserID,
                        action: "add",
                    }),
                })
                    .then((response) => response.json())
                    .then((result) => {
                        console.log(result);
                    });
            }
        });
}

// Changes dark mode preference
let layoutFirstVisit = true;
function darkMode() {
    const darkModeToggle = document.querySelector("#dark-mode-toggle");
    const darkModePref = darkModeToggle.dataset.darkmode;

    // Don't change dark mode preference on first visit
    if (layoutFirstVisit) {
        layoutFirstVisit = false;

        if (darkModePref == "True") {
            darkModeToggle.src =
                "https://cdn3.iconfinder.com/data/icons/meteocons/512/moon-symbol-512.png";
            document.body.classList.remove("light-mode");
            document.body.classList.toggle("dark-mode");
        } else if (darkModePref == "False") {
            document.body.classList.toggle("light-mode");
            document.body.classList.remove("dark-mode");
            darkModeToggle.src =
                "https://cdn4.iconfinder.com/data/icons/biticon-weather-line/24/weather_sun_sunny_day-512.png";
        }
        return;
    }

    // Add/remove light mode class
    const body = document.body;
    body.classList.toggle("light-mode");

    // Turn from true to false, change icon and theme
    if (darkModePref == "True") {
        darkModeToggle.setAttribute("data-darkmode", "False");
        darkModeToggle.src =
            "https://cdn4.iconfinder.com/data/icons/biticon-weather-line/24/weather_sun_sunny_day-512.png";
    } else {
        // Turn from false to true, change icon and theme
        darkModeToggle.setAttribute("data-darkmode", "True");
        darkModeToggle.src =
            "https://cdn3.iconfinder.com/data/icons/meteocons/512/moon-symbol-512.png";
    }

    // Update darkmode preference in database
    fetch(`/api/darkmode/${currentUserID}`, {
        method: "PUT",
    })
        .then((response) => response.json())
        .then((result) => {
            console.log(result);
        });
}

// Comments prompt
function postComments(container) {
    // Show comment prompt
    const commentPrompt = document.querySelector("#commentPrompt");
    commentPrompt.style.display = "block";

    // Get postID, add it to the comment section prompt
    const commentSection = document.querySelector("#commentSection");
    const postID = container.dataset.postid;
    commentSection.dataset.postid = postID;

    // Fetch comments for that post
    fetch(`/api/comments/${postID}`)
        .then((response) => response.json())
        .then((data) => {
            const comments = data.comments;

            // Cycle through each comment, add to container
            comments.forEach((comment) => {
                const indComment = document.createElement("div");
                indComment.className = "indComment";
                indComment.dataset.userid = comment.user;
                indComment.innerHTML = `
                <p class="comment_info">${comment.username}: ${comment.content}</p>
                <p class="comment_date">${comment.date}</p>
                `;

                commentSection.appendChild(indComment);
            });
        });
}

// Exit comment prompt
function exitComments() {
    // Hide comment prompt
    const commentPrompt = document.querySelector("#commentPrompt");
    commentPrompt.style.display = "none";

    // Clear all posts in comment prompt
    const indPosts = document.querySelectorAll(".indComment");
    indPosts.forEach((post) => post.remove());
}

// Add comment to post
function addComment(container) {
    // Get postID and the user's comment
    const postID = container.dataset.postid;
    const commentContent = container.querySelector("#add_comment_text").value;

    // Update the comment in the database
    fetch(`/api/comments/${postID}`, {
        method: "POST",
        body: JSON.stringify({
            user: currentUserID,
            post: postID,
            content: commentContent,
        }),
    })
        .then((response) => response.json())
        .then((result) => {
            console.log(result);

            // Clear comment input field
            const commentInput = document.querySelector("#add_comment_text");
            commentInput.value = "";
            const commentSection = document.querySelector("#commentSection");

            // Get date
            const date = new Date();
            let currentDay = String(date.getDate()).padStart(2, "0");
            let currentMonth = String(date.getMonth() + 1).padStart(2, "0");
            let currentYear = date.getFullYear();
            let currentDate = `${currentYear}-${currentMonth}-${currentDay}`;

            // Add comment to the prompt, appears to be responsive for user
            const indComment = document.createElement("div");
            indComment.className = "indComment";
            indComment.dataset.userid = currentUserID;
            indComment.innerHTML = `
                <p class="comment_info">${currentUsername}: ${commentContent}</p>
                <p class="comment_date">${currentDate}</p>`;

            commentSection.appendChild(indComment);
        });
}

// Inital loading of dark mode preference and get current user info
document.addEventListener("DOMContentLoaded", function () {
    getUserInfo();
    setTimeout(darkMode, 20);
});

function delay() {
    console.log("Delay.");
}

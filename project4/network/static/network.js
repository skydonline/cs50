// get username and ID
let currentUsername;
let currentUserID;
function getUserInfo() {
    currentUser = document.querySelector('#current-user');
    currentUsername = currentUser.dataset.user;
    currentUserID = currentUser.dataset.id;
    console.log(`Current User: ${currentUsername}`);
    console.log(`Current UserID: ${currentUserID}`);
}
document.addEventListener('DOMContentLoaded', () => getUserInfo());
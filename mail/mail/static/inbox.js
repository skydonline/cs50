/* 
const id = emails.id;
const sender = emails.sender;
const recipients = emails.recipients;
const subject = emails.subject;
const body = emails.body;
const timestamp = emails.timestamp;
const read = emails.read;
const archived = emails.archived;
*/

document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').onsubmit = function() {
    
    // send POST request to /email URL
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector("#compose-recipients").value,
        subject: document.querySelector("#compose-subject").value,
        body: document.querySelector("#compose-body").value,
        read: false,
        archived: false
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log(result);
    });
  }

}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails from respective mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    console.log(emails);
    emails.forEach(email => display_email(email, mailbox));

  })
  .catch(error => {
    console.log("Error: ", error);
  });


}

function display_email(email, mailbox) {
  const mailContainer = document.createElement('div');
  mailContainer.className = 'singleEmail';

  // reciever
  let reciever;
  if (mailbox === 'inbox') {
    reciever = truncateText(email.sender, 15);
  } else {
    reciever = truncateText(email.recipients, 15);
  }

  // truncate email subject line
  const subject = truncateText(email.subject, 55);
  

  mailContainer.innerHTML = 
  `
  <p class='mailText mailReciever'>${reciever}</p>
  <p class='mailText mailSubject'>${subject}</p>
  <p class='mailText mailTime'>${email.timestamp}</p>
  `

  if (email.read === true) {
    mailContainer.style.backgroundColor = 'lightgrey';
  }

  document.querySelector('#emails-view').appendChild(mailContainer);

  mailContainer.addEventListener('click', function() {
    load_email(email);
  });
};

function truncateText(text, limit) {
  if (text.length > limit) {
    return text.substr(0, limit-3) + '...';
  } else {
    return text;
  }
};

function load_email(email) {
  fetch(`/emails/${email.id}`)
  .then(response => response.json())
  .then(email => {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email').style.display = 'block';
    document.querySelector('#email').innerHTML = '';

    let archive_status;
    if (email.archived === false) {
      archive_status = 'Archive';
    } else {
      archive_status = 'Unarchive';
    }

    document.querySelector('#email').innerHTML = 
    `
    <p><b>From: </b>${email.sender}</p>
    <p><b>To: </b>${email.recipients}</p>
    <p><b>Subject: </b>${email.subject}</p>
    <p><b>Timestamp: </b>${email.timestamp}</p>
    <div class="">
      <button id="reply" class="emailButtons">Reply</button>
      <button id="archive" class="emailButtons">${archive_status}</button>
    </div>
    <div class="emailDivider"></div>
    <p>${email.body}</p>
    `;

    document.querySelector('#archive').addEventListener('click', () => archive(email));
  });

  fetch(`/emails/${email.id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  });
};

function archive(email) {
  if (email.archived === false) {
    fetch(`/emails/${email.id}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: true
      })
    });
  } else {
    fetch(`/emails/${email.id}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: false
      })
    });
  }
  load_mailbox('inbox');
};
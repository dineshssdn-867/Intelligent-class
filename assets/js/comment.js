/*Comment Form - Storing Data in Firebase*/
// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyA14djRHXrqE_sfvrdzAnBPHjQmYuiq_3I",
    authDomain: "intellisense-comment.firebaseapp.com",
    databaseURL: "https://intellisense-comment-default-rtdb.firebaseio.com",
    projectId: "intellisense-comment",
    storageBucket: "intellisense-comment.appspot.com",
    messagingSenderId: "50495912627",
    appId: "1:50495912627:web:118d65d2a0bde4e5dd0ec6",
    measurementId: "G-EW5VX2E1TV"
  };
  
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();
  
  
    // Refernece commentInfo collections
    let commentInfo = firebase.database().ref("CommentInfo");
    
    // Listen for a submit
    document.querySelector(".comment-form").addEventListener("submit", submitForm);
    
    function submitForm(e) {
      e.preventDefault();
    
      //   Get input Values
      let name = document.querySelector(".name").value;
      let email = document.querySelector(".email").value;
      let comment = document.querySelector(".comment").value;
      console.log(name, email, comment);
    
      saveCommentInfo(name, email, comment);
    
      document.querySelector(".comment-form").reset();

    }
    
    // Save infos to Firebase
    function saveCommentInfo(name, email, comment) {
      let newCommentInfo = commentInfo.push();
    
      newCommentInfo.set({
        name: name,
        email: email,
        comment: comment,
      });
  
      // Alert the user that the comment has been posted successfully
      Swal.fire({
        icon: 'success',
        title: 'Success!',
        text: 'Your comment has been posted successfully!',
      });
  
    }
  
  // Check data here: https://console.firebase.google.com/u/0/project/intellisense-comment/database/intellisense-comment-default-rtdb/data/~2F
  
  
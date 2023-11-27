/*Contact Form - Storing Data in Firebase*/

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBHDV4JiiL7kcJDf587i0N_qXliOLQ7iTo",
    authDomain: "intellisense-22c1f.firebaseapp.com",
    databaseURL: "https://intellisense-22c1f-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "intellisense-22c1f",
    storageBucket: "intellisense-22c1f.appspot.com",
    messagingSenderId: "1084876455360",
    appId: "1:1084876455360:web:e4613ba98b868743ea5c25",
    measurementId: "G-S7NKM7462P"
  };
  
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();
  
  
    // Refernece contactInfo collections
    let contactInfo = firebase.database().ref("ContactInfo");
    
    // Listen for a submit
    document.querySelector(".contact-form").addEventListener("submit", submitForm);
    
    function submitForm(e) {
      e.preventDefault();
    
      //   Get input Values
      let name = document.querySelector(".name").value;
      let email = document.querySelector(".email").value;
      let subject = document.querySelector(".subject").value;
      let message = document.querySelector(".message").value;
      console.log(name, email, message);
    
      saveContactInfo(name, email, subject, message);
    
      document.querySelector(".contact-form").reset();
    }
    
    // Save infos to Firebase
    function saveContactInfo(name, email, subject, message) {
      let newContactInfo = contactInfo.push();
    
      newContactInfo.set({
        name: name,
        email: email,
        subject: subject,
        message: message,
      });
  
      // Alert the user that the message has been sent successfully
      Swal.fire({
        icon: 'success',
        title: 'Success!',
        text: 'Your message has been sent successfully!',
      });
  
    }
  
  // Check data here: https://console.firebase.google.com/u/0/project/intellisense-22c1f/database/intellisense-22c1f-default-rtdb/data
  

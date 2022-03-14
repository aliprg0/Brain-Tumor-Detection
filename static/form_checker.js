function validateForm() {
  //selecting the elements to read their value later on

  var name = document.forms["myForm"]["name"];
  var email = document.forms["myForm"]["email"];
  var message = document.forms["myForm"]["message"];

  //if one of the elements has a problem or is null the request won't be send to the server
  if (name.value == "") {
    document.getElementById("errorname").innerHTML =
      "Please enter a valid name";
    name.focus();
    return false;
  } else {
    document.getElementById("errorname").innerHTML = "";
  }

  if (email.value == "") {
    document.getElementById("erroremail").innerHTML =
      "Please enter a valid email address";
    email.focus();
    return false;
  } else {
    document.getElementById("erroremail").innerHTML = "";
  }

  if (email.value.indexOf("@", 0) < 0) {
    document.getElementById("erroremail").innerHTML =
      "Please enter a valid email address";
    email.focus();
    return false;
  }

  if (email.value.indexOf(".", 0) < 0) {
    document.getElementById("erroremail").innerHTML =
      "Please enter a valid email address";
    email.focus();
    return false;
  }

  if (message.value == "") {
    document.getElementById("errormsg").innerHTML =
      "Please enter a valid message";
    message.focus();
    return false;
  } else {
    document.getElementById("errormsg").innerHTML = "";
  }

  return true;
}

document.getElementById("submit").addEventListener("click", myFunction);  
       function myFunction() {  
         window.location.href="/submit/";  
       }
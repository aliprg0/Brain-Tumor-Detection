function showPreview(event) {
  //checks if there is a file. then makes a preview of it
  if (event.target.files.length > 0) {
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-1-preview");
    preview.src = src;
    preview.style.display = "block";
  }

  //adding the picture into a form data for making a post request to the api
  const files = event.target.files;
  const formData = new FormData();
  formData.append("myFile", files[0]);

  //making the post request to the api
  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    //reading the response from server and showing it into Prediction_Result element
    .then((response) => response.json())
    .then((data) => {
      var pricesection = document.getElementById("Predicted_Result");
      pricesection.innerText = "نتیجه : " + data["Result"];
    })

    //if there's an error, you'll see it here
    .catch((error) => {
      console.error(error);
    });
}

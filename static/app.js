function showPreview(event) {
  if (event.target.files.length > 0) {
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-1-preview");
    preview.src = src;
    preview.style.display = "block";
  }
  const files = event.target.files;
  const formData = new FormData();
  formData.append("myFile", files[0]);
  console.log(formData)
  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      var pricesection = document.getElementById("Predicted_Result");
      pricesection.innerText = "Prediction : " + data["Result"];
    })
    .catch((error) => {
      console.error(error);
    });
}

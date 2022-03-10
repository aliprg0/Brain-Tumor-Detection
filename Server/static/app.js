
const handleImageUpload = (event) => {
  const files = event.target.files;
  const formData = new FormData();
  formData.append("myFile", files[0]);

  fetch("http://192.168.1.107:5000/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      var pricesection = document.getElementById("Predicted_Result");
      pricesection.innerText = data["Result"];
    })
    .catch((error) => {
      console.error(error);
    });
};


document.querySelector("#fileUpload").addEventListener("change", (event) => {
  handleImageUpload(event);
});

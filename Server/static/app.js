
const handleImageUpload = (event) => {
  const files = event.target.files;
  const formData = new FormData();
  formData.append("myFile", files[0]);
  
  console.log(formData);
  for (var value of formData.values()) {
    console.log(value)};

  fetch("http://192.168.1.107:5000/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
};


document.querySelector("#fileUpload").addEventListener("change", (event) => {
  handleImageUpload(event);
});

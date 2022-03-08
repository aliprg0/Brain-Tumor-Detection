const image_input = document.querySelector("#image_input");
var uploaded_image = "";
const button = document.getElementById("button")

image_input.addEventListener("change",function() {

    const reader = new FileReader();
    reader.addEventListener("load",() => {
        uploaded_image =reader.result;


        const el = document.querySelector('div');
        el.style.backgroundImage = `url(${uploaded_image})`;

    });
    reader.readAsDataURL(this.files[0]);
}

)

const myform = document.getElementById("myform")

myform.addEventListener("submit",e => {
    e.preventDefault();
    
    const inpFile = document.getElementById("image_input");

    const form_data = new FormData();

    form_data.append("inpFile",inpFile.files[0]);
     
    fetch("/predict", {
        method:"Post",
        body: form_data
    });
});
 
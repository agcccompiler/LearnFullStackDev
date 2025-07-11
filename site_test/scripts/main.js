const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/porsche911.png") {
    myImage.setAttribute("src", "images/spyderrs.png");
  } else {
    myImage.setAttribute("src", "images/porsche911.png");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
        setUserName()
    } else {
    localStorage.setItem("name", myName);
    myHeading.textContent = `Porsche 911 is cool, ${myName}`;
    }
}

if (!localStorage.getItem("name")) {
    setUserName();
} else {
    const storedName = localStorage.getItem("name");
    myHeading.textContent = `Porsche 911 is cool, ${storedName}`;
}
  
myButton.onclick = function () {
    setUserName();
  };
  
  
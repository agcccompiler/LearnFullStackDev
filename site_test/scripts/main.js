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
  
function gettingPrimes(n){
// 下面是一个不使用 push 的简单获取小于 n 的所有素数的实现方法。
// 先创建一个长度合适的数组，然后直接赋值。

let primes = new Array(n); // 预分配足够空间
let count = 0;
for (let i = 2; i < n; i++) {
    let isPrime = true;
    for (let j = 2; j * j <= i; j++) {
        if (i % j === 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        primes[count] = i;
        count++;
    }
}
primes.length = count; // 截断数组到实际素数个数
return primes;
}



var myHeading = document.querySelector('h1');
var myImage = document.querySelector("img");
var myButton = document.querySelector('button');

function setUserName() {
    var myName = prompt("please enter your name");
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Mozilla is cool, ' + myName;
}

if(!localStorage.getItem('name')) {
    setUserName();
} else {
    var storedName = localStorage.getItem('name');
    myHeading.textContent = 'Mozilla is cool, ' + storedName;
}



myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if (mySrc == 'images/firefox-icon.png'){
        myImage.setAttribute('src', 'images/firefox2.png');
}
    else{
        myImage.setAttribute('src', 'http://www.covenanteyes.com/lemonade/wp-content/uploads/2013/12/Firefox-icon.png')
        
        }
}

myButton.onclick = function () {
    setUserName();
}
//myHeading.textContent = 'hello world!';


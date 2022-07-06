var myI = document.querySelector('img');
myI.onclick = function () 
{
var mySrc = myI.getAttribute('src');
if (mySrc === 'images/image_1.jpeg') {
    myI.setAttribute('src', 'images/image_2.jpeg')}
    else {myI.setAttribute('src', 'images/image_1.jpeg')}
}
var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    var myName = prompt('Как вас зовут?');
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Добро пожаловать в ЮАР, ' + myName;
  }

  if(!localStorage.getItem('name')) 
  {
    setUserName();
  } else {
    var storedName = localStorage.getItem('name');
    myHeading.textContent = 'Добро пожаловать в ЮАР, ' + storedName;
  }

  myButton.onclick = function() {
    setUserName();
  }
  
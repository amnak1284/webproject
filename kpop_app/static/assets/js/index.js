var jumbotrons = document.getElementsByClassName("jumbotron");

var jumbotronElement = jumbotrons.length ? jumbotrons[0] : null;

if (jumbotronElement !== null) {
  jumbotronElement.addEventListener('click', function(event) {
     event.target.style.width *= .225; 	
  })
}



console.log("is it running?");

var button = document.getElementById('makebutton');

if (button !== null){
button.addEventListener('click', function(event){
        event.preventDefault();
	event.target.style.color= ("pink"); 
})
}

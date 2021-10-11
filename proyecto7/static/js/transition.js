timeLeft = 5;

function countdown() {
	timeLeft--;
	document.getElementById("seconds").innerHTML = String( timeLeft );
	if (timeLeft > 0) {
		setTimeout(countdown, 1000);
	}else{
		document.getElementById("clock").style.display = 'none';
		
	}
};

setTimeout(countdown, 1000);

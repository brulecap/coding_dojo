$(document).ready(function() {
	console.log("Ready");
	$("#wrapper button").click(function() {
		console.log("Button clicked");
		$( "#content img" ).fadeTo( "slow", 1, function() {
			console.log("Fade to complete");
		});
	});

	$("#content img").click(function() {
		console.log("Fade out");
		$(this).fadeTo("slow", 0, function() {
			//Fade out complete
		});
	});
})
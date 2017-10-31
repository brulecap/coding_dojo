$(document).ready(function() {
	$("#user_form").submit(function(event) {
		console.log($("#user_form input[name=first_name]").val(), " herer");
		event.preventDefault();
		$("tbody").append("<tr><td>" + $("#user_form input[name=first_name]").val() + "</td><td>" + $("#user_form input[name=last_name]").val() + "</td><td>" + $("#user_form input[name=email_address]").val() + "</td><td>" + $("#user_form input[name=contact_number]").val() + "</td></tr>");
	});
})
$(document).ready(function() {
	// Get the default text for the description textarea. This is used during error checking.
	var description_default = $("#description").text();
	var description_clicked = false;
	$("#user_form").submit(function(event) {
		/*
			Start with error checking and make sure all fields have values.
			If they don't set input border red and error to true
		*/
		var error = false;
		if ($("#first").val() === "") {
			$("#first").css("border", "1px solid red");
			error = true;
		}
		if ($("#last").val() === "") {
			$("#last").css("border", "1px solid red");
			error = true;
		}
		if (($("#description").val() === "") || ($("#description").val() === description_default)) {
			$("#description").css("border", "1px solid red");
			error = true;
		}
		if (error) {
			$("#contact_form h2").after('<p class="error">The red highlighted fields can not be empty.</p>');
		} else {
			// No error. Clean up the error indicators.
			$("#first").removeAttr( 'style' );
			$("#last").removeAttr( 'style' );
			$("#description").removeAttr( 'style' );
			$(".error").remove();
			//Add contact to contacts div
			var div_text = '<div><h3>' + $("#first").val() + ' ' + $("#last").val() + '</h3><a href="#">Click for description!</a>';
			div_text += '<p class="start_hidden">' + $("#description").val() + '</p><a class="start_hidden"" href="#">Click for name!</a></div>';
			$("#contacts").append(div_text);
			$(".start_hidden").hide();
			//Reset input and textarea fields to default values.
			$("#first").val("");
			$("#last").val("");
			$("#description").val(description_default);
			description_clicked = false;

		}
		event.preventDefault();
	});

	$("#contacts").on("click", "a", function() {
		$(this).toggle();
		$(this).siblings().each(function() {
			$(this).toggle();
		})
	});

	$("#description").click(function() {
		if (!description_clicked) {
			$(this).val("");
		}
	});
})
$(document).ready(function() {
	var fields =[["Toggle/Slide", "toggle_slide"], ["Text Manipulation", "text_manipulation"]];
	//Hide all of the content classes
	for (var i=0; i<fields.length; i++) {
		console.log(fields[i][1]);
		$('#' + fields[i][1]).addClass('display_none');
	}

	$("#text_manipulation p").data( "test", { first: "some ", last: "updated!" } );

	$('#left_nav li').click(function() {
		for (var i=0; i<fields.length; i++) {
			if (fields[i][0] === $(this).text()) {
				$('#' + fields[i][1]).addClass('inline_block');
				$('#' + fields[i][1]).removeClass('display_none');
			} else {
				$('#' + fields[i][1]).removeClass('inline_block');
				$('#' + fields[i][1]).addClass('display_none');
			}
		}
	});

	$('#slide_down').click(function() {
		$('#toggle_slide img').slideDown( "slow", function() {
			$('#slide_up').show();
			$('#slide_down').hide();
			$("#toggle").prop("disabled",false);
			$("#slide_toggle").prop("disabled",false);
			$('#fade_out').prop("disabled",false);
		});
	});

	$('#slide_up').click(function() {
		$('#toggle_slide img').slideUp( "slow", function() {
			$('#slide_down').show();
			$('#slide_up').hide();
			$("#toggle").prop("disabled",true);
			$("#slide_toggle").prop("disabled",true);
			$('#fade_out').prop("disabled",true);
		});
	});


	$("#fade_in").click(function() {
		$( "#toggle_slide img" ).fadeIn( "slow", function() {
			$('#fade_out').show();
			$("#fade_in").hide();
			$('#slide_up').prop("disabled",false);
			$("#toggle").prop("disabled",false);
			$("#slide_toggle").prop("disabled",false);
		});
	});

	$("#fade_out").click(function() {
		$( "#toggle_slide img" ).fadeOut( "slow", function() {
			$('#fade_in').show();
			$("#fade_out").hide();
			$('#slide_up').prop("disabled",true);
			$("#toggle").prop("disabled",true);
			$("#slide_toggle").prop("disabled",true);
		});
	});

	$('#toggle').click(function() {
		$('#toggle_slide img').toggle( "slow", function() {
			if ($('#toggle_slide img').css("display") === 'none') {
				$("#slide_up").prop("disabled",true);
				$("#slide_toggle").prop("disabled",true);
				$("#fade_out").prop("disabled",true);
			} else {
				$("#slide_up").prop("disabled",false);
				$("#slide_toggle").prop("disabled",false);
				$("#fade_out").prop("disabled",false);
			}
		});
	});

	$('#slide_toggle').click(function() {
		$('#toggle_slide img').slideToggle( "slow", function() {
			if ($('#toggle_slide img').css("display") === 'none') {
				$('#slide_up').prop("disabled",true);
				$("#toggle").prop("disabled",true);
				$("#fade_out").prop("disabled",true);
			} else {
				$('#slide_up').prop("disabled",false);
				$("#toggle").prop("disabled",false);
				$("#fade_out").prop("disabled",false);
			}
		});
	});

	$('#append').click(function() {
		$('#text_manipulation p').append($('#text_manipulation input:text').val());
	});

	$('#refresh').click(function() {
		$('#text_manipulation p').html("This is sample text");
		$('#text_manipulation p').before($("h2"));
		$('#text_manipulation h2').html("Header");
	});

	$('#after').click(function() {
		$('#text_manipulation p').after($("h2"));
	});

	$('#text').click(function() {
		$('#text_manipulation p').html($('button').text());
	});

	$('#data').click(function() {
		$("span:first").text($("p").data("test").first);
		$("span:last").text($("p").data("test").last);
	});

})
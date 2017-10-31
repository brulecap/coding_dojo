function create_content_html(res) {
	var html_str = `<h2>${res.name}</h2><img src="${res.sprites.front_default}"  alt="${res.name}">`;
	var type_str = "<h3>Types</h3><ul>";
	for (var j=0; j<res.types.length; j++) {
		type_str += `<li>${res.types[j].type.name}</li>`;
	}
	type_str += "</ul>";
	html_str += `${type_str}<h3>Weight</h3><p>${res.weight}</p><h3>Height</h3><p>${res.height}</p>`;
	return html_str;
}

$(document).ready(function(){
	$(document).ajaxStart(function() {
		$("#loading").show();
		$("#wrapper").fadeTo("slow", 0.5);
	});
	$(document).ajaxStop(function() {
		$('#loading').hide();  // hide loading indicator
		$("#wrapper").fadeTo("slow", 1);
	});

	$("#loading").hide();
	var pokeURL2 = "https://pokeapi.co/api/v2/pokemon/";
	var tempURL;
	var number_pokemon = 50; //Doing 151 caused problems outlined below. Seems good with 50.
	var one_selected = false;

	for (var index=1; index<=number_pokemon; index++) {
		/*
			Having some issues with the .ajax gets... 
			Some come back with the following error:
				Failed to load https://pokeapi.co/api/v2/pokemon/"index"/: 
				No 'Access-Control-Allow-Origin' header is present on the 
				requested resource. Origin 'null' is therefore not allowed
				access. The response had HTTP status code 504.
			It seems like the error is telling me there is a CORS issue, but
			why do some work and others not?
		*/
		$.ajax({
			type: 'GET',
			url: pokeURL2 + index + "/",
			data: null,
			dataType: 'json',
			success: function(response) {
				console.log(response);
				var sprite_img = `<img id="${response.id}" src="${response.sprites.front_default}" alt="${response.name}">`;
				$("#sprites").append(sprite_img);
				if (!one_selected) {
					$("#content").html(create_content_html(response));
					$("#"+response.id).addClass("selected");
					one_selected = true;
				}
			},
			xhrFields: {
				withCredentials: false
			},
			error: function(error) {
				console.log('ERROR:', error);

			}
		});
	}

	$("#sprites").on("click", "img", function() {
		console.log("getting");
		$.ajax({
			type: 'GET',
			url: pokeURL2 + $(this).attr("id") + "/",
			data: null,
			dataType: 'json',
			success: function(response) {
				$(".selected").removeClass("selected");
				$("#content").html(create_content_html(response));
				$("#"+response.id).addClass("selected");
				console.log(response);
			},
			xhrFields: {
				withCredentials: false
			},
			error: function(error) {
				console.log('ERROR:', error);

			}
		});
	})
});
$(document).ready(function(){
    $('form').submit(function() {
		// your code here (build up your url)
		var base_url = "http://api.openweathermap.org/data/2.5/weather?units=imperial";
		var api_key = "&appid=6dc2cc8059d26537c82de1951003f2f8";
		var city_prefix = "&q=";
		if ($("#location").val()!= "") {
			$.get(base_url+city_prefix+$("#location").val()+api_key, function(res) {
				var html_str = `<h2>${res.name}, ${res.sys.country}</h2><p>${res.main.temp}&#176; Fahrenheit</p>`;
				$("#content").html(html_str);
			}, 'json').fail(function(e) {
				var error_str = "";
				if (e.status == 404) {
					error_str = "<h3>Nothing was found matching " + $("#location").val() + "</h3>";
				} else {
					error_str = "<h3>An unanticipated error occurred. Please try again.</h3>";
				}
				$("#content").html(error_str);
			})
		}
		return false;
	});
});
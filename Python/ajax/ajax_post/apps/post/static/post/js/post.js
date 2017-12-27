$(document).ready(function(){
	$('#wrapper').on( "submit", "form", function(e) {
		e.preventDefault()
		console.log('Sending Ajax request to', $(this).attr('action'))
		console.log('Submitting the following data', $(this).serialize())
		$.ajax({
			url: $(this).attr('action'),
			method: 'post',
			data: $(this).serialize(),
			success: function(response) {
				console.log(response)
				$('#posts').html(response)
				$('#title').val('')
			}
		})
	})

	$.ajax({
		url: '/init/',
		method: 'get',
		success: function(response){
			console.log(response)
			$('#posts').html(response)
		}
	})
})
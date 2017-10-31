$(document).ready(function() {
	$("#content img").click(function() {
		var path = "";
		var backslash_index = $(this).attr('src').lastIndexOf("/");
		var current_image = $(this).attr('src');
		if (backslash_index != -1) {
			path = current_image.slice(0, backslash_index+1);
			current_image = current_image.substr(backslash_index+1);
			console.log("Found: ", backslash_index, " path ", path, " image ", current_image);
		}
		$(this).attr('src', path+$(this).attr('data-alt-src'));
		$(this).attr('data-alt-src', current_image);
	});
})
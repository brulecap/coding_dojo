var game_board = [[16,12,12,12,12,12,12,12,12,12,12,12,12,10,10,12,12,12,12,12,12,12,12,12,12,12,12,17],
[15,3,3,3,3,3,3,3,3,3,3,3,3,13,14,3,3,3,3,3,3,3,3,3,3,3,3,15],
[15,3,16,10,10,17,3,16,10,10,10,17,3,13,14,3,16,10,10,10,17,3,16,10,10,17,3,15],
[15,3,13,0,0,14,3,13,0,0,0,14,3,13,14,3,13,0,0,0,14,3,13,0,0,14,3,15],
[15,3,18,11,11,19,3,18,11,11,11,19,3,18,19,3,18,11,11,11,19,3,18,11,11,19,3,15],
[15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15],
[15,3,16,10,10,17,3,16,17,3,16,10,10,10,10,10,10,17,3,16,17,3,16,10,10,17,3,15],
[15,3,18,11,11,19,3,13,14,3,18,11,11,0,0,11,11,19,3,13,14,3,18,11,11,19,3,15],
[15,3,3,3,3,3,3,13,14,3,3,3,3,13,14,3,3,3,3,13,14,3,3,3,3,3,3,15],
[18,12,12,12,12,17,3,13,0,10,10,17,3,13,14,3,16,10,10,0,14,3,16,12,12,12,12,19],
[0,0,0,0,0,15,3,13,0,11,11,19,3,18,19,3,18,11,11,0,14,3,15,0,0,0,0,0],
[0,0,0,0,0,15,3,13,14,0,0,0,0,0,0,0,0,0,0,13,14,3,15,0,0,0,0,0],
[0,0,0,0,0,15,3,13,14,0,16,12,12,1,1,12,12,17,0,13,14,3,15,0,0,0,0,0],
[12,12,12,12,12,19,3,18,19,0,15,0,0,0,0,0,0,15,0,18,19,3,18,12,12,12,12,12],
[0,0,0,0,0,0,3,0,0,0,15,0,4,5,6,7,0,15,0,0,0,3,0,0,0,0,0,0],
[12,12,12,12,12,17,3,16,17,0,15,0,0,0,0,0,0,15,0,16,17,3,16,12,12,12,12,12],
[0,0,0,0,0,15,3,13,14,0,18,12,12,12,12,12,12,19,0,13,14,3,15,0,0,0,0,0],
[0,0,0,0,0,15,3,13,14,0,0,0,0,0,2,0,0,0,0,13,14,3,15,0,0,0,0,0],
[0,0,0,0,0,15,3,13,14,0,16,10,10,10,10,10,10,17,0,13,14,3,15,0,0,0,0,0],
[16,12,12,12,12,19,3,18,19,0,18,11,11,0,0,11,11,19,0,18,19,3,18,12,12,12,12,17],
[15,3,3,3,3,3,3,3,3,3,3,3,3,13,14,3,3,3,3,3,3,3,3,3,3,3,3,15],
[15,3,16,10,10,17,3,16,10,10,10,17,3,13,14,3,16,10,10,10,17,3,16,10,10,17,3,15],
[15,3,18,11,0,14,3,18,11,11,11,19,3,18,19,3,18,11,11,11,19,3,13,0,11,19,3,15],
[15,3,3,3,13,14,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,13,14,3,3,3,15],
[13,10,17,3,13,14,3,16,17,3,16,10,10,10,10,10,10,17,3,16,17,3,13,14,3,16,10,14],
[13,11,19,3,18,19,3,13,14,3,18,11,11,0,0,11,11,19,3,13,14,3,18,19,3,18,11,14],
[15,3,3,3,3,3,3,13,14,3,3,3,3,13,14,3,3,3,3,13,14,3,3,3,3,3,3,15],
[15,3,16,10,10,10,10,0,0,10,10,17,3,13,14,3,16,10,10,0,0,10,10,10,10,17,3,15],
[15,3,18,11,11,11,11,11,11,11,11,19,3,18,19,3,18,11,11,11,11,11,11,11,11,19,3,15],
[15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15],
[18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,19]];

/*
	The following constants define the different types of bricks in the game.
	The border on the bricks are defined by the classes. Class top for example
	puts a border on the top. Class left_top should be used in conjunction with left and top
	to provide a rounded border. Similarly with the other side_side combinations.
	ID pacman_holder denotes the place on the game board pacman will be put at the start of
	a game/round. Class pacman is the current position of pacman on the grid.
	Class coin_holder will have a point in place when at the start off each
	game/round. When pacman eats a coin, class point will be removed. 
*/
var classes=[];
classes[10] = 'class="brick top"';
classes[11] = 'class="brick bottom"';
classes[12] = 'class="brick top bottom"';
classes[13] = 'class="brick left"';
classes[14] = 'class="brick right"';
classes[15] = 'class="brick left right"';
classes[16] = 'class="brick left top left_top"';
classes[17] = 'class="brick right top right_top"';
classes[18] = 'class="brick left bottom left_bottom"';
classes[19] = 'class="brick right bottom right_bottom"';
classes[0] = 'class="blank"';
classes[1] = 'class="door"';
classes[2] = 'id="pacman_holder" class="pacman"';
classes[3] = 'class="coin_holder point"';
classes[4] = 'id="pinky_holder" class="pinky"';
classes[5] = 'id="blinky_holder" class="blinky"';
classes[6] = 'id="clyde_holder" class="clyde"';
classes[7] = 'id="inky_holder" class="inky"';

function create_game_board() {
	board_html = "";
	for (var i=0; i<game_board.length; i++) {
		board_html += '<div class="row">';
		for (var j=0; j<game_board[i].length; j++) {
			board_html += '<div ' + classes[game_board[i][j]] + '></div>';
		}
		board_html += '</div>';
	}
	return board_html;
}

const up_key = 38;
const down_key = 40;
const left_key = 37;
const right_key = 39;

var done = false;

function ghost(name) {
	this.name = name
	this.x = $("."+this.name).parent().index(),
	this.y = $("."+this.name).index();

	this.move = function(target) {

		//console.log("Moving inky...", this.name, " ", target.x);
	}
}

function set_position(moveable_object) {
	moveable_object.x = $("."+moveable_object.id).parent().index(),
	moveable_object.y = $("."+moveable_object.id).index();
}

function move(new_cell, transform) {
	var point = 0;
	if (new_cell.length === 0) {
		//Going to the other side of the board
		if ($(".pacman").index() === 0) {
			//left side
			new_cell = $(".pacman").siblings().last();
		} else {
			new_cell = $(".pacman").siblings().first();
		}
	}
	if (new_cell.attr("class").indexOf("brick") === -1) {
		if (new_cell.attr("class").indexOf("point") !== -1) {
			point = 1;
			new_cell.removeClass("point");
			if ($(".row").find(".point").length ===0) {
				done = true;
			}
		}
		$(".pacman").removeClass("pacman transform_down transform_left transform_up");
		new_cell.addClass("pacman" + transform);
	}
	return point;
}

$(document).ready(function(){
	$("#game_area").html(create_game_board());
	var points = 0;
	var pacman = {
		id: "pacman",
		x: $(".pacman").parent().index(),
		y: $(".pacman").index()
	};

//	var inky = new ghost("inky");
//	console.log(inky.x);
//	var nIntervId = setInterval(inky.move, 2000, pacman);;
//	inky.move(pacman);
//	setTimeout(inky.move(pacman), 5000);

	$(document).keydown(function(e) {
		if (!done) {
			if (e.keyCode == left_key) {
				points += move($(".pacman").prev(), " transform_left");
			} else if (e.keyCode == right_key) {
				points += move($(".pacman").next(), "");
			} else if (e.keyCode == up_key) {
				points += move($(".pacman").parent("div").prev().eq(0).children().eq($(".pacman").index()), " transform_up");
			} else if (e.keyCode == down_key) {
				points += move($(".pacman").parent("div").next().eq(0).children().eq($(".pacman").index()), " transform_down");
			}
		}

		set_position(pacman);
//		console.log(pacman);
		$("#wrapper p").html(points);
		if (done) {
			$("#done").show();
			$("#game_area").addClass("background");
		}
  		return false;
	});

	$("button").on("click", function() {
		$(".coin_holder").addClass("point");
		$(".pacman").removeClass("pacman");
		$("#pacman_holder").addClass("pacman");
		$(".pinky").removeClass("pinky");
		$("#pinky_holder").addClass("pinky");
		$(".clyde").removeClass("clyde");
		$("#clyde_holder").addClass("clyde");
		$(".blinky").removeClass("blinky");
		$("#blinky_holder").addClass("blinky");
		$(".inky").removeClass("inky");
		$("#inky_holder").addClass("inky");
		$("#game_area").removeClass("background");
		$("#done").hide();
		done = false;
	})
});
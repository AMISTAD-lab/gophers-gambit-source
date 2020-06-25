/* 
animation.js
Created on June 23, 2020
js file for the third experiment's animation
problem: gopher not on top of other image!!
*/


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
var gopher = document.createElement("img");
gopher.src = "testImages/adversaryidle/adversaryidle1.PNG";
gopher.id = "gopher";

// other vars
var fps = 1; // one frame per second
var frameNum = 0; // frame to start at
var totalFrames = 100; // change this later! The total NUMBER of frame

// inputs that will be set using getInput()
var terrainArray = []

// call init once document has loaded.
$(document).ready(function () {
	init();
});

/** Called when file is run */
function init() 
{
	getInput(); // will be written to the file.
	setUpGrid();
	animate();
}

/** populate grid with grid elements. Grid has same dimension as terrain array */
function setUpGrid()
{	//console.log("setting up grid");
	// set up number of columns in grid. 
	gridContainer.style.gridTemplateColumns = "repeat(" + String(terrainArray[0].length) + ", 1fr)";

	// set up elements: loop through terrain, adding div element
	for (let row = 0; row < terrainArray.length; row++)
	{
		//var rowList = []; // append an empty list for this row.

		for (let col = 0; col < terrainArray[0].length; col++)
		{
			// create div element, set its position.
			var div = document.createElement("div");
			div.style.gridColumnStart = col + 1;
			div.style.gridRowStart = row + 1; // add 1 because col, rows in gridlayout start at 1. 
			div.style.gridColumnEnd = col + 2;
			div.style.gridRowEnd = row + 2;
			div.classList.add("gridDiv");

			// NOTE: if setting up terrain ONCE and then just updating specific cells 
				// (i.e where gopher is, then keep this here. Otherwise, set up images each frame.)
			image = document.createElement("img");
			image.src = terrainArray[row][col];
			image.classList.add(".terrainImage");
			div.appendChild(image);

			// add to grid Container
			gridContainer.appendChild(div);
		}
	}
}


/** The animation. Calls draw.*/
function animate(){
	timer = setTimeout(function(){
		requestAnimationFrame(animate);  
	}, 1000/fps);// repaint 7 times a second

	// only go up to a certain number of steps
	if (frameNum >= totalFrames)
	{
		console.log("clearing timeout");
		clearTimeout(timer);
		return;
	}

	draw();


	frameNum++;	// step through (1 to 10)
}

/** draws one frame */
function draw(){
	// change position later, this one is for testing.
	redrawGopher([frameNum % terrainArray.length +1, frameNum % terrainArray[0].length + 1]);
}

/** moves a gopher from one cell to another */
function redrawGopher(newGopherCell){
	if (isValidGridPos(newGopherCell))
	{
		$("div.gridDiv:nth-of-type(" + String(getNth(newGopherCell)) +")").prepend(gopher); // prepend so gopher is on top

	}
	else{
		console.log("ERROR: NOT A VALID GRID POSITION");
	}
}

function getInput(){
	terrainArray = [["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]];
	/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
	/*[["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]];*/
	/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
}

/** Helper methods */

/** determines if the inputted list is a valid grid position. 
inputted list: [row, col] */
function isValidGridPos(gridPos){
	if (gridPos[0] <= 0 || gridPos[0] <= 0){ // row/column lines start at 1
		return false;
	} else if (gridPos[0] > terrainArray.length || gridPos[1] > terrainArray[0].length){ // and end at length
		return false;
	}
	return true;
}

/** calculates the number of the gridPos (in order of how they are added to the grid container */
function getNth(gridPos){
 	return (gridPos[0] - 1) * terrainArray[0].length + gridPos[1]; // row * total num columns + col
}
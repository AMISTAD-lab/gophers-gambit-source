/* 
animation.js
Created on June 23, 2020
js file for the third experiment's animation
*/


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
//var gopher = 
var gridElements = []; // array of div elements

// other vars
var fps = 1; // one frame per second
var frameNum = 0; // frame to start at
var totalFrames = 100; // change this later! The total NUMBER of frame

// inputs that will be set using getInput()
var terrainArray = [["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]];/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
/*[["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]];*/
/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
var lastGopherCell = [-1, -1]; // row and column of last gopher cell.

init();

/** Called when file is run */
function init() 
{
	getInput(); // will be written to the file.
	setUpGrid();
	animate();
}

/** populate grid with grid elements. Grid has same dimension as terrain array */
function setUpGrid()
{	
	// set up number of columns in grid. 
	//gridContainer.setAttribute("grid-template-columns", "repeat(" + String(terrainArray[0].length) + ", 1fr)");
	gridContainer.style.gridTemplateColumns = "repeat(" + String(terrainArray[0].length) + ", 1fr)";
	//gridContainer.gridTemplateColumns = "repeat(" + String(terrainArray[0].length) + ", 1fr)";

	// set up elements: loop through terrain, adding div element
	for (let row = 0; row < terrainArray.length; row++)
	{
		gridElements.push([]); // append an empty list for this row.

		for (let col = 0; col < terrainArray[0].length; col++)
		{
			// create div element, set its position.
			var div = document.createElement("div");
			div.style.gridColumn = col + 1;
			div.style.gridRow= row + 1; // add 1 because col, rows in gridlayout start at 1. 

			// NOTE: if setting up terrain ONCE and then just updating specific cells 
				// (i.e where gopher is, then keep this here. Otherwise, set up images each frame.)
			image = document.createElement("img");
			image.src = terrainArray[row][col];
			div.appendChild(image);

			// add to array
			gridElements[row].push(div);

			// add to grid Container
			gridContainer.appendChild(div);
		}
	}
}

/** moves a gopher from one cell to another */
/*function redrawGopher(newGopherCell){
	// remove gopher from previous cell
	if (isValidGridPos(lastGopherCell[0]){
		gridElements[lastGopherCell[0]][lastGopherCell[1]].removeChild(gopher);
	}
	// put gopher in new cell
	gridElements[newGopherCell[0]][newGopherCell[1]].appendChild(gopher);
}*/


/** The animation. Calls draw.*/
function animate(){
	timer = setTimeout(function(){
		requestAnimationFrame(draw);  
	}, 1000/fps);// repaint 7 times a second

	// only go up to a certain number of steps
	if (frameNum >= totalFrames)
	{
		clearTimeout(timer);
		return;
	}

	draw();

	frameNum++;	// step through (1 to 10)
}

/** draws one frame */
function draw(){

}



function getInput(){

}

/** Helper methods */

/** determines if the inputted list is a valid grid position. 
inputted list: [row, col] */
function isValidGridPos(gridPos){
	// can't be below 0
	if (gridPos[0] < 0 || gridPos[0] < 0){ // 1 because row/column lines start at 1
		return false;
	} else if (gridPos[0] > gridElements.length || gridPos[1] > gridElements[0].length){
		return false;
	}
	return true;
}

/**template.js
Created on June 23, 2020 by Cynthia Hom
js file for the third experiment's animation

Todo: 
Implement image rotation!!!!!! And test it!! yay
Test active states because for some reason they never seem to be active yet?
*/


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
var gopher = document.createElement("img");
//gopher.src = "testImages/adversaryidle/adversaryidle1.PNG";
gopher.id = "gopher";

// inputs that will be set using getInput()
var terrainList = []
var trapList = [] /// for testing purposes

// other vars
var fps = 1; // one frame per second

var currentList = []; // which grid to display at the current moment
var trapNum = 0;	// which trap/random walk animations to play
var trapFrameNum = 0; // which step in trap animation

// call init once document has loaded.
$(document).ready(function () {
	init();
});

/** Called when file is run */
function init() 
{
	//console.log(getImageName("211", 1));
	//let tupleList = [(1, 4, 0, 1), (1, 3, 0, 1)];
	//console.log("myTupleList is " + tupleList);
	getInput(); // get input that is written to the file.
	currentList = trapList; // CHANGE THIS LATER!
//	currentList = terrainList; // show the terrain first
	animate();
}

/** Removes any existing grid and sets up a new one. 
Inputs:
	gridListIn: the new 2-d array to display */
function updateGrid(gridListIn)
{	
	// remove existing grid by deleleting all gridElements.
	gridContainer.innerHTML = "";

	// set up number of columns in grid. 
	gridContainer.style.gridTemplateColumns = "repeat(" + String(gridListIn[0].length) + ", 1fr)";

	// set up elements: loop through terrain, adding div element
	for (let row = 0; row < gridListIn.length; row++)
	{
		//var rowList = []; // append an empty list for this row.

		for (let col = 0; col < gridListIn[0].length; col++)
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
			image.src = getImageName(gridListIn[row][col], 0); // initialize board to not active.
			image.classList.add(".boardImage");
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
	}, 1000/fps);// repaint 1 time a second

	// only go up to a certain number of steps
	if (trapNum >= trapList.length) // will end after last trap has been run
	{
		console.log("ANIMATION FINISHED");
		clearTimeout(timer);
		return;
	}

	draw();
	updateVars();
}

/** draws one frame */
function draw(){
	// if at the first step of this part, update the grid to reflect the surroundings
	if (trapFrameNum == 0){
		updateGrid(getCurrentlyDisplayedGrid());
	}

	// if it's a trap, also update the active/not active state.
	if (currentList == trapList){
		updateActiveStates(); 
	}

	// regardless, updateGopher's state
	updateGopher();
}

function updateVars(){
	trapFrameNum++;
	// if trapFrameNum is greater than max for that trap frame, then increment trapNum, change grid type, etc.
	if (trapFrameNum >= getCurrentGopherList().length) 
	{
		console.log("switching to a new trap");
		// switch between modes
		if (currentList == terrainList){
			currentList = trapList;
			console.log("UH OH");
		}
		else if (currentList == trapList){
//			currentList = terrainList;
			console.log("FINISHED TRAP #" + trapNum);
			trapNum++;	// if done with a trap, move on to next trap.
		}
		else{
			console.log("ERROR: currentList is not a terrainList or trapList");
		}
		// reset trapFrameNum
		trapFrameNum = 0;
	}
}


/** Updates whether or not cells are active or not for the trap part of the animation. */
function updateActiveStates()
{
	// make sure this is only being called for traps
	if (currentList != trapList){
		console.log("ERROR: Calling updateActiveStates when trapBoard is not showing");
		return;
	}
	
	activeStateList = trapList[trapNum][1][trapFrameNum];
	// loop through, and give appropriate img element the correct src.
	for (let row = 0; row < activeStateList.length; row++){
		for (let col = 0; col < activeStateList[0].length; col++){
			cell = [row + 1, col + 1];
			if (!isValidGridPos(cell)){
				console.log("ERROR: Not a valid grid position");
				return;
			}

			let image = $("img.boardImage:nth-of-type(" + String(getNth(cell)) +")");
			// make sure image exists first
			if (image == undefined){
				console.log("ERROR: image is undefined!");
				return;
			}

			isActiveNum = activeStateList[row][col]; 
			image.src = getImageName(getCurrentlyDisplayedGrid()[row][col], isActiveNum);  // set image src
		}
	}
}

/** Moves the gopher and updates its image */
function updateGopher(){
	console.log("trapFrameNum is " + trapFrameNum);
	console.log("currentGopherList is " + getCurrentGopherList());
	let gopherTuple = getCurrentGopherList()[trapFrameNum];
	gopher.src = getGopherImageName(gopherTuple); // update gopher image
	moveGopher(gopherTuple);
}

/** move the gopher to a given cell */
function moveGopher(gopherTuple){
	let cell = [gopherTuple[1] + 1, gopherTuple[0] + 1]; // row first then col
	// check if the grid position is valid first!
	console.log(String(gopherTuple));
	console.log(String(getNth(cell)));
	console.log(String(cell));
	if (isValidGridPos(cell))
	{
		$("div.gridDiv:nth-of-type(" + String(getNth(cell)) +")").prepend(gopher); // prepend so gopher is on top
	}
	else{
		console.log("ERROR: NOT A VALID GRID POSITION");
	}
}


/** --------------- Helper methods ----------*/

/** Returns the gopher Image name depending on its tuple. */
function getGopherImageName(gopherTuple){
	let stateNum = gopherTuple[3];
	let states = ["dead", "alive", "hit"];
	return "gopher/gopher" + states[stateNum] + ".png";
}

/** returns a cell name given a cell code. Cell code is the contents of the array that is passed in 
NOTE does not take into account rotation! ALSO is NOT used for gophers!
cellType + angleType+ thickType + isActive. 
*/
function getImageName(cellCode, isActiveNum){
	let cellType = getCellType(cellCode.charAt(0));
	let thickType = getThickType(cellCode.charAt(2));
	return cellType + thickType + "/" + cellType + getAngleType(cellCode.charAt(1)) + 
		thickType + getIsActive(isActiveNum) + ".png";
}

/** Interpret the char corresponding to cell type */
function getCellType(cellTypeIn){
	let cellTypes = ["gopher", "door", "wire", "arrow", "dirt", "food", "floor"];
	return cellTypes[parseInt(cellTypeIn)];
}

/** Interpret the char corresponding to angle type */
function getAngleType(angleTypeIn){
	if (angleTypeIn == 'x'){
		return "";
	}
	let angleTypes = ["lacute", "racute", "lright", "rright", "lobtuse", "robtuse", "straight"];
	return angleTypes [parseInt(angleTypeIn)];
}

/** Interpret the char corresponding to thick type */
function getThickType(thickTypeIn){
	if (thickTypeIn == 'x'){
		return "";
	}
	let thickTypes = ["skinny", "normal", "wide"]
	return thickTypes[parseInt(thickTypeIn)];
}

/** Return "true" if input is 1, "false" otherwise */
function getIsActive(isActiveNumIn){
	if(isActiveNumIn == 1){
		return "active";
	}
	return "inactive";
}

/** returns a 2d list corresponding to the currently displayed grid. */
function getCurrentlyDisplayedGrid(){
	if (currentList == terrainList){
		return currentList[0]; // terrain stays same before and after gopher goes into traps
	}
	return currentList[trapNum][0]; // the grid corresponding to the current trap.
}

/** returns a 2d list consisting of gopher tuples for 
	this given part of the animation. */
function getCurrentGopherList(){
	if (currentList == terrainList){
		return currentList[1][trapNum]; // overall gopher list is second element, must access this particular gopherList
	}else if (currentList == trapList){
		//console.log.log("returning " + currentList[trapNum][2]);
		return currentList[trapNum][2]; // third element in each tuple is gopherList
	}else{
		console.log("ERROR: currentList is not a terrainList or trapList");
	}
}

/** determines if the inputted list is a valid grid position. 
Inputs:
	gridPos: [row, col] */
function isValidGridPos(gridPos){
	currentlyDisplayedGrid = getCurrentlyDisplayedGrid();
	if (gridPos[0] <= 0 || gridPos[0] <= 0){ // row/column lines start at 1
		return false;
	} else if (gridPos[0] > currentlyDisplayedGrid.length || gridPos[1] > currentlyDisplayedGrid[0].length){ // and end at length
		return false;
	}
	return true;
}

/** calculates the number of the gridPos (in order of how they are added to the grid container 
Inputs:
	gridPos: [row, col] */
function getNth(gridPos){
 	return (gridPos[0] - 1) * getCurrentlyDisplayedGrid()[0].length + gridPos[1]; // row * total num columns + col
}
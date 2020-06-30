/** animation.js (template.js if does not contain getInput())
Created on June 23, 2020 by Cynthia Hom
js file for the third experiment's animation

Todo: 
Test everything using lots of different traps! */


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
var gopher = document.createElement("img");
gopher.id = "gopher";

// inputs that will be set using getInput()
var terrainList = []
var trapList = [] 

// other vars
var fps = 2; // show two frames per second

var currentList = []; // current grid to display
var trapNum = 0;	// current trap animation to play
var trapFrameNum = 0; // current step of trap animation

// call init once document has loaded.
$(document).ready(function () {
	init();
});

/** Called when file is run */
function init() 
{
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
	// remove existing grid by deleting all gridElements.
	gridContainer.innerHTML = "";

	// set up number of columns in grid. 
	gridContainer.style.gridTemplateColumns = "repeat(" + String(gridListIn[0].length) + ", 1fr)";

	// set up elements: loop through terrain, adding div element
	for (let row = 0; row < gridListIn.length; row++)
	{
		for (let col = 0; col < gridListIn[0].length; col++)
		{
			// create div element, set its position.
			let div = document.createElement("div");
			div.style.gridColumnStart = col + 1;
			div.style.gridRowStart = row + 1; // add 1 because col, rows in gridlayout start at 1. 
			div.style.gridColumnEnd = col + 2;
			div.style.gridRowEnd = row + 2;
			div.classList.add("gridDiv");

			// NOTE: if setting up terrain ONCE and then just updating specific cells 
				// (i.e where gopher is, then keep this here. Otherwise, set up images each frame.)
			let image = document.createElement("img");
			activeStateList = trapList[trapNum][1][0];
			image.src = getImageName(gridListIn[row][col], activeStateList[row][col]); // initialize board to its initial state. 
			image.style.transform = "rotate(" + getRotInDegrees(gridListIn[row][col][3]) + "deg)"; // fourth element is rotation. 
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
	}, 1000/fps);// repaint fps frames per second

	// animation ends after last trap has been run
	if (trapNum >= trapList.length) 
	{
		console.log("ANIMATION FINISHED");
		clearTimeout(timer);
		return;
	}

	draw();
	updateVars();
}

/** Draws one frame */
function draw(){
	console.log("trapFrameNum is " + trapFrameNum);
	// if at the first step of this trap, update the grid to reflect the new surroundings
	if (trapFrameNum == 0){
		updateGrid(getCurrentlyDisplayedGrid());
	}

	// if it's a trap, also update the active/not active state. Don't bother if grid has just been set up.
	else if (currentList == trapList){
		updateActiveStates(); 
	}

	// regardless, update the gopher's state
	updateGopher();
}

/** Updates variables to move to next frame, etc. */
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

			// get image. Must use gridContainer, because otherwise we can't change the src attribute.
			let image = gridContainer.children[getNth(cell) - 1].children[0]; // subtract 1 because .children returns an array.
			
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
	let gopherTuple = getCurrentGopherList()[trapFrameNum];
	gopher.src = getGopherImageName(gopherTuple); // update gopher image
	gopher.style.transform = "rotate(" + getRotInDegrees(gopherTuple[2]) + "deg)"; // fourth element is rotation. 
	moveGopher(gopherTuple);
}

/** move the gopher to a given cell */
function moveGopher(gopherTuple){
	let cell = [gopherTuple[1] + 1, gopherTuple[0] + 1]; // row first then col
	// check if the grid position is valid first!
	if (isValidGridPos(cell))
	{
		$("div.gridDiv:nth-of-type(" + String(getNth(cell)) +")").append(gopher); // prepend so gopher is on top
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

/** Returns a cell name given a cell code.
Cell code is the contents of the array that is passed in , eg. 41xx
Note: This is NOT used for gophers! 
*/
function getImageName(cellCode, isActiveNum){
	let cellType = getCellType(cellCode.charAt(0));
	let thickType = getThickType(cellCode.charAt(2));
	let imgName = cellType + thickType + "/" + cellType + getAngleType(cellCode.charAt(1)) + 
		thickType + getIsActive(isActiveNum) + ".png";
	return imgName;
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

/** Interpret the rotation char. Return the rotation from top in degrees */
function getRotInDegrees(rotTypeIn){
	if (rotTypeIn == 'x')
		return 0;
	return 45 * parseInt(rotTypeIn);
}

/** Return "active" if input is 1, "inactive" otherwise */
function getIsActive(isActiveNumIn){
	if(isActiveNumIn == 1){
		return "active";
	}
	else if (isActiveNumIn == 0){
		return "inactive";
	}
	console.log("ERROR: isActiveNumIn is neither 1 nor 0");
	return;
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

/** Calculates the cell number. Upper leftmost cell is #1. Read across rows and move down columns.
Inputs:
	gridPos: [row, col]. row, col both start at 1 */
function getNth(gridPos){
 	return (gridPos[0] - 1) * getCurrentlyDisplayedGrid()[0].length + gridPos[1]; // row * total num columns + col
}function getInput(){
trapList = [[[['2214', '2600', '3114'], ['3314', '5xxx', '2610'], ['3104', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2214', '2220', '3014'], ['2604', '5xxx', '3426'], ['3316', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2214', '2222', '3420'], ['3222', '5xxx', '2610'], ['3112', '1xx0', '3002'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2214', '3402', '2616'], ['6xxx', '5xxx', '3510'], ['3126', '1xx0', '3406'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2214', '2224', '3102'], ['3000', '5xxx', '3400'], ['3104', '1xx0', '3022'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2214', '2224', '3116'], ['3026', '5xxx', '3206'], ['3126', '1xx0', '3414'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3116', '3104'], ['6xxx', '5xxx', '3110'], ['3024', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3400', '3002'], ['3400', '5xxx', '2600'], ['3426', '1xx0', '3022'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3100', '3422'], ['3512', '5xxx', '3424'], ['2600', '1xx0', '3022'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3206', '3324'], ['3122', '5xxx', '3410'], ['3116', '1xx0', '6xxx'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3206', '3526'], ['3200', '5xxx', '2200'], ['3106', '1xx0', '3120'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2612', '3520', '3214'], ['2622', '5xxx', '3012'], ['3116', '1xx0', '2206'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '2620', '3002'], ['3324', '5xxx', '3110'], ['3002', '1xx0', '3002'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '2606', '3420'], ['2606', '5xxx', '3216'], ['3116', '1xx0', '2220'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '2606', '2200'], ['3406', '5xxx', '2602'], ['3106', '1xx0', '2226'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '3004', '3500'], ['2614', '5xxx', '2224'], ['3502', '1xx0', '3002'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '3124', '3520'], ['3506', '5xxx', '3324'], ['2214', '1xx0', '3002'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['3204', '3426', '3506'], ['6xxx', '5xxx', '3404'], ['3116', '1xx0', '3112'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3106', '2600'], ['3412', '5xxx', '3514'], ['3116', '1xx0', '3516'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3406', '3322'], ['2216', '5xxx', '2606'], ['3116', '1xx0', '2602'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3406', '3504'], ['3010', '5xxx', '3122'], ['3222', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3424', '3202'], ['3120', '5xxx', '3206'], ['3500', '1xx0', '3002'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3516', '2212'], ['3200', '5xxx', '3016'], ['3000', '1xx0', '3022'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '3516', '3006'], ['3326', '5xxx', '3004'], ['3116', '1xx0', '2614'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2222', '2212', '3100'], ['2606', '5xxx', '3324'], ['2620', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '3002', '3310'], ['3510', '5xxx', '3020'], ['3406', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '2622', '3512'], ['3326', '5xxx', '3510'], ['3116', '1xx0', '3406'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '2224', '3410'], ['3220', '5xxx', '3204'], ['3502', '1xx0', '3012'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '3522', '3320'], ['3000', '5xxx', '2212'], ['3106', '1xx0', '3526'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '3522', '2220'], ['3102', '5xxx', '3404'], ['3126', '1xx0', '2606'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]], [[['2202', '3212', '2614'], ['2220', '5xxx', '3400'], ['3114', '1xx0', '3022'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]]];
terrainList = [[[]], []];
}
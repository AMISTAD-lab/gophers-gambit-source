/**  template.js 
Created on June 23, 2020 by Cynthia Hom
js file for the third experiment's animation

Todo: 
One frame of all dirt. Gopher "moves to right", everything moves to left.
Make it work for width 3 height 4 traps
Test everything using lots of different traps! */


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
var gopher = document.createElement("img");
gopher.id = "gopher";

// inputs that will be set using getInput()
var trapList = [] 

// other vars
var fps = 2; // show two frames per second

var trapNum = 0;	// current trap animation to play
var trapFrameNum = 0; // current step of the current animation (either trap or movement)
var frameNum = 0; // frame for the overall animation

// call init once document has loaded.
$(document).ready(function () {
	init();
});

/** Called when file is run */
function init() 
{
	getInput(); // get input that is written to the file.
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
			image.src = getImageName(gridListIn[row][col], "0");// activeStateList[row][col]); // initialize board to its initial state. 
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
	//if (frameNum < getNumStartSteps())
	//{
		// make gopher move in 
		//moveGopher(gopherTuple)
	//}
	// if moving to a trap or moving away from trap, update the grid and make gopher rotate. 
	if (areChangingTraps())
	{
		updateGrid(getCurrentlyDisplayedGrid());
	}
	// otherwise, simply update the active states of the grid and the gopher position/rotation.
	else
	{
		updateActiveStates(); 
	}
	updateGopher();
}

/** Updates variables to move to next frame, etc. */
function updateVars(){
	frameNum++;
	trapFrameNum++;
	// if we have just finished starting sequence, then don't make gopher "move to" the trap again!
	//if (frameNum == getNumStartSteps()){
		//trapFrameNum = getTrapWidth();
	//}
	// if done with this trap, then switch traps. If on the last trap, don't make gopher go to next trap. Note: not sure if this will work as well for hunger. 
	if ((trapFrameNum > getCurrentGopherList().length + 2 * getTrapWidth()) ||
		(trapNum == trapList.length - 1 && trapFrameNum >= getCurrentGopherList().length + getTrapWidth()))
	{
		console.log("FINISHED TRAP #" + trapNum);
		trapNum++;	// if done with a trap, move on to next trap.

		// reset trapFrameNum
		trapFrameNum = 0;
	}
}


/** Updates whether or not cells are active or not for the trap part of the animation. */
function updateActiveStates()
{
	activeStateList = trapList[trapNum][1][trapFrameNum - getTrapWidth()];
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
	let gopherTuple = []
	// if we are changing traps, make gopher turn to right and be in center of trap area.
		// otherwise, make gopher do what it is supposed to according to input. 
	if (areChangingTraps()){
		gopherTuple = getCurrentGopherList()[0]; // make gopher show up in center, ie. same state as its first step in trap animation.
		gopher.style.transform = "rotate(90deg)";
	}else{
		gopherTuple = getCurrentGopherList()[trapFrameNum - getTrapWidth()];
		gopher.src = getGopherImageName(gopherTuple); // update gopher image
		gopher.style.transform = "rotate(" + getRotInDegrees(gopherTuple[2]) + "deg)"; // fourth element is rotation. 
	}
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
	// if we are not in the middle of changing traps, just return the grid. Otherwise, calc the grid.
	if (!areChangingTraps()){
		return trapList[trapNum][0];
	}
	
	// create an array initialized to all dirt
	let gridArr = makeDirtArray();

	// if moving toward a trap, then show the trap slowly coming into view. Replace
		// the columns of dirt with trap columns.
	if (trapFrameNum < getTrapWidth()){
		// start at first column of trap, replace as many columns as trapFrameNum dictates.
		for (let trapCol = 0; trapCol <= trapFrameNum; trapCol++)
		{
			gridCol = getTrapWidth() - 1 - trapFrameNum + trapCol; // which grid column to replace with this trap column.
			gridArr = replaceCol(gridArr, gridCol, trapCol); 
		}
	}
	// if moving away from a trap, then show trap slowly moving away from view.
	else{
		// trapCol is the first col to show. Goes from 0 to 3. AND show all columns after trapCol.
		let animNum = trapFrameNum - (getTrapWidth() + getCurrentGopherList().length);
		for (let trapCol = animNum; trapCol < getTrapWidth(); trapCol++) 
		{
			gridCol = trapCol - animNum; // grid column to change is dependent upon which stage of animation we are at. Further along we are, the more columns shift to left.
			gridArr = replaceCol(gridArr, gridCol, trapCol);
		}
	}
	return gridArr;
}

/** Replaces the gridCol column in gridArr with the trapCol column in the trap array. 
Assumes that gridArr and trap array have the same number of rows. */
function replaceCol(gridArr, gridCol, trapCol){
	// loop through all rows, change that column.
	for (let row = 0; row < gridArr.length; row++){
		gridArr[row][gridCol] = trapList[trapNum][0][row][trapCol]; // Don't add 0 to make it inactive, this is done in updateGRid()
	}
	return gridArr
}

/** Returns a 2-d array of all dirt, with same size as the current trap board. */
function makeDirtArray(){
	// create an array initialized to all dirt
	let gridArr = []
	for (let row = 0; row < getTrapHeight(); row++){
		gridArr.push([])
		for (let col = 0; col < getTrapWidth(); col++){
			gridArr[row].push('4xxx');
		}
	}
	return gridArr;
}


function getTrapWidth(){
	let grid = trapList[trapNum][0]; // first element is the grid
	return grid[0].length;
}

function getTrapHeight(){
	let grid = trapList[trapNum][0]; // first element is the grid
	return grid.length;
}

/** returns a 2d list consisting of gopher tuples for 
	this given part of the animation. */
function getCurrentGopherList(){
	return trapList[trapNum][2]; // third element in each tuple is gopherList
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

/** returns true if we are currently in the middle of switching from one trap to the next, false otherwise */
function areChangingTraps(){
	return (trapFrameNum < getTrapWidth()) || (trapFrameNum >= getCurrentGopherList().length + getTrapWidth());
}

/** Calculates the cell number. Upper leftmost cell is #1. Read across rows and move down columns.
Inputs:
	gridPos: [row, col]. row, col both start at 1 */
function getNth(gridPos){
 	return (gridPos[0] - 1) * getCurrentlyDisplayedGrid()[0].length + gridPos[1]; // row * total num columns + col
}
function getInput(){
trapList = [[[['6xxx', '6xxx', '6xxx'], ['6xxx', '5xxx', '3000'], ['3500', '6xxx', '2600'], ['2306', '1xx0', '2202'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['3006', '2214', '6xxx'], ['6xxx', '5xxx', '2614'], ['3524', '6xxx', '2610'], ['6xxx', '1xx0', '3302'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['3404', '3124', '3404'], ['2600', '5xxx', '2216'], ['2622', '6xxx', '3520'], ['6xxx', '1xx0', '6xxx'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['3120', '3226', '2220'], ['2620', '5xxx', '2620'], ['2620', '6xxx', '2620'], ['2326', '1xx0', '2222'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['6xxx', '6xxx', '6xxx'], ['3100', '3216', '2210'], ['2600', '5xxx', '2610'], ['2204', '1xx0', '2216'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['3410', '6xxx', '3300'], ['3516', '5xxx', '6xxx'], ['3420', '6xxx', '3402'], ['6xxx', '1xx0', '3126'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['6xxx', '6xxx', '6xxx'], ['6xxx', '5xxx', '3010'], ['3510', '6xxx', '2610'], ['2316', '1xx0', '2212'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['2624', '2210', '6xxx'], ['3500', '5xxx', '6xxx'], ['2206', '6xxx', '3402'], ['2204', '1xx0', '6xxx'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['3526', '6xxx', '3426'], ['3116', '5xxx', '6xxx'], ['3114', '6xxx', '6xxx'], ['6xxx', '1xx0', '3520'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['6xxx', '6xxx', '2222'], ['6xxx', '5xxx', '6xxx'], ['6xxx', '6xxx', '6xxx'], ['2220', '1xx0', '6xxx'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['2600', '6xxx', '3024'], ['6xxx', '5xxx', '2606'], ['2610', '6xxx', '3214'], ['2602', '1xx0', '3016'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['6xxx', '6xxx', '6xxx'], ['6xxx', '6xxx', '6xxx'], ['3310', '5xxx', '3210'], ['2316', '1xx0', '2212'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['2210', '2214', '2200'], ['6xxx', '5xxx', '2210'], ['6xxx', '6xxx', '3002'], ['2202', '1xx0', '3316'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['3320', '6xxx', '6xxx'], ['6xxx', '5xxx', '6xxx'], ['3410', '6xxx', '6xxx'], ['6xxx', '1xx0', '2624'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 2, 4, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['6xxx', '6xxx', '3302'], ['2206', '5xxx', '2600'], ['6xxx', '6xxx', '2202'], ['3506', '1xx0', '6xxx'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 3, 4, 1], [1, 4, 4, 1]]], [[['2310', '3312', '6xxx'], ['2610', '5xxx', '3210'], ['2610', '6xxx', '2610'], ['2316', '1xx0', '2212'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1]]], [[['3110', '6xxx', '6xxx'], ['2610', '5xxx', '6xxx'], ['2610', '6xxx', '3420'], ['2316', '1xx0', '2222'], ['4xxx', '4xxx', '4xxx']], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[1, 4, 0, 1], [1, 3, 0, 1], [1, 2, 0, 1], [1, 1, 0, 0]]]];
}
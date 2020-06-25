/**
animation.js
Created on June 23, 2020 by Cynthia Hom
js file for the third experiment's animation
Todo: test rigorously!
test/implement methods to interpret code (don't use them yet, just make them)
test getinput
after amani is done drawing images: implement images.
rotate images.
*/


// get elements from the html
var gridContainer = document.getElementById("gridContainer");
var gopher = document.createElement("img");
gopher.src = "testImages/adversaryidle/adversaryidle1.PNG";
gopher.id = "gopher";

// inputs that will be set using getInput()
var terrainList = []
var trapList = [] /// for testing purposes

// other vars
var fps = 1; // one frame per second
var frameNum = 0; // frame counter
var totalFrames = 10; // change this later! The total NUMBER of frame

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
	getInput(); // will be written to the file.
	currentList = terrainList; // show the terrain array first
	animate();
}

/** Removes any existing grid and sets up a new one */
function updateGrid(newGridList)
{
	// remove existing grid by deleleting all gridElements.
	console.log("inside updateGrid");
	gridContainer.innerHTML = "";

	// set up new grid
	setUpGrid(newGridList);
}

/** populate grid with grid elements. Grid has same dimension as terrain array */
function setUpGrid(gridListIn)
{
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
			image.src = gridListIn[row][col];
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
	}, 1000/fps);// repaint 1 time a second

	// only go up to a certain number of steps
	if (trapNum >= trapList.length)
	{
		console.log("ANIMATION FINISHED");
		clearTimeout(timer);
		return;
	}
	console.log("inside animate, trapNum is " + trapNum + " and trapFrameNum is " + trapFrameNum)

	draw();
	updateVars();
}

/** draws one frame */
function draw(){
	// if it's a terrain, just show the terrain grid if its the first step, and then update gopher position
	if (currentList == terrainList)
	{
		if (trapFrameNum == 0)
		{
			updateGrid(getCurrentlyDisplayedGrid());
		}
		redrawGopher([2, 2]);//[frameNum % currentList[trapNum][trapFrameNum].length + 1, frameNum % currentList[trapNum][trapFrameNum].length + 1]) // replace with actual gopher position later
	}

	// if it's a trap, then show the trap grid if this is the first time we are showing the trap. Otherwise,
		// just update the active states of the cell.
	else if (currentList == trapList)
	{
		if (trapFrameNum == 0)
		{
			updateGrid(getCurrentlyDisplayedGrid());
		}
		// regardless, update active states and draw the gopher
		updateGrid(getCurrentlyDisplayedGrid());// REMOVE later, only for testing! 
		//updateActiveStates(trapNum, trapFrameNum); 
		redrawGopher([2, 2]);//[frameNum % currentList[trapNum][trapFrameNum].length + 1, frameNum % currentList[trapNum][trapFrameNum].length + 1]);
	}
}

function updateVars(){
	trapFrameNum++;
	// if trapFrameNum is greater than max for that trap frame, then increment trapNum, change grid type, etc.
	if (trapFrameNum >= currentList[trapNum].length)
	{
		if (currentList == terrainList){
			currentList = trapList;
		}
		else if (currentList == trapList){
			currentList = terrainList;
			trapNum++;
		}
		else{
			console.log("ERROR: invalid currentList!");
		}
		// reset trapFrameNum
		trapFrameNum = 0;
	}
	frameNum++;	// step through NOTE: might be able to just take this out? 
}

/** Updates whether or not cells are active or not for the trap part of the animation. */
function updateActiveStates(trapNum, trapFrameNum)
{
	//console.log("trap num is " + trapNum + " trapFrameNum is " + trapFrameNum);
	// make sure this is only being called for traps
	if (currentList != trapList){
		console.log("ERROR: Calling updateActiveStates when trapBoard is not showing");
	}
	else{
		activeStateArr = currentList[trapNum][trapFrameNum];
		// loop through, and give appropriate img element the correct src.
		for (let row = 0; row < activeStateArr.length; row++){
			for (let col = 0; col < activeStateArr[0].length; col++){
				cell = [row + 1, col + 1];
				//console.log("is the cell a valid grid poistion? " + isValidGridPos(cell));
				//console.log("looking for div " + "div.gridDiv:nth-of-type(" + String(getNth(cell)) +")");
				//console.log("div is " + $("div.gridDiv:nth-of-type(" + String(getNth(cell)) +")"));
				image = $("img.terrainImage:nth-of-type(" + String(getNth(cell)) +")");

				//var image = $("div.gridDiv:nth-of-type(" + String(getNth(cell)) +")").lastChild;
				//console.log("image is " + image);
				if (image == undefined){
					console.log("ERROR: image is undefined!");
					return;
				}
				oldSrc = getCurrentlyDisplayedGrid()[row][col]; // change later to actually have the value!!!
				image.src = oldSrc.substring(0, oldSrc.length - 1) + String(activeStateArr[row][col]);  // create new src
				//image.src = image.src.substring(0, image.src.length - 1) + String(activeStateArr[row][col]);  // create new src
			}
		}
	}
	//console.log("updating active states!");
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


/** --------------- Helper methods ----------*/

/** returns a 2d list corresponding to the currently displayed grid. */
function getCurrentlyDisplayedGrid(){
	if (currentList == terrainList){
		return currentList[trapNum][0]; // Just for testing! Remove later! // If a terrain, then don't even use [0].
	}
	return currentList[trapNum][0]; // If its a trap, the current grid is the first index
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


/** -------this method will in reality be written to the file using python---------- */
function getInput(){
	terrainList = [[[["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"]]],
				[[["testImages/adversaryidle/adversaryidle1.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"],
				["testImages/adversarymad/adversarymad1.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG",  "testImages/environment/environment.PNG"]]]];
	trapList = [[[["testImages/adversarymad/adversarymad1.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad2.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad3.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad4.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad5.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad6.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]],
				[["testImages/adversarymad/adversarymad7.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]]],
				[[["testImages/adversaryattack/adversaryattack7.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/adversaryattack/adversaryattack7.PNG", "testImages/environment/environment.PNG"]]]];
	/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
	/*[["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"],
				["testImages/environment/environment.PNG", "testImages/environment/environment.PNG"]];*/
	/*[["testImages/environment/environment.PNG", "testImages/heroattack/heroattack1.PNG"],
				["testImages/adversaryidle/adversaryidle1.PNG", "testImages/adversaryattack/adversaryattack1.PNG"]];*/
}
let dictionary = {};
dictionary[0] = "black"
dictionary[1] = "brown"
dictionary[2] = "red"
dictionary[3] = "orange"
dictionary[4] = "yellow"
dictionary[5] = "green"
dictionary[6] = "blue"
dictionary[7] = "darkviolet"
dictionary[8] = "grey"
dictionary[9] = "cornsilk"

let tolerance = {};
tolerance[0] = "silver"
tolerance[1] = "gold"
tolerance[2] = "brown"

let fourBandMultiply = {};
fourBandMultiply[0] = "silver";
fourBandMultiply[1] = "gold";
fourBandMultiply[2] = "black";
fourBandMultiply[3] = "brown";
fourBandMultiply[4] = "red";
fourBandMultiply[5] = "orange";
fourBandMultiply[6] = "yellow";
fourBandMultiply[7] = "green";

let multipler = {};
multipler[0] = 1;
multipler[1] = 10;
multipler[2] = 100;
multipler[3] = 1000;
multipler[4] = 10000;
multipler[5] = 100000;
multipler[6] = 1000000;

let fourmultiply = {};
fourmultiply[0] = 0.01;
fourmultiply[1] = 0.1;
fourmultiply[2] = 1;
fourmultiply[3] = 10;
fourmultiply[4] = 100;
fourmultiply[5] = 1000;
fourmultiply[6] = 10000; 
fourmultiply[7] = 100000;

var bandOne = 1;
var bandTwo = 0;
var bandThree = 0;
var bandFour = 1;

var bandOneFour = 1;
var bandTwoFour = 0;
var bandThreeFour = 0;
var bandFourFour = 0;
var bandFiveFour = 0;

firstBand = document.getElementById("first-band");
secondBand = document.getElementById("second-band");
thirdBand = document.getElementById("third-band");
fourthBand = document.getElementById("fourth-band");

firstBandFour = document.getElementById("four-first-band");
secondBandFour = document.getElementById("four-second-band");
thirdBandFour = document.getElementById("four-third-band");
fourthBandFour = document.getElementById("four-fourth-band");
fifthBandFour = document.getElementById("four-fifth-band");

function firstClicker(){

    if (bandOne == 9) {
        bandOne = 1;
    }

    else {bandOne += 1;}

    color = document.getElementById("first-band");
    color.style.backgroundColor = dictionary[bandOne];  
    calcValue();  
}

function secondClicker(){

    if (bandTwo == 9) {
        bandTwo = 0;
    }

    else {bandTwo += 1;}

    color = document.getElementById("second-band");
    color.style.backgroundColor = dictionary[bandTwo];   
    calcValue();  
}

function thirdClicker(){

    if (bandThree == 6) {
        bandThree = 0;
    }

    else {bandThree += 1;}

    color = document.getElementById("third-band");
    color.style.backgroundColor = dictionary[bandThree];
    calcValue();     
}

function fourthClicker(){

    if (bandFour == 1) {
        bandFour = 0;
    }

    else {bandFour += 1;}

    color = document.getElementById("fourth-band");
    color.style.backgroundColor = tolerance[bandFour];    

    calcTolerance()
}

function calcValue() {

    strOne = bandOne.toString();
    strTwo = bandTwo.toString();
    combStr = strOne + strTwo;
    combInt = parseInt(combStr);
    var suffix = ""

    totalValue = combInt * multipler[bandThree]

    if (totalValue >= 1000000) {
        suffix = "MΩ";
    } else if (totalValue >= 1000) {
        suffix = "kΩ";
    } else {
        suffix = "Ω";
    }

    if (suffix == "Ω") {
        outputString = totalValue.toString() + suffix;
    } else if (suffix == "kΩ") {
        kiloValue = totalValue / 1000;
        outputString = kiloValue.toString() + suffix;
    } else if (suffix == "MΩ"){
        megaValue = totalValue / 1000000;
        outputString = megaValue.toString() +suffix;
    }
      
    return document.getElementById("resistance-total").innerText = outputString;
}

function calcTolerance() {
    if (bandFour == 1) {
        toleranceString = "±5%";
    } else {
        toleranceString = "±10%";
    }

        return document.getElementById("tolerance-total").innerText = toleranceString;

}

function firstClickerFour(){

    if (bandOneFour == 9) {
        bandOneFour = 1;
    }

    else {bandOneFour += 1;}

    color = document.getElementById("four-first-band");
    color.style.backgroundColor = dictionary[bandOneFour];
    calcValueFour();
    
}

function secondClickerFour(){

    if (bandTwoFour == 9) {
        bandTwoFour = 0;
    }

    else {bandTwoFour += 1;}

    color = document.getElementById("four-second-band");
    color.style.backgroundColor = dictionary[bandTwoFour];   
    calcValueFour();
}

function thirdClickerFour(){

    if (bandThreeFour == 9) {
        bandThreeFour = 0;
    }

    else {bandThreeFour += 1;}

    color = document.getElementById("four-third-band");
    color.style.backgroundColor = dictionary[bandThreeFour];   
    calcValueFour();
}

function fourthClickerFour(){

    if (bandFourFour == 7) {
        bandFourFour = 0;
    }

    else {bandFourFour += 1;}

    color = document.getElementById("four-fourth-band");
    color.style.backgroundColor = fourBandMultiply[bandFourFour];
    calcValueFour();
}

function fifthClickerFour(){

    if (bandFiveFour == 2) {
        bandFiveFour = 0;
    }

    else {bandFiveFour += 1;}

    color = document.getElementById("four-fifth-band");
    color.style.backgroundColor = tolerance[bandFiveFour]; 
    calcToleranceFour();   
    
}

function calcToleranceFour() {
    if (bandFiveFour == 1) {
        toleranceStringFour = "±5%";
    } else if (bandFiveFour == 2) {
        toleranceStringFour = "±1%";
    } else {
        toleranceStringFour = "±10%";
    }

        return document.getElementById("four-tolerance-total").innerText = toleranceStringFour;

}

function calcValueFour() {

    strOneFour = bandOneFour.toString();
    strTwoFour = bandTwoFour.toString();
    strThreeFour = bandThreeFour.toString();
    combStrFour = strOneFour + strTwoFour + strThreeFour;
    combIntFour = parseInt(combStrFour);
    var suffixFour = ""

    totalValueFour = combIntFour * fourmultiply[bandFourFour]

    if (totalValueFour >= 1000000) {
        suffixFour = "MΩ";
    } else if (totalValueFour >= 1000) {
        suffixFour = "kΩ";
    } else {
        suffixFour = "Ω";
    }

    if (suffixFour == "Ω") {
        totalValueFour = Math.round(totalValueFour * 100) / 100;
        outputStringFour = totalValueFour.toString() + suffixFour;
    } else if (suffixFour == "kΩ") {
        kiloValueFour = totalValueFour / 1000;
        kiloValueFour = Math.round(kiloValueFour * 100) / 100;
        outputStringFour = kiloValueFour.toString() + suffixFour;
    } else if (suffixFour == "MΩ"){
        megaValueFour = totalValueFour / 1000000;
        megaValueFour = Math.round(megaValueFour * 100) / 100;
        outputStringFour = megaValueFour.toString() +suffixFour;
    }
      
    return document.getElementById("four-resistance-total").innerText = outputStringFour;
}
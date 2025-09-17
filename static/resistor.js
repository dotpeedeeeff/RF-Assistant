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

let multipler = {};
multipler[0] = 1
multipler[1] = 10
multipler[2] = 100
multipler[3] = 1000
multipler[4] = 10000
multipler[5] = 100000
multipler[6] = 1000000


var bandOne = 1;
var bandTwo = 0;
var bandThree = 0;
var bandFour = 1;

firstBand = document.getElementById("first-band");
secondBand = document.getElementById("second-band");
thirdBand = document.getElementById("third-band");
fourthBand = document.getElementById("fourth-band");

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
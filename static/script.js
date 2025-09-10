function stopCheck(){
    let capStart = document.getElementById("startcapacitance").value;
    let capStop = document.getElementById("stopcapacitance").value;

    capStart = Number(capStart);
    capStop = Number(capStop);
            
    if (capStop <= capStart) {
        warn = "Only one result will be returned, stop capacitance is less than start capacitance.";
        document.getElementById("stopcheck").innerHTML = warn;       
}
    else {document.getElementById("stopcheck").innerHTML = "" };
}

function stepCheck(){
    
    let capStep = document.getElementById("capacitancestep").value;
        
    capStep = Number(capStep);    
                    
    if (capStep == 0) {
        warn = "Only one result will be returned, step size is zero.";
        document.getElementById("stepcheck").innerHTML = warn;       
                    }
    else {document.getElementById("stepcheck").innerHTML = "" };
 }

document.onload = stepCheck();

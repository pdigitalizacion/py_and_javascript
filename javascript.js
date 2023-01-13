//function myFunc(vars) {
//    return vars
//}

var objects = {"alerts":[
    {"alert":"alert_order","info":"error1"},
    {"alert":"alert_ID","info":"error2"}
    ]};

document.getElementById('content').innerHTML = objects.alerts[0].alert;

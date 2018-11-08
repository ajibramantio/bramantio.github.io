var myVar;

function myFunction() {
    myVar = setTimeout(showPage, 3000);
}

function showPage() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

function tema() {
    if (document.body.style.backgroundColor == "rgb(222, 222, 222)") {
        document.body.style.backgroundColor = "rgb(39,60,80)";
        document.body.style.color = "#8ba691";
        document.body.style.fontFamily = "'Marck Script', cursive"
        document.getElementsByClassName("accordion").style.backgroundColor = "#080b12";
    } else {
        document.body.style.backgroundColor = "rgb(222,222,222)";
        document.body.style.color = "#384D54";
        document.body.style.fontFamily = "'Ropa Sans', Verdana, Tahoma";
        document.getElementsByClassName("accordion").style.backgroundColor = "#eee";
    }
}
    
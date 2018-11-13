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
    if (document.body.style.background == "rgb(222, 222, 222)") {
        document.body.style.background = "rgb(39,60,80)";
        document.body.style.color = "#8ba691";
        document.body.style.fontFamily = "'Marck Script', cursive"
        // document.getElementsByClassName("accordion").style.background = "#080b12";
    } else {
        document.body.style.background = "rgb(222,222,222)";
        document.body.style.color = "#384D54";
        document.body.style.fontFamily = "'Ropa Sans', Verdana, Tahoma";
        // document.getElementsByClassName("accordion").style.background = "#eee";
    }
}

var categ = [];
var bukus = [];
var counter = 0;
var favo = 'Favorite(s): ';
$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'https://www.googleapis.com/books/v1/volumes?q=quilting',
        dataType: 'json',
        success: function (data) {
            var print = '<tr>';
            for (var i = 1; i <= data.items.length; i++) {
                // bukus.push("<p>" +data.items.title +"</p>");
                print += '<th scope ="row">' + i + '</th> <td>' + data.items[i - 1].volumeInfo.title + '</td> <td>';
                for (var j = 0; j < data.items[i - 1].volumeInfo.authors.length; j++) {
                    print += data.items[i - 1].volumeInfo.authors[j];
                }
                print += '</td> <td>' + data.items[i - 1].volumeInfo.publisher + '</td> <td>' + data.items[i - 1].volumeInfo.publishedDate + '</td> <td>';

                print += ' <button id="button" type="button" class="btn btn-outline-light"><i id="star"class ="fa fa-star"></i></button> </td></tr>';

            }
            $('tbody').append(print);


        }
    });
    $(document).on('click', '#star', function () {
        if ($(this).hasClass('clicked')) {
            counter -= 1;
            $(this).removeClass('clicked');
        }
        else {
            $(this).addClass('clicked');
            counter = counter + 1;


        }
        $('.counters').html(counter);

    });

});

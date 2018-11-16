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
        document.getElementById("bintang").style.color = "rgb(39,60,80)";
        // document.getElementsByClassName("accordion").style.background = "#080b12";
    } else {
        document.body.style.background = "rgb(222,222,222)";
        document.body.style.color = "#384D54";
        document.body.style.fontFamily = "'Ropa Sans', Verdana, Tahoma";
        document.getElementById("bintang").style.color = "rgb(222, 222, 222)";
        // document.getElementsByClassName("accordion").style.background = "#eee";
    }
}

function search() {
    // Declare variables 
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("books");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


// var counter = 0;
// $(document).ready(function () {
//     $.ajax({
//         type: 'GET',
//         url: 'api/books',
//         dataType: 'json',
//         success: function (data) {
//             var print = '<tr>';
//             console.log(data.data[0].title);
//             for (var i = 1; i <= data.data.length; i++) {
//                 print += '<th scope ="row">' + i + '</th> <td>' + data.data[i - 1].title + '</td> <td>';
//                 print += data.data[i - 1].author;
//                 print += '</td> <td>' + data.data[i - 1].publishedDate + '</td> <td>';
//                 print += ' <button id="star" type="button" class="btn btn-outline-light"><i id="bintang" class ="fa fa-star"></i></button> </td></tr>';

//             }
//             $('tbody').append(print);
//         }
//     });
//     $(document).on('click', '#star', function () {
//         if ($(this).hasClass('clicked')) {
//             counter -= 1;
//             $(this).removeClass('clicked');
//             alert("It has been removed!")
//         }
//         else {
//             $(this).addClass('clicked');
//             counter = counter + 1;
//             alert("Book added to Favorite!")
//         }
//         $('.counters').html(counter);

//     });
// });

$(document).on('click', '#searchbutton', function () {
    $('tbody').empty();
    var search_result = $("#search").val();
    $.ajax({
        url: "{% url 'data' %}" + "?search=" + search_result,
        datatype: 'json',
        success: function (result) {
            console.log("ajia");
            var books_object = jQuery.parseJSON(result);
            renderHTML(books_object);
        }
    });
})

function renderHTML(data) {
    console.log("sabi");
    var books_list = data.items;
    for (var i = 0; i < books_list.length; i++) {
        var title = books_list[i].volumeInfo.title;
        var author = books_list[i].volumeInfo.authors[0];
        var published = books_list[i].volumeInfo.publishedDate;
        var temp = title.replace(/'/g, "\\'");
        var pagecount = books_list[i].volumeInfo.pageCount;
        var country = books_list[i].accessInfo.country;
        var table =
            '<tr class="table-books">' +
            '<td class = "nomor">' + (i + 1) + '</td>' +
            '<td class = "image">' + "<img src='" + data.items[i].volumeInfo.imageLinks.smallThumbnail + "'></img>" + "</td>" +
            '<td class="title">' + title + '</td>' +
            '<td class= "author">' + author + '</td>' +
            '<td class= "published">' + published + '</td>' +
            '<td class= "pagecount">' + pagecount + '</td>' +
            '<td class= "country">' + country + '</td>' +
            '<td>' + '<button id ="star" class = "button"><i class="fa fa-star"></i></button>' + '</td>';
        $('tbody').append(table);
    }
}

var counter = 0;
$(function () {
    $(document).on('click', '#star', function () {
        if ($(this).hasClass('clicked')) {
            counter -= 1;
            console.log(counter);
            $(this).removeClass('clicked');
            $(this).css("color", "black");
            alert("you just removed one book hope u didnt regret it");

        } else {
            counter += 1;
            console.log(counter);
            $(this).addClass('clicked');
            $(this).css("color", "black");
            alert("book added hope u love it");
        }
        $('.count').html(counter);

    });
}); 

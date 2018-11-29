function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.disconnect();
    auth2.signOut().then(function () {
        alert('User signed out.');
    });
}
$(document).ready(function () {
    $("#myInput").on("keyup", function (e) {
        q = e.currentTarget.value.toLowerCase()
        console.log(q)

        $.ajax({
            url: "json/?q=" + q,
            datatype: 'json',
            success: function (data) {
                $('tbody').html('')
                var result = '<tr>';
                for (var i = 0; i < data.items.length; i++) {
                    result += "<th scope='row' class='align-middle text-center'>" + (i + 1) + "</th>" +
                        "<td><img class='img-fluid' style='width:22vh' src='" + data.items[i].volumeInfo.imageLinks.smallThumbnail + "'></img>" + "</td>" +
                        "<td class='align-middle'>" + data.items[i].volumeInfo.title + "</td>" +
                        "<td class='align-middle'>" + data.items[i].volumeInfo.authors + "</td>" +
                        "<td class='align-middle'>" + data.items[i].volumeInfo.publisher + "</td>" +
                        "<td class='align-middle'>" + data.items[i].volumeInfo.publishedDate + "</td>" +
                        "<td class='align-middle' style='text-align:center'>" + "<img id='bintang" + i + "' onclick='favorite(this.id)' width='28px' src='https://image.flaticon.com/icons/svg/149/149222.svg'>" + "</td></tr>";
                }
                $('tbody').append(result);
                // checkLike();
            },
            error: function (error) {
                $('#alert').html('')
                var result = "Server error :(";
                $('#alert').append(result);
            }
        })
    });
});

var counter = 0;
function checkLike() {
    $.ajax({
        type: 'GET',
        url: '/lab11/book-list/get-like/',
        dataType: 'json',
        success: function (data) {
            for (var i = 1; i <= data.message.length; i++) {
                console.log(data.message[i]);
                var id = data.message[i - 1];
                var td = document.getElementsByName(id)[0];
                if (typeof td !== 'undefined') {
                    td.className = 'fas fa-star clicked';
                    td.style.color = 'red';
                }
                $('.count').html(data.message.length);
            }
            $('tbody').html(print);
        }
    });
};

function favorite(id) {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    var ini = $(this);
    var yellowstar = 'https://image.flaticon.com/icons/svg/291/291205.svg';
    var blankstar = 'https://image.flaticon.com/icons/svg/149/149222.svg';
    if (ini.hasClass('checked')) {
        $.ajax({
            url: "/lab11/book-list/unlike/",
            type: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
            },
            data: {
                id: id,
            },
            success: function (result) {
                counter = result.message;
                ini.removeClass('checked');
                $("#id").attr('src', blankstar);
                // ini.css("color","rgba(150,150,150,0.5);");
                $('#counter').html(counter);
            },
            error: function (errmsg) {
                alert("Something is wrong");
            }
        });
    } else {
        $.ajax({
            url: "/lab11/book-list/like/",
            type: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
            },
            data: {
                id: id,
            },
            success: function (result) {
                console.log('tolong');
                counter = result.message;
                ini.addClass('checked');
                $("#id").attr('src', yellowstar);
                // ini.css("color","yellow");
                $('#counter').html(counter);

            },
            error: function (errmsg) {
                alert("Something is wrong");
            }
        });
    }
}

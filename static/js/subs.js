$(document).ready(function () {
    $('#submit_subscribe').prop('disabled', true);
    $('#form_nama').hide();
    $('#form_email').hide();
    $('#form_email2').hide();
    $('#form_password').hide();
    $('#nama').val("");
    $('#email').val("");
    $('#password').val("");
    var flag = [false, false, false, false] //index 0 untuk nama, index 1 untuk email, index 2 untuk password, dan index 3 untuk email exist
    $('#nama').on('input', function () {
        var input = $(this); //ambil elemen dengan id nama
        check(input, 0);
        checkButton();
    });

    var timer = null;
    $('#email').keydown(function () {
        clearTimeout(timer);
        timer = setTimeout(function () {
            var input = $("#email"); //ambil elemen dengan id email
            check(input, 1);
            checkButton();
        }, 1000)
    });

    $('#password').on('input', function () {
        var input = $(this); //ambil elemen dengan id password
        check(input, 2);
        checkButton();
    });

    var check = function (input, arr) {
        if (arr === 1) { //jika email
            var reg = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/; //cek email
            var is_elemen = reg.test(input.val()); // jika benar is_elemen bernilai true
            if (is_elemen) {
                $('#form_email').hide();
                checkEmail(input.val()); // ambil isi data form
                flag[arr] = true;
                return
            } else {
                $('#form_email2').hide();
            }
        } else {
            var is_elemen = input.val();
        }
        if (is_elemen) { //kalau data nya ada
            if (arr === 0) {
                $('#form_nama').hide();
            } else if (arr === 1) {
                $('#form_email').hide();
            } else {
                $('#form_password').hide();
            }
            flag[arr] = true;
        } else {
            if (arr === 0) {
                $('#form_nama').show();
            } else if (arr === 1) {
                $('#form_email').show();
            } else {
                $('#form_password').show();
            }
            flag[arr] = false;
        }
    };

    var checkEmail = function (email) {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            method: "POST",
            url: "/Lab_10/checkEmail/",
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: {'email': email},
            success: function (response) { //response berupa boolean is_email_already_exist
                if (response.is_email) {
                    $('#form_email2').show();
                    flag[3] = false;
                    checkButton();
                } else {
                    $('#form_email2').hide();
                    flag[3] = true;
                    checkButton();
                }
            },
            error: function (error) {
                alert("Error, cannot get data from server")
            }
        })
    };

    var checkButton = function () {
        var button_subscribe = $('#submit_subscribe');
        for (var x = 0; x < flag.length; x++) {
            if (flag[x] === false) {
                button_subscribe.prop('disabled', true);
                return
            }
        }
        button_subscribe.prop('disabled', false);
    };

    $(function () {
        $('form').on('submit', function (e) {
            e.preventDefault(); //biar ga reload
            $.ajax({
                method: "POST",
                url: '/Lab_10/',
                data: $('form').serialize(),
                success: function (status) {
                    if (status.status_subscribe) {
                        var title1 = "<h1 align=\"center\" class=\"judul_utama_subscribe\"><strong> Thank you for subscribing! </strong></h1>";
                        var title2 = "<div align=\"center\" class=\"sub_judul_subscribe\"> Enjoy my website :)</div>";
                    } else {
                        var title1 = "<h1 align=\"center\" class=\"judul_utama_subscribe\"><strong> Sorry, something error! </strong></h1>";
                        var title2 = "<div align=\"center\" class=\"sub_judul_subscribe\"> Try again :(</div>";
                    }
                    $(".judul_utama_subscribe").replaceWith(title1);
                    $(".sub_judul_subscribe").replaceWith(title2);
                    for (var i = 0; i < flag.length; i++) {
                        flag[i] = false
                    }
                    $("#submit_subscribe").prop('disabled', true);
                    $('#nama').val("");
                    $('#email').val("");
                    $('#password').val("");

                },
                error: function (error) {
                    alert("Error, cannot connect to server")
                }
            });
        });
    });
    // UNSUBSCRIBE
    function validation() {
        $.ajax({
            url: '/checkEmail/',
            type: 'POST',
            data: {
                email: $('.email').val(),
                nama: $('.name').val(),
                password1: $('.password').val(),
            },

            success: function (response) {
                console.log(response.message)
                if (response.message == "User Valid") {
                    $('#validate').html("<div class='alert-box alert radius' data-alert><a href='#' class='close text-success'>" + response.message + "</a></div>");
                    $('#response').html("");
                    $('#subs_button').prop('disabled', false)
                }
                else {
                    $('#validate').html("<div class='alert-box alert radius' data-alert><a href='#' class='close text-danger'>" + response.message + "</a></div>");
                    $('#subs_button').prop('disabled', true)
                }
            }
        })
    }
    $(document).on('click', '#subs_button', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/Lab_10/subscribe/',
            type: 'POST',
            data: $('form').serialize(),
            success: function (json) {
                $('.email').val('');
                $('.name').val('');
                $('.pass').val('');
                $('#subcsribe_form').val('');
                $('#response').html("<div class='alert-box alert radius' data-alert><a href='#' class='close'>Thanks for Subscribe Me</a></div>");

            },
            error: function (xhr, errmsg, err) {
                $('#response_msg').html("<div class='alert-box alert radius' data-alert><a href='#' class='close'>Error message &times;</a></div>");
            },
        });
    })

    $(document).ready(function () {
        $.ajax({
            url: '/Lab_10/get-subs-list/',
            method: 'GET',
            dataType: 'json',
            success: function (data) {
                $('#alert_subs').hide()
                console.log(data)
                if (data.results.length == 0) {
                    $('#alert_subs').show()
                    $('#alert_subs').append('<strong>Opps!</strong> Tidak ada Subscriber')
                }
                var print = "";
                for (var i = 0; i < data.results.length; i++) {
                    console.log(data.results[i].email)
                    print += '<a class="list-group-item clearfix" id="list_subscribe">'
                    print += data.results[i].email + " - " + data.results[i].nama
                    print += "<button type='submit' id='unsubs_button' class='btn btn-dark unsub'>Unsubscribe</button> </a>"
                }
                $("#subs-list").append(print)
                /*<input type="text" aria-label="First name" class="form-control" placeholder="Confirmation Password" id="pass_confirmation">*/
            },
        })
    })

    $(document).on('click', '.unsub', function () {
        e.preventDefault();
        $.ajax({
            url: '/Lab_10/get-subs-list/',
            method: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log(data)
                var my_text = prompt('Confirmation Password');
                console.log(my_text)
                for (var i = 0; i < data.results.length; i++) {
                    if (my_text == data.results[i].password) {
                        console.log("true")
                        unsubscribe(data.results[i]);
                    }
                }
            },
        })
    })

    function unsubscribe(data) {
        $.ajax({
            url: '/Lab_10/subscribe/delete/',
            method: 'POST',
            data: {
                'email': data.email,
            },
            success: function (data) {
                window.location.reload()
            }
        })
    }
});
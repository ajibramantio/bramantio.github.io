$(document).ready(function () {
    $("button").click(function () {
        $.ajax({
            url: "https://localhost:8000/static/js/drone.json",
            success: function (result) {
                console.log(result)
            }
        });
    });
});
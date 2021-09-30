$(document).ready(function(){

    // toggle side bar
    $("#btn").click(function() {
        $(".sidebar").toggleClass('active');
    });

    // load_data();
    function load_data(input) {
        $.ajax({
            url: "/ajaxlivesearch",
            method: "POST",
            // dataType: "json",
            // pass input as prepared dict., so we can use it at backend
            data: {query: input},
            success: function(data) {
                // replace #result html tag
                $("#result").html(data);
                // $("#result").append(data.htmlresponse);
            }
        });
    }

    $("#search").keyup(function() {
        // get the current value of this input - #search
        var search = $(this).val();
        // if search is not empty, we want to invoke load_data function
        if(search != "") {
            // pass the user search input as argument
            load_data(search);
        } else {
            load_data();
        }
    });

});
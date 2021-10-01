$(document).ready(function(){

    // toggle side bar
    $("#btn").click(function() {
        $(".sidebar").toggleClass('active');
    });

    // hover effect
    $("#search-icon").hover(function() {
        $(this).css({"background-color": "#fff", "color": "#1d1b31"})
    }, function() {
        $(this).css({"background-color": "#11101d", "color": "#fff"})
    })

    $(".sidebar ul li a").hover(function() {
        $(this).css({"background-color": "#fff", "color": "#11101d", "transition-duration": "0.3s"})
    }, function() {
        $(this).css({"background-color": "#11101d", "color": "#fff"})
    })

    // search feature
    function load_data(input) {
        $.ajax({
            url: "/ajaxlivesearch",
            method: "POST",
            // pass input as prepared dict., so we can use it at backend
            data: {query: input},
            success: function(data) {
                // replace #result html tag
                $("#result").html(data);
            }
        });
    }

    // get input for search feature
    $("#search").keyup(function() {
        // get the current value of this input - #search
        var search = $(this).val();
        // we want to invoke load_data function
        load_data(search)
    });

    // check which th was clicked
    $(".sort").click(function() {
        let str = $(this).attr("value");
        $("#table-content").fadeToggle("fast", function() {
            $("#table-content").slideDown();
        });
        setTimeout(getSort(str), 10000)
    });

    // sorting the table
    const getSort = str => {
        // console.log(str)
        $.ajax({
            url: "/livetablesort",
            method: "POST",
            // pass input as prepared dict., so we can use it at backend
            data: {query: str},
            success: function(data) {
                // replace #result html tag
                // console.log(data)
                $("#table-content").html(data);
            }
        });
    }
});
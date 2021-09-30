$(document).ready(function(){

    // toggle side bar
    $("#btn").click(function() {
        $(".sidebar").toggleClass('active');
    });

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
        $("#table-content").fadeToggle("slow", function() {
            $("#table-content").slideDown();
        });
        getSort(str)
    });

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

    // $("#graph").click(function() {
    //     jQuery.get("/analytics", function(data) {
    //         // console.log(data)
    //         // let x = data[0]
    //         // let y = data[1]
    //         // console.log(x)
    //         // console.log(y)
    //         // for(let i = 0; i < x.length; i ++) {
    //         //     console.log(x[i])
    //         // }
    //         var xy = JSON.parse(data);
    //         console.log(xy)
    //     })
    // })

    $("#graph").click(function() {
        fetch('/analytics')
            .then(response => response.json())
            // pass the data and call showData function (to retrive individual pokemon)
            .then(data => console.log(data))
    })
});


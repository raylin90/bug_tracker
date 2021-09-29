$(document).ready(function(){

    // toggle side bar
    $("#btn").click(function() {
        $(".sidebar").toggleClass('active');
    });

    load_data();
    function load_data(query) {
        $.ajax({
            url: "/ajaxlivesearch",
            method: "POST",
            data: {query: query},
            success: function(data) {
                $("#result").html(data);
            }
        });
    }

    $("#search").keyup(function() {
        // var data = $("#searchForm").serilize();
        // print(data);
        var search = $(this).val();
        if(search != "") {
            load_data(search);
        } else {
            load_data();
        }
    });
});
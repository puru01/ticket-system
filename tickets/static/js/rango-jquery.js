$(document).ready(function(){


});
$('.apireq').click( function() {
    $.ajax({
             url : "http://localhost:8000/ticketapi",
             dataType: "json",
             success : function (data) {
             		$('#name').text( data[0].name);
             		$('#category').text( data[0].name);
             		$('#tid').text( data[0].tid);
                    }
                 });
             });
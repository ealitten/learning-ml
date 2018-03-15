
$( document ).ready(function() {

  $("#pk1").change(onPidChange);
  $("#pk2").change(onPidChange);
  $(".battle").click(fight);

  function onPidChange() {
       var url = $("#fightForm").attr("p-details-url"); // get the url of the `pokemon_details` view
       var selectObj = $(this);
       var pid = selectObj.val();  // get the selected pokemon ID from the HTML input
       $.ajax({                       // initialize an AJAX request
           url: url,                    // set the url of the request (= localhost:8000/hr/ajax/pokemon_data/)
           data: {
           'pid': pid       // add the pokemon id to the GET parameters
       },
       success: function (data) {   // `data` is the return of the `pokemon_details` view function
       var divId = `#${selectObj.attr('name')}_details`;
       var imageId = `#${selectObj.attr('name')}_img`;
       var html = `<img src="https://storage.googleapis.com/wepredictedthat-pokemon/pokemon-images/${pid}.png">`
       $(divId).html(data);  // replace the contents of the with the data that came from the server
       $(imageId).html(html)
      }
    })
  };

 function fight() {
   $.ajax({
       url: $(this).attr("p-details-url"),
       data:{
        'pk1_id':  $("#pk1").val(),
        'pk2_id':  $("#pk2").val()
      },
   success: function (result) {
     $('#results').html(result)
   }
 })
}
});

$(document).ready(function() {
    // inspired by http://jsfiddle.net/arunpjohny/564Lxosz/1/
    $('.table-responsive-stack').each(function (i) {
        var id = $(this).attr('id');
        //alert(id);
        $(this).find("th").each(function(i) {
            $('#'+id + ' td:nth-child(' + (i + 1) + ')').prepend('<span class="table-responsive-stack-thead">' + $(this).text() + ':</span> ');
            $('.table-responsive-stack-thead').hide();
        });
       
    });  
    
    $( '.table-responsive-stack' ).each(function() {
        var thCount = $(this).find("th").length; 
        var rowGrow = 100 / thCount + '%';
        //console.log(rowGrow);
        $(this).find("th, td").css('flex-basis', rowGrow);   
    });
      
    function flexTable(){
        if ($(window).width() < 768) {
            $(".table-responsive-stack").each(function (i) {
                $(this).find(".table-responsive-stack-thead").show();
                $(this).find('thead').hide();
            }); 
        // window is less than 768px   
        } else {
            $(".table-responsive-stack").each(function (i) {
                $(this).find(".table-responsive-stack-thead").hide();
                $(this).find('thead').show();
            });
       
        }
        // flextable   
    }      
  
    flexTable();
    
    window.onresize = function(event) {
        flexTable();
    };
    // document ready  
});


var btn = document.getElementById("btn");
// the counter
var counter = document.getElementById("btn-counter");
// set the counter to 0
counter.innerHTML = 0;

// increment the counter by 1 everytime the user clicks on the button
btn.onclick = function() {
    counter.innerHTML++;
};

 
 
 
 

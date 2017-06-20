$(function() {
	
    var th=$("#th");
    var tg = $( "#tgg" );
    var xx = $( "#xxx" );
	var sel = $("#select");
	
	$("#dialog-form2").hover(
	  function(){
		  $("#type2").css("visibility","visible");
	  },
	  function(){
		  $("#type2").css("visibility","hidden");
	  }
	  
	);
	
 
    $( "#dialog-form2" ).dialog({
      autoOpen: false,
      height: 550,
      width: 500,
      modal: true,
      buttons: {
        "插入题目": function() {
          var bValid = true;
		  var action=$("#type2");
		  console.log(xx.val());
		  var xs = xx.val().split("\n");
		  
		
		
		  $( this ).dialog( "close" );
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });
 
    
	
	
  });
  
  
  //对于第三个编辑的dialog（删除问题）的功能添加
  $(function() {
      
	
	
	  
	$("#dialog-form3").hover(
	 
	  function(){
		   console.log("dialog3-hover-in");
	  	  $("#type3").css("visibility","visible");
	  },
	  function(){
		  console.log("dialog3-hover-out");
	  	  $("#type3").css("visibility","hidden");
	  }
    ); 
 
    $( "#dialog-form3" ).dialog({
      autoOpen: false,
      height: 450,
      width: 400,
      modal: true,
      buttons: {
        "确定要删除吗": function() {
          var bValid = true;
		  var action=$("#type3");
		  console.log(xx.val());
		  
		  $( this ).dialog( "close" );
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });
	
	
	
   
   });

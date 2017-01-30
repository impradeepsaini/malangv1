



$(document).ready(

	function(){
	
		$(document).on("click",".add-button",function(){

		var link 	=	$(this).siblings("a");
		console.log(link.text());

		var youtubeId = link.attr("href")

    	//then get everything after the found index
    	var strOut = youtubeId.substr(32);

		title = link.text();


		$.ajax({

			method:"POST",
			url:"http://localhost:8000/add/",
			
			dataType:"jsonp",
			data:{"youtubeId":strOut,"title":title},
			success:function(data,textStatus,request){


				alert("successfully stored");


			},
			error:function(e){


				alert("there is a problem"+e);


			}


		});


 		});

 	});
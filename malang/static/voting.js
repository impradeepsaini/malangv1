$(document).ready(function() {

    getTopJson();

});




function getTopJson() {


    $.ajax({
        url: '/test/',

        success: function(data) {

            handleRequestJson(data);

        },

        error: function(data) {
            alert("error in getting data from server");
        }
    });

}


function handleRequestJson(data) {


    $.each(data, function(index, value) {

        html_string = "<div id='" + data[index].id +

            "' class='col-xs-12 outer-request-container' style='margin-top:20px;'>" +



            `<div  class= 'col-xs-1 thumbnail-container' >
	    	
	    			<img src="http://img.youtube.com/vi/` +
            data[index].youtubeId

            +
            `/1.jpg"/>
	    		
	    	 
			    	</div>
	    	
	    	
	    	
	    			<div  class= 'col-xs-2 vote-container' >
		    	
		    		<div id='topic-` +

            data[index].id +

            "' data-id='" + data[index].id + "' class='upvote'>" +
            `<a class="upvote"></a>
	    			<span class="count"></span>
	    			<a class="downvote"></a>
	    			<a class="star"></a>
					</div>
		    	

		    		</div>


			    	<div  class='col-xs-9 request-container'>
			        
			        <br>    
			        	<h4 class="song-title">
			        
			        		<a href="#">` + data[index].song__name + `</a> 
			        		<span class="hidden-content" style="visibility:hidden">{{object.youtubeId}}</span>
			        		<span class="request-id" style="visibility:hidden">{{object.id}}</span>	
			        	</h4>     
			    	</div>
						
						
					

					</div>
					<br>
					<br>`;



        console.log(html_string);
        $('body').append(html_string);


        var div_string = 'div#topic-' + data[index].id;


        function booleanToInteger(x) {


            if (x == false || null) return 0;
            else if (x == true) return 1;


        }



        var callback = function(data) {


            $.ajax({
                url: '/vote/',
                type: 'post',
                data: {
                    id: data.id,
                    up: data.upvoted,
                    down: data.downvoted,
                    star: data.starred
                }
            });
        };


        $(div_string).upvote({
            count: data[index].offset,
            upvoted: booleanToInteger(data[index].voterecord__upvoted),
            downvoted: booleanToInteger(data[index].voterecord__downvoted),
            callback: callback
        });

    });


}
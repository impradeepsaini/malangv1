$(document).ready(

    function() {


        $(document).on({
            ajaxStart: function() {
                $('body').addClass("loading");
            },
            ajaxStop: function() {
                $('body').removeClass("loading");
            }
        });

        $(".y-searchbox").autocomplete({


            source: function(request, response) {



                $.ajax({



                    url: "http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q=" + request.term + "&key=" + "AIzaSyBUjqwJuIEWUPJce2MGLC61F-DFvK1l8Cc" + "&format=5&alt=json&callback=?",
                    dataType: 'jsonp',
                    success: function(data, textStatus, request) {
                        response($.map(data[1], function(item) {
                            return {
                                label: item[0],
                                value: item[0]
                            }
                        }));
                    }
                });

            }

        });



        $("#search-button").click(function() {


            var val = $(".y-searchbox").val();

            $.ajax({


                url: "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + val + "&key=AIzaSyBUjqwJuIEWUPJce2MGLC61F-DFvK1l8Cc",
                dataType: 'jsonp',
                success: function(data, textStatus, request) {


                    if (data.items) {

                        $("#sonuc").empty();

                        $.each(data.items, function(i, x) {


                            // $("div").html("https://www.youtube.com/watch?v="+x.id.videoId);

                            $("#sonuc").append(
                                "<li style='list-style-type:none;'><br><img src=" +
                                "'" +
                                x.snippet.thumbnails.default.url +
                                "'" +
                                "width='100px' height='100px'/><a style='text-decoration:none;word-wrap:break-word;' href='https://www.youtube.com/watch?v=" +
                                x.id.videoId +
                                "'" +
                                "><p style='word-wrap: break-word;'>" +
                                x.snippet.title +
                                "</p><br></a><input type='button' value='add' class='add-button'></li><br>");


                        });

                    }

                }



            });


        });



    });
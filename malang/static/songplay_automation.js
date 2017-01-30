var tobedeleted;


var test = false;


$('.upvote').upvote();


$(document).ready(
    function() {


        // $('.upvote').upvote();

        //voting methods

        getajaxdata(handleYoutubeUrl);

        function getajaxdata() {

            var new_url;

            $.ajax({
                url: "/index/",
                type: "post",

                cache: 'false',

                success: function(data) {

                    handleYoutubeUrl(data);

                },

                error: function(data) {
                    alert("error in getting data from server");
                }
            });

        };



        //handles the ajax data recieved 

        function handleYoutubeUrl(data) {

            var nextsong_id = data[0].nextsong_pk;
            tobedeleted = data[0].nextsong_pk;
            var nextsong_yid = data[0].nextsong_yid;
            // var song_youtubeid = $("div.outer-request-container > div.request-container").
            // find("span.request-id").filter(

            //     function() {

            //         return $(this).text() === String(nextsong_id);

            //     }).siblings("span").text();

            new_url = "https://www.youtube.com/embed/" + nextsong_yid + "?enablejsapi=1";

            if (test === false) {
                $("#myframe").attr("src", new_url);
                test = true;

            } else {
                $("#urlplaceholder").attr("href", new_url);
                player.loadVideoByUrl(getUrl());

            }

            $("#" + nextsong_id + "> .request-container .song-title a").css("color", "red");



        }


        function deleteprevious() {


            $("#" + tobedeleted).hide();

        }

        function getUrl() {

            return $("#urlplaceholder").attr("href");

        }

    });
// function setUrl(url){

//   console.log(url);
//   $("#myframe").attr("src", url);
// }



// }
// $('.upvote').upvote();



var tobedeleted;


var test = false;


// parseInt($(this).attr("id").substr(6))


$(document).ready(
    function() {
        //ajax call to send vote status in backend
        getajaxdata(handleYoutubeUrl);



    });


//get next highest upvoted song from backend
function getajaxdata() {

    // var new_url;

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


        console.log(new_url);
        $("#urlplaceholder").attr("href", new_url);
        player.loadVideoByUrl(getUrl());

    }

    $("#" + nextsong_id + "> .request-container .song-title a").css("color", "red");



}





// function deleteprevious() {


//     $("#" + tobedeleted).hide();

// }

function getUrl() {

    console.log($("#urlplaceholder").attr("href"));
    return $("#urlplaceholder").attr("href");

}








// function setUrl(url){

//   console.log(url);
//   $("#myframe").attr("src", url);
// }



// }
// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;

function onYouTubeIframeAPIReady() {


  player = new YT.Player('myframe', {


    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });

  // setUrl(getUrl()); 

}



// 4. The API will call this function when the video player is ready
function onPlayerReady(event) {

  //  setUrl(getUrl());
  event.target.playVideo();
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.


function onPlayerStateChange(event) {



  if (event.data === 0) {

    // deleteprevious();
    getajaxdata();

  }



}
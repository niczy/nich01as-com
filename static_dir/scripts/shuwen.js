var player;
function onYouTubePlayerAPIReady() {
  console.log("Youtube ready");
  player = new YT.Player('player');
}

$(function() {
  var video_visable = false;
  $('#show_video').click(
        function() {
          $('#show_video').hide();
          console.log('clicked');
          $('.video_dialog').fadeIn('slow', function() {
            video_visable = true;
            player.playVideo();
          })
        }
      );
  $('body').click(
      function() {
        if (video_visable) {
          $('.video_dialog').fadeOut('slow', function() {
            video_visable = false;
            player.stopVideo();
            $('#show_video').show();
          });
        }
      }
    )
  $('.video_dialog').keypress(function(e){
    console.log('key pressed');
    $('.video_dialog').fadeOut('slow', function() {
          video_visable = false;
          player.stopVideo();
      });
  });
});


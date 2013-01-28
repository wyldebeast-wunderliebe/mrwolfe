/* TTS js */


$(document).ready(function() {

    // Setup AJAX calls for CSRF
    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
          function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
              for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
                }
              }
            }
            return cookieValue;
          }
          
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        } 
      });

    $(document).on("click", "#MyModal .cancel", function(e) {
        $('#MyModal').modal('hide');
        e.preventDefault();
        e.stopPropagation();
      })
  });

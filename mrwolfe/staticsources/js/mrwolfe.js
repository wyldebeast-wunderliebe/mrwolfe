/* Mr.Wolfe JS lib */

var mrwolfe = {};

mrwolfe.refreshHistory = function(issue_id) {

  $.get("/issue_history/" + issue_id,
        function(data) {
          $("#history").replaceWith(data);
        });
};


/**
 * Expand viewlet after add and remove any alerts.
 * @param sender Originating element of action
 */
mrwolfe.afterAdd = function(sender) {

  sender.parents(".viewlet").find(".toggle.expand").click();
  sender.parents(".viewlet").find(".alert").hide();
};


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

      $("body").on("click", ".toggle", function(e) {
          $(e.target).parents(".viewlet").toggleClass("expanded");
          $(e.target).parents("h2").nextAll().toggle("slow");

          e.preventDefault();
        });

    // Set calendar defaults
    $.datepicker.setDefaults({dateFormat: "dd-mm-yy"});

    $("input.date").datepicker();
    
    // init datepickers in modal
    $(document).on("show", "#MyModal", function(e) {
        $("#MyModal").find("input.date").datepicker();
      });
  });

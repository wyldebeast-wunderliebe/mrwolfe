/* Mr.Wolfe JS lib */

var mrwolfe = {};


mrwolfe.showMessage = function(mesg, type) {

  $("body").append('<div id="message" class="alert alert-' + type + '"><a class="close" data-dismiss="alert">&times;</a>' + mesg + '</div>');
  
  setTimeout('$("#message").hide("slow")', 5000);
  
  $("#message").alert();
};

mrwolfe.refreshHistory = function(issue_id) {

  $.get("/issue_history/" + issue_id,
        function(data) {
          $("#history-viewlet").replaceWith(data);
        });
};


/**
 * Expand viewlet after add and remove any alerts.
 * @param sender Originating element of action
 */
mrwolfe.afterAdd = function(sender) {

  if (!sender.parents(".viewlet").hasClass("expanded")) {
    sender.parents(".viewlet").find(".toggle.expand").click();
  }

  sender.parents(".viewlet").find(".alert").hide();
};


/**
 * Initialize file uploader widget.
 */
mrwolfe.init_fileuploader = function(options) {

  var defaults = {
    url: '/fileupload',
    dataType: 'json',

    start: function(e) {
      $($(e.target).data("progress")).show();
    },
    done: function (e, data) {

      var tgt = $(e.target);

      $(tgt.data("target")).append(data.result.html);
      $(tgt.data("progress") + " .bar").css("width", "100%");
      $(tgt.data("progress")).hide("slow");
    },
    progress: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      $($(e.target).data("progress") + " .bar").css("width", progress + "%");
    }
  };

  if (options) {
    $.extend(defaults, options);
  }

  $("input[type='file']").each(function() {
    defaults['formData'] = {"issue_id": $(this).data("issueid")};
    $(this).fileupload(defaults);
  });
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

    var tgt = $(e.currentTarget);

    tgt.parents(".viewlet").toggleClass("expanded");
    $(tgt.attr("href")).toggle("slow");

    e.preventDefault();
  });

  // Set calendar defaults
  $.datepicker.setDefaults({dateFormat: "dd-mm-yy"});

  $("input.date").datepicker();

  // Make sure to clean up modal after use...
  $('.modal').on('hide', function () {
    $(this).removeData('modal');
  });

  $(document).on("click", ".create-status", function(e) {

    var link = $(e.currentTarget);

    e.preventDefault();

    $.get(link.attr("href"), function(data) {

      $("#modalcontainer").html(data);
      $("#modalcontainer .modal").modal('show');
    });

    $(document).on("submit", "form.create-inline", function(e) {

      var form = $(e.currentTarget);

      e.preventDefault();

      $.post(form.attr("action"), form.serialize(), function(data) {

        $("#modalcontainer .modal").modal('hide');

        $("#status").replaceWith(data);
      });

    });

  });

  /**
   * Handle inline a clicks.
   */
  $(document).on("click", "a.inline", function(e) {

    e.preventDefault();

    var link = $(e.currentTarget);
    var tgt = link;
    var behavior = link.data('targetbehavior') || "replace";

    if (link.attr("target")) {
      tgt = $(link.attr("target"));
    }

    $.ajax(link.attr("href"),
           {type: link.data('method') || "GET",
            success: function(data, status, xhr) {

              if (xhr.getResponseHeader("content-type").indexOf("json") > -1) {
                mrwolfe.showMessage(data.message, "success");
              } else {
                if (behavior == "replace") {
                  tgt.replaceWith(data);
                } else if (behavior == "append") {
                  tgt.append(data);
                }
              }
            }
           });
  });

  /**
   * Handle inline a clicks.
   */
  $(document).on("submit", "form.inline", function(e) {

    e.preventDefault();

    var form = $(e.target);
    var tgt = form;
    var behavior = form.data('targetbehavior') || "replace";

    if (form.attr("target")) {
      tgt = $(form.attr("target"));
    }

    $.ajax(form.attr("action"),
           {type: form.attr('method') || "POST",
            data: form.serialize(),
            success: function(data, status, xhr) {

              if (xhr.getResponseHeader("content-type").indexOf("json") > -1) {
                mrwolfe.showMessage(data.message, "success");
              } else {
                if (behavior == "replace") {
                  tgt.replaceWith(data);
                } else if (behavior == "append") {
                  tgt.append(data);
                }
              }
            }
           });
  });

  mrwolfe.init_fileuploader();
});

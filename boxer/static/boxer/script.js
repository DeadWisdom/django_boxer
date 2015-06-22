function openMessage(message) {
    $('.message').not(message).removeClass('open');
    message.addClass('open');
};

function deleteMessage(id) {
    var msg = $('#email-' + id);
    $.ajax({
        url: window.BASE_HREF + 'delete/',
        type: 'POST',
        data: {'id': id},
        headers: {'X-CSRFToken': CSRF_TOKEN},
        success: function() {
           msg.remove();
           if ( $('.message').length == 0 ) {
                $("<em>No emails yet.</em>").appendTo($('article'));
           }
        },
        error: function() {
            alert("Server error, delete failed.");
            msg.fadeIn();
        }
    });
    msg.fadeOut();
}

$(document).on('click', function(e) {
    if (e.target.tagName == 'A') return;
    var msg = $(e.target).closest('.message');
    if (msg.length) {
        openMessage(msg);
    } else {
        $('.message').removeClass('open');
    }
});


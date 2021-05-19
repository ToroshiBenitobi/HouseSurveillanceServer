$(document).ready(function () {
    $("#message-form").submit(handleFormSubmit);
    $("#message-container").empty();
    $("#sent-result").hide();
    $("#sent-fail").hide();
    getMessages();
});


/**
 * Handle submission of the form.
 */
function handleFormSubmit(evt) {
    evt.preventDefault();

    var textArea = $("#message");
    var msg = textArea.val();

    console.log("handleFormSubmit: ", msg);
    addMessage(msg);
    // Reset the message container to be empty
    textArea.val("");
}


/**
 * Makes AJAX call to the server and the message to it.
 */
function addMessage(msg) {
    $.post(
        "/message/wall/add",
        {'m': msg},
        function (data) {
            console.log("addMessage: ", data);
            displayResultStatus(data.result);
            msg = data.message
            if (msg) {
                showAddedMessages(msg);}
        }
    );
}
$(document).ready(function () {
    $("#class-form").submit(handleFormSubmit);
    $("#inputDay").val('');
    $("#inputTime").val('');
});


/**
 * Handle submission of the form.
 */
function handleFormSubmit(evt) {
    evt.preventDefault();
    var inputDay = $("#inputDay");
    var inputTime = $("#inputTime");
    var inputClassName = $("#inputClassName");
    var inputTeacher = $("#inputTeacher");
    var inputWeek = $("#inputWeek");
    var inputLocation = $("#inputLocation");

    var text = '<b>' + inputClassName.val() + '</b><br>' + inputTeacher.val() + '<br>' + inputWeek.val() + '周 ， ' + inputLocation.val() + '<br>';
    console.log(inputDay.val());
    console.log(inputTime.val());
    console.log(text);
    // addMessage(msg);
    // Reset the message container to be empty
    inputClassName.val('');
    inputTeacher.val('');
    inputWeek.val('');
    inputLocation.val('');
    inputDay.val('');
    inputTime.val('');
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
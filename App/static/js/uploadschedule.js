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
    var day = inputDay.val();
    var time = inputTime.val();
    var classTime = '';
    if (time === '1-2节') {
        classTime += 'c1-';
    } else if (time === '3-4节') {
        classTime += 'c2-';
    } else if (time === '5-6节') {
        classTime += 'c3-';
    } else if (time === '7-8节') {
        classTime += 'c4-';
    } else if (time === '9-10节') {
        classTime += 'c5-';
    } else {
        return;
    }

    if (day === '星期一') {
        classTime += '1';
    } else if (day === '星期二') {
        classTime += '2';
    } else if (day === '星期三') {
        classTime += '3';
    } else if (day === '星期四') {
        classTime += '4';
    } else if (day === '星期五') {
        classTime += '5';
    } else {
        return;
    }
    console.log(classTime);
    console.log(text);
    addCourse(msg);
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
function addCourse(classTime, text) {
    $.post(
        "/myinfo/uploadschedule",
        {'time': classTime, 'text': text},
        function (data) {
            console.log('Successfully add course.');

        }
    );
}
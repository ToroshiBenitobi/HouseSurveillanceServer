var buttonRecord = document.getElementById("record");
var buttonStop = document.getElementById("stop");
var msg = document.getElementById("msg");

buttonStop.disabled = true;

buttonRecord.onclick = function () {
    // var url = window.location.href + "record_status";
    buttonRecord.disabled = true;
    buttonStop.disabled = false;
    // 禁用下载链接
    var downloadLink = document.getElementById("download");
    downloadLink.text = "";
    downloadLink.href = "";

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);
            msg.textContent = result.result;
            print('record start');
        }
    }
    xhr.open("POST", "/surveillance/recordstatus");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({status: "true"}));

};

buttonStop.onclick = function () {
    buttonRecord.disabled = false;
    buttonStop.disabled = true;

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);
            msg.textContent = result.result;
            print('record end');
            // set download link
            var downloadLink = document.getElementById("download");
            downloadLink.text = "Download";
            downloadLink.href = result.save_path;
        }
    }
    xhr.open("POST", "/surveillance/recordstatus");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({status: "false"}));
};


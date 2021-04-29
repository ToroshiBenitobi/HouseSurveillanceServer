var buttonRecord = document.getElementById("record");
var buttonStop = document.getElementById("stop");

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
            var msg = document.getElementById("msg");
            var result = JSON.parse(xhr.responseText);
            msg.textContent = result['result'];
            console.log('start recording');
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
            var msg = document.getElementById("msg");
            var result = JSON.parse(xhr.responseText);
            msg.innerText = result['result'];
            // set download link
            var downloadLink = document.getElementById("download");
            downloadLink.text = "Download";
            downloadLink.href = result['save_path'];
            console.log('end recording');
        }
    }
    xhr.open("POST", "/surveillance/recordstatus");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({status: "false"}));
};


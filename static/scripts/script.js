// Reroll function
function rerollPost() {
    const rerollBtn = document.getElementById("reroll-btn");
    const rerollBtnSpan = document.getElementById("reroll-btn-span");
    rerollBtn.disabled = true;

    // for reducing spamming of reroll btn
    var timeOut = 3; // seconds
    rerollBtnSpan.innerHTML=`Reroll in ${timeOut}`;
    const timeOutId = setInterval(()=>{
        if (timeOut>0) {
            --timeOut;
            rerollBtnSpan.innerHTML=`Reroll in ${timeOut}`;
        } else {
            rerollBtn.disabled = false;
            rerollBtnSpan.innerHTML=`Reroll`;
            clearInterval(timeOutId);
        }
    }, 1000);
    
    // xhr code for posting data to the api at '/reroll/'
    var xhr = new XMLHttpRequest();
    const spanElement = document.getElementById("output-url-span");
    const json = {
        shortLink : spanElement.innerHTML
    }
    
    xhr.open("POST", "/reroll/", true);

    // Set the request header to indicate the content type as JSON
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const newShortLink = JSON.parse(xhr.responseText)["newShortLink"];
            spanElement.innerHTML = newShortLink;
        }
    };
    xhr.send(JSON.stringify(json));
    
}

function copyTextToClipboard() {
    const copyBtnSpan = document.getElementById("copy-btn-span");
    const text = protocolHostPortText + document.getElementById("output-url-span").innerText;
    if (document.hasFocus()) {
        navigator.clipboard.writeText(text).then(() => {
            copyBtnSpan.innerHTML="Copied!";
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
        timeOutId = setTimeout(()=>{
            copyBtnSpan.innerHTML="Copy"
            clearTimeout(timeOutId);
        }, 2000); // 2 second
    } else {
        console.error('Failed to copy text: Document is not focused.');
    }
}

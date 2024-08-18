// Reroll function
function rerollPost() {
    const rerollBtn = document.getElementById("reroll-btn");
    rerollBtn.disabled = true;

    var xhr = new XMLHttpRequest();
    const spanElement = document.getElementById("output-url-span");
    const json = {
        shortLink : spanElement.innerHTML
    }
    
    xhr.open("POST", "/reroll/", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const newShortLink = JSON.parse(xhr.responseText)["newShortLink"];
            spanElement.innerHTML = newShortLink;
        }
    };
    xhr.send(JSON.stringify(json));

    // for reducing spamming of reroll btn
    timeOutId = setTimeout(()=>{
        rerollBtn.disabled = false;
        clearTimeout(timeOutId);
    }, 2000); // 2 seconds
}
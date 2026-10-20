const copyBtn = document.querySelector('.copy-btn');
const copyText = copyBtn.querySelector("span");
const copyIcon = copyBtn.querySelector('.copy-icon');
const curlCmd = document.getElementById("curl-cmd");

copyBtn.addEventListener("click", async () => {
    await navigator.clipboard.writeText(curlCmd.innerText);
    copyText.innerText = "Copied!";
    copyIcon.src = "/static/copy-check.svg";
    copyBtn.classList.add("copied");

    setTimeout(() => {
        copyText.innerText = "Copy";
        copyIcon.src = "/static/copy.svg";
        copyBtn.classList.remove("copied");
    }, 1500);
});
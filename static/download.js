const copyBtn = document.querySelector(".copy-btn");
const downloadBtn = document.querySelector(".download-btn");

const copyIcon = copyBtn.querySelector('.copy-icon');
const copyText = copyBtn.querySelector('.copy');

copyBtn.addEventListener('click', async() => {
    const command = `curl -C - -O -L "${downloadBtn.href}"`;

    await navigator.clipboard.writeText(command);
    copyIcon.src = '/static/icons/copied.svg';
    copyText.textContent = 'Command copied!';
    copyBtn.classList.add('copied');

    setTimeout(() => {
        copyIcon.src = '/static/icons/copy.svg';
        copyText.textContent = 'Copy command for terminal';
        copyBtn.classList.remove('copied');
    }, 2000);
})
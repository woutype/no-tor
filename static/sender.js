const webInput = document.getElementById('web');
const webBtn = document.getElementById('web-btn');
const webIcon = document.getElementById('web-icon');
const webText = document.getElementById('web-text');

webBtn.addEventListener('click', async () => {
    await navigator.clipboard.writeText(webInput.value);
    webIcon.src = '/static/icons/copied.svg';
    webText.textContent = 'Copied!';
    webBtn.classList.add('copied');

    setTimeout(() => {
        webIcon.src = '/static/icons/copy.svg';
        webText.textContent = 'Copy';
        webBtn.classList.remove('copied');
    }, 2000);
});

const terminalInput = document.getElementById('terminal');
const terminalBtn = document.getElementById('terminal-btn');
const terminalIcon = document.getElementById('terminal-icon');
const terminalText = document.getElementById('terminal-text');

terminalBtn.addEventListener('click', async () => {
    await navigator.clipboard.writeText(terminalInput.value);
    terminalIcon.src = '/static/icons/copied.svg';
    terminalText.textContent = 'Copied!';
    terminalBtn.classList.add('copied');

    setTimeout(() => {
        terminalIcon.src = '/static/icons/copy.svg';
        terminalText.textContent = 'Copy';
        terminalBtn.classList.remove('copied');
    }, 2000);
});
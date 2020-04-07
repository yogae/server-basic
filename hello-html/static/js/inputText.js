const inputTexts = document.getElementsByTagName("input");
const inputButtons = document.getElementsByTagName("button");
const textListDiv = document.getElementById('textList');

const inputText = inputTexts[0];
const inputButton = inputButtons[0];

inputButton.addEventListener('click', () => {
    const p = document.createElement("p");
    p.textContent = inputText.value;
    textListDiv.appendChild(p);
    inputText.value = "";
});
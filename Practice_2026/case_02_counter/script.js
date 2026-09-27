const display = document.getElementById("display");
const increaseControl = document.getElementById("increaseControl");
const decreaseControl = document.getElementById("decreaseControl");
const limitNotice = document.getElementById("limitNotice");

let currentCount = 0;

function renderCounter() {
    display.textContent = currentCount;
    display.classList.remove("positive", "negative", "zero");

    if (currentCount > 0) {
        display.classList.add("positive");
    } else if (currentCount < 0) {
        display.classList.add("negative");
    } else {
        display.classList.add("zero");
    }

    increaseControl.disabled = currentCount >= 10;
    decreaseControl.disabled = currentCount <= -10;

    if (currentCount === 10 || currentCount === -10) {
        limitNotice.textContent = "Вы достигли экстремального значения";
    } else {
        limitNotice.textContent = "";
    }
}

increaseControl.addEventListener("click", () => {
    if (currentCount < 10) {
        currentCount += 1;
        renderCounter();
    }
});

decreaseControl.addEventListener("click", () => {
    if (currentCount > -10) {
        currentCount -= 1;
        renderCounter();
    }
});

renderCounter();

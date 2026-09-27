const leftField = document.getElementById("leftField");
const rightField = document.getElementById("rightField");
const output = document.getElementById("output");
const operationControls = document.querySelectorAll("[data-operation]");

function addValues(a, b) { return a + b; }
function subtractValues(a, b) { return a - b; }
function multiplyValues(a, b) { return a * b; }

function divideValues(a, b) {
    if (b === 0) {
        throw new Error("Деление на ноль невозможно.");
    }
    return a / b;
}

function normalizeDecimal(value) {
    return value.trim().replace(",", ".");
}

function parseOperands() {
    const leftText = normalizeDecimal(leftField.value);
    const rightText = normalizeDecimal(rightField.value);

    if (leftText === "" || rightText === "") {
        throw new Error("Введите два числа.");
    }

    const leftOperand = Number(leftText);
    const rightOperand = Number(rightText);

    if (!Number.isFinite(leftOperand) || !Number.isFinite(rightOperand)) {
        throw new Error("Ошибка: в поля необходимо вводить числа.");
    }

    return [leftOperand, rightOperand];
}

function renderAnswer(value) {
    const roundedAnswer = Number(value.toFixed(10));

    output.classList.remove("error");
    output.textContent = `Результат: ${roundedAnswer}`;
}

function renderFailure(message) {
    output.classList.add("error");
    output.textContent = message;
}

operationControls.forEach((button) => {
    button.addEventListener("click", () => {
        try {
            const [leftOperand, rightOperand] = parseOperands();
            const operation = button.dataset.operation;
            let calculation;

            if (operation === "addValues") calculation = addValues(leftOperand, rightOperand);
            else if (operation === "subtractValues") calculation = subtractValues(leftOperand, rightOperand);
            else if (operation === "multiplyValues") calculation = multiplyValues(leftOperand, rightOperand);
            else if (operation === "divideValues") calculation = divideValues(leftOperand, rightOperand);

            renderAnswer(calculation);
        } catch (error) {
            renderFailure(error.message);
        }
    });
});

const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
let currentInput = '';

// Number and operator buttons
buttons.forEach(button => {
    const value = button.getAttribute('data-value');
    if (value) {
        button.addEventListener('click', () => {
            currentInput += value;
            display.value = currentInput;
        });
    }
});

// Equal button
document.getElementById('equal').addEventListener('click', () => {
    try {
        display.value = eval(currentInput);
        currentInput = display.value;
    } catch {
        display.value = "Error";
        currentInput = '';
    }
});

// Clear button
document.getElementById('clear').addEventListener('click', () => {
    currentInput = '';
    display.value = '';
});

// Delete button
document.getElementById('delete').addEventListener('click', () => {
    currentInput = currentInput.slice(0, -1);
    display.value = currentInput;
});

async function calculate() {
    const expression = document.getElementById("calcInput").value;
    
    // Split the expression into numbers and operation
    const [num1, operation, num2] = expression.match(/(\d+)([+\-*/])(\d+)/);

    let result;

    if (operation === '+') {
        result = await eel.add(parseFloat(num1), parseFloat(num2))();
    } else if (operation === '-') {
        result = await eel.sub(parseFloat(num1), parseFloat(num2))();
    } else if (operation === '/') {
        result = await eel.div(parseFloat(num1), parseFloat(num2))();
    } else if (operation === '*') {
        result = await eel.mult(parseFloat(num1), parseFloat(num2))();
    } else {
        // Handle invalid operation (optional)
        result = "Invalid operation";
    }

    document.getElementById("result").textContent = `Result: ${result}`;
}

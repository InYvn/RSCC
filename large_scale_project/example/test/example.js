// This is a JavaScript sample file

/*
Multiline comment:
This class represents a simple calculator
*/
class Calculator {
    constructor() {
        this.result = 0;
    }

    // Addition method
    add(a, b) {
        return a + b;
    }

    // Subtraction method
    subtract(a, b) {
        return a - b;
    }
}

// Arrow function example
const multiply = (a, b) => {
    return a * b;
};

// Module export example
module.exports = {
    Calculator,
    multiply
};

// Main function example
function main() {
    const calc = new Calculator();
    const sum = calc.add(5, 3);
    const product = multiply(4, 5);

    console.log(`Sum: ${sum}, Product: ${product}`);
}

// Immediately Invoked Function Expression (IIFE)
(function() {
    console.log("This is an IIFE");
})();
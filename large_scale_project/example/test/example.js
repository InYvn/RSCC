// 这是一个JavaScript示例文件

/*
多行注释：
这个类表示一个简单的计算器
*/
class Calculator {
    constructor() {
        this.result = 0;
    }

    // 加法方法
    add(a, b) {
        return a + b;
    }

    // 减法方法
    subtract(a, b) {
        return a - b;
    }
}

// 箭头函数示例
const multiply = (a, b) => {
    return a * b;
};

// 模块导出示例
module.exports = {
    Calculator,
    multiply
};

// 主函数示例
function main() {
    const calc = new Calculator();
    const sum = calc.add(5, 3);
    const product = multiply(4, 5);

    console.log(`Sum: ${sum}, Product: ${product}`);
}

// 立即执行函数表达式 (IIFE)
(function() {
    console.log("This is an IIFE");
})();
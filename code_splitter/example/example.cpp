// 这是一个C++示例文件

/*
多行注释：
这个类表示一个简单的计算器
*/
class Calculator {
public:
    Calculator() {}
    ~Calculator() {}

    // 加法函数
    int add(int a, int b) {
        return a + b;
    }

    // 减法函数
    int subtract(int a, int b) {
        return a - b;
    }
};

// 主函数
int main() {
    Calculator calc;
    int sum = calc.add(5, 3);
    int difference = calc.subtract(10, 4);

    return 0;
}

// 另一个示例函数
void printMessage() {
    std::cout << "Hello, C++!" << std::endl;
}
// This is a C++ sample file

/*
Multiline comment:
This class represents a simple calculator
*/
class Calculator {
public:
    Calculator() {}
    ~Calculator() {}

    // Addition function
    int add(int a, int b) {
        return a + b;
    }

    // Subtraction function
    int subtract(int a, int b) {
        return a - b;
    }
};

// Main function
int main() {
    Calculator calc;
    int sum = calc.add(5, 3);
    int difference = calc.subtract(10, 4);

    return 0;
}

// Another example function
void printMessage() {
    std::cout << "Hello, C++!" << std::endl;
}
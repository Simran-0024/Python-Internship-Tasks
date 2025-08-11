## **Simple Calculator Program — Documentation**

### **Overview**

I have built a **command-line-based calculator** in Python that takes two numbers and an operator from the user, performs the chosen mathematical operation, and displays the result.
The program supports **addition**, **subtraction**, **multiplication**, and **division**, including decimal numbers.

---

### **Features**

1. **User-friendly input prompts** for first number, second number, and operator.
2. **Supports decimals** as well as integers by using `float()` for number conversion.
3. **Handles division by zero** with a clear error message.
4. **Handles invalid numeric inputs** using error handling.
5. **Handles invalid operators** and notifies the user if the operator is not supported.

---

### **How It Works**

1. **Input Phase**

   * The program asks the user to enter:

     * First number (`a`)
     * Second number (`b`)
     * Operator (`+`, `-`, `*`, `/`)
   * Numbers are taken as `float` so both integers and decimals can be processed.

2. **Processing Phase**

   * The program checks the entered operator.
   * Based on the operator, it performs:

     * `+` → Addition
     * `-` → Subtraction
     * `*` → Multiplication
     * `/` → Division (with zero-check)
   * If an unsupported operator is entered, it shows **"Invalid operator"**.

3. Error Handling**

   * Division by Zero:** Custom error message — "Cannot divide by zero".
   * Invalid Input: If non-numeric data is entered, it shows — "Please enter valid numeric values."

4. **Output Phase**

   * If a valid operation is performed, the result is displayed to the user.

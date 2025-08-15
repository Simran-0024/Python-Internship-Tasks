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
  





---------
---------


## **Number Guessing Game — Documentation**

This program is an interactive number guessing game where the computer randomly selects a number between 1 and 100, and the player attempts to guess it within a set number of chances. The game provides hints after each guess, allows early exit by typing `"exit"`, and displays a final message when the game ends.

**Working**

1. **Random Number Generation**

   * At the start of the game, the program generates a random integer between 1 and 100 using Python’s `random` module.
   * This number remains constant for the entire game until the player either guesses correctly or runs out of chances.

2. **User-Defined Chances**

   * The player specifies how many chances they want to have to guess the correct number.
   * The program will loop through these chances one by one.

3. **Guess Input and Exit Option**

   * During each turn, the player is prompted to enter a guess.
   * The player can also type `"exit"` at any point to immediately quit the game.

4. **Input Validation**

   * If the player’s input is not a number or `"exit"`, the program will display an error message and prompt the player again without losing a chance.

5. **Guess Evaluation**

   * If the guess matches the secret number, the program congratulates the player and ends the game early.
   * If the guess is lower than the secret number, a “Too Low” message is displayed.
   * If the guess is higher than the secret number, a “Too High” message is displayed.

6. **End of Game**

   * If the player uses up all their chances without guessing correctly, the program informs them that they have lost and reveals the total number of chances they had.
   * The program ends automatically after displaying the result.

**Key Features**

* Random number generation for unpredictability.
* Player decides the number of chances.
* Exit command (`"exit"`) for immediate termination of the game.
* Error handling for invalid inputs.
* Feedback after each guess to guide the player.

**Example Gameplay Flow**
1. The player chooses 5 chances.
2. The computer picks a random number.
3. The player starts guessing, receiving hints after each attempt.
4. The game ends when the player guesses correctly, runs out of chances, or types `"exit"`.

-------
-------


## **ToDo List CLI App — Documentation**

### **Overview**

The Work List Manager is an interactive console-based application that allows users to maintain a personal task list. It provides options to add tasks, remove tasks, view the current list, and exit the application.

---

### **Features**

1. **Add Task (`a`)**

   * Prompts the user to enter a task.
   * Adds the entered task to the work list.
   * Displays a confirmation message after adding.

2. **Remove Task (`b`)**

   * Prompts the user to enter the task they want to remove.
   * Checks if the task exists in the list before removing.
   * Displays a success message if removed, or an error message if not found.

3. **View Work List (`v`)**

   * Displays all the current tasks in the list in their current order.
   * If the list is empty, a message stating "Your work list is empty" is shown.

4. **Exit Application (`e`)**

   * Ends the program and displays a goodbye message.

---

### **Program Flow**

* The program runs in a continuous loop until the user chooses to exit.
* At each iteration, the user is prompted to select an action.
* The work list is updated in real time based on user actions.
* If the work list is empty, the program immediately notifies the user.

-------
-------

## **Number System Converter — Documentation**

### **Overview**

The *Number System Converter* is a Python-based, menu-driven application that allows users to convert numbers between **Binary, Octal, Decimal, and Hexadecimal** formats. It provides a simple interactive interface where the user selects the type of conversion, inputs a value, and receives the converted result instantly.

---

### **Objective**

To create a simple and user-friendly tool for converting numbers between different number systems using Python’s built-in functions.

---

### **Tools Used**

* **Python 3.x** — for program logic and built-in conversion functions
* **VS Code / Jupyter Notebook** — for writing and running the code
* **Basic knowledge of number systems** — to understand conversions between Binary, Octal, Decimal, and Hexadecimal

---

### **Features**

* Menu-driven interface for easy navigation
* Supports the following conversions:

  1. Decimal → Binary
  2. Binary → Decimal
  3. Decimal → Octal
  4. Octal → Decimal
  5. Decimal → Hexadecimal
  6. Hexadecimal → Decimal
* Repeats until the user chooses to exit
* Uses Python’s built-in functions like `bin()`, `oct()`, `hex()`, and `int()` for accurate conversions

---

### **How It Works**

1. **Menu Display**
   The program displays a list of conversion options (1–6) and an exit option (7).

2. **User Input**
   The user selects the desired conversion type by entering a number from the menu.

3. **Number Entry**
   Based on the selected option, the user is prompted to enter a number in the corresponding number system.

4. **Conversion Process**

   * For decimal to other systems, Python’s `bin()`, `oct()`, and `hex()` functions are used.
   * For other systems to decimal, the `int(number, base)` function is used, where the base is **2** for binary, **8** for octal, and **16** for hexadecimal.

5. **Output**
   The converted number is displayed in the appropriate format (without prefixes like `0b`, `0o`, or `0x`).

6. **Repeat or Exit**
   After each conversion, the menu appears again, allowing the user to perform multiple conversions until they choose to exit.

---

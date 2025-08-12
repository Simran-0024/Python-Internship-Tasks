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

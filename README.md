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
----
# Contact Book — Documentation

This program is a simple **command-line Contact Management System** that allows users to **store, view, search, and delete contacts**. Contacts are saved in a CSV file so that the data remains persistent even after the program is closed.

---

## **Features**

1. **Add Contact**

   * Users can enter a contact's **Name**, **Phone number**, and **Email address**.
   * The details are appended to the `contacts.csv` file for future use.
   * If the file does not exist initially, the program automatically creates it with proper headers.

2. **View Contacts**

   * Displays all the saved contacts from the CSV file.
   * Each row contains the **Name, Phone, and Email**.
   * The program skips the header and shows only actual contacts.

3. **Search Contact**

   * Lets users search for a contact by entering a **name**.
   * The search is **case-insensitive** (e.g., "John" and "john" are treated the same).
   * If found, the program prints the full contact details.
   * If not found, it notifies the user.

4. **Delete Contact**

   * Allows users to delete a contact by entering a **name**.
   * The program rewrites the file excluding the contact to be deleted.
   * If the contact is not present, no changes are made.
   * Displays a message confirming deletion (if existed).

5. **Exit Option**

   * Users can exit the program anytime by choosing the exit option.

---

## **File Handling**

* The program uses a file named **`contacts.csv`** to store contacts.
* At startup, it checks if the file exists:

  * If not, it creates the file and adds a header row (`Name, Phone, Email`).
* All future read/write operations are performed on this file.

---

## **User Interaction**

* The program runs in a continuous **menu-driven loop**, presenting options:

  1. Add Contact
  2. View Contacts
  3. Search Contact
  4. Delete Contact
  5. Exit

* The user selects an option by entering a number (1–5).

* If an invalid choice is entered, the program notifies the user and asks again.

---
---

# Student Management System — Documentation

This program is a **menu-driven student management system** that allows users to manage student records. It uses **Object-Oriented Programming (OOP)** concepts in Python and provides options to **add, view, search, update, and delete students**.

---

## **Core Concept**

* The program is built around a **`Student` class**, which holds:

  * **Name** of the student
  * **Roll Number** (unique identifier)
  * **Course** enrolled in
  * **Marks** (default is `0`)

* The class provides methods for:

  * Displaying student details
  * Adding/updating marks
  * Calculating grade based on marks

---

## **Features**

### 1. **Add Student**

* User enters the **Name, Roll Number, and Course**.
* A new `Student` object is created and added to the list of students.
* Confirmation message is displayed.

---

### 2. **View All Students**

* Displays the details of all stored students.
* If no students are found, the program notifies the user.
* Information displayed includes:

  * Name
  * Roll Number
  * Course
  * Marks

---

### 3. **Search Student by Roll Number**

* User enters a roll number.
* If a student with that roll number exists:

  * Displays student details
  * Calculates and shows the **grade**:

    * Marks ≥ 90 → Grade A
    * Marks ≥ 75 → Grade B
    * Marks ≥ 50 → Grade C
    * Marks < 50 → Grade F
* If not found, displays "Student not found."

---

### 4. **Update Marks**

* User enters a roll number to identify the student.
* If found, user can enter new marks.
* Marks are updated and confirmation is shown.
* If not found, the program notifies the user.

---

### 5. **Delete Student**

* User enters a roll number to delete a student.
* If found, the student is removed from the list.
* Displays a confirmation message.
* If not found, shows "Student not found."

---

### 6. **Exit**

* Ends the program with a goodbye message.

---

## **User Interaction**

* The program continuously shows a **menu of options** until the user chooses to exit.

* Options:

  1. Add Student
  2. View All Students
  3. Search Student by Roll No
  4. Update Marks
  5. Delete Student
  6. Exit

* Input is taken from the user, and the corresponding operation is executed.

* Invalid choices are handled gracefully with a message asking the user to try again.

---
---

# Weather Application — Documentation

This program is a **command-line weather application** that fetches and displays real-time weather information for any city using the **OpenWeatherMap API**.

---

## **Features**

1. **Fetch Weather Data**

   * Retrieves weather details (temperature, humidity, and description) for a user-specified city.
   * Data is shown in **Celsius** for user convenience.

2. **Error Handling**

   * **Invalid API Key** → Alerts the user.
   * **City not found** → Notifies if the entered city does not exist.
   * **No Internet** → Handles connection errors gracefully.
   * Any other errors display the status code.

3. **Loop & Exit Option**

   * Runs continuously, asking for city names.
   * User can type `"exit"` anytime to quit the program.

---

## **User Interaction**

* The program asks: *"Enter city name"*
* On valid input, it displays:

  * 🌡 **Temperature (°C)**
  * 💧 **Humidity (%)**
  * ☁️ **Condition (weather description)**
* Example: *Weather in London → 18°C, 65% humidity, cloudy*

---
----

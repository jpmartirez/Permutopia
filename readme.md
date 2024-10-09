# 💫Project Exam Title - "Permutopia"

## 👩🏻‍💻Description

This project is a Python Language Program that uses a GUI application for generating combinations and permutations. The project provides users with an intuitive interface to explore mathematical concepts and perform calculations related to discrete mathematics. It gives a unique and worthwhile experience for students programming techniques as well as having a visual presentation on the topics Linear Permutation, Circular Permutation, Permutation with Repeated Elements, Permutation with Truncated Elements and Combination.

## 🌐 Topics

## ` 1. Linear Permutation`

- Linear permutation refers to an arrangement of a set of objects in a specific order, where the order matters. In mathematics, particularly in combinatorics, it involves finding all possible ways to arrange a certain number of items linearly.

For example in our system, if you have three letters: A, B, and C, the linear permutations would include arrangements like ABC, ACB, BAC, BCA, CAB, and CBA. The formula for calculating the number of linear permutations of 𝑛 distinct objects is 𝑛! (n factorial), which is the product of all positive integers up to 𝑛.

In a broader context, linear permutations can also refer to the concept of arranging elements in sequences or lines, which can be applied in various fields, including computer science, cryptography, and operations research.

## `2. Circular Permutations`

- Circular permutations account for arrangements where the order matters, but rotations of the same arrangement are viewed as identical. For example, if you have three objects 𝐴 , 𝐵 and 𝐶 , the arrangements 𝐴𝐵𝐶, 𝐵𝐶𝐴 , and 𝐶𝐴𝐵 are considered the same in a circular permutation. The formula for the number of distinct circular permutations of 𝑛 objects is (n−1)!, since fixing one object helps eliminate the redundancy caused by rotations. This concept is particularly useful in combinatorial problems, such as seating arrangements around a table or designing round-robin tournaments. Understanding circular permutations can enhance problem-solving strategies in various fields, including mathematics and computer science.

For example in our system, Consider four friends in CCMS —Jp, Jef, Kenneth, and Dave —forming circular positions in a dance. To find the number of distinct arrangements, we use the formula
(𝑛−1)!, where 𝑛 n is the number of friends. Here, n=4, so the number of circular permutations is
(4−1)!=3!=6. The distinct arrangements are:

- Jp, Jef, Kenneth, Dave
- Jp, Jef, Dave, Kenneth
- Jp, Kenneth, Jef, Dave
- Jp, Dave, Jef, Kenneth
- Jp, Kenneth, Dave, Jef
- Jp, Dave, Kenneth, Jef

## `3. Permutations with Repeated Elements`

- Permutations with repeated elements involve counting the different arrangements of a set of items where some items may be identical. To find the total number of unique arrangements, you consider the total number of items and the counts of each repeated item. This method ensures that you accurately account for indistinguishable items. It's a key concept in combinatorics, helping to understand how many distinct arrangements can be formed. This understanding is important for solving various problems in probability and statistics.

For example in our system, Sure! Let’s say you have a collection of books categorized by genre. Imagine you have the following genres:

- 2 Mystery
- 3 Fantasy
- 1 Science Fiction

In total, you have 6 books: 2 Mystery (M), 3 Fantasy (F), and 1 Science Fiction (S).

To find the number of unique ways to arrange these books, you can use the formula for permutations with repeated elements:

P(n; n1, n2, n3, ..., nk) = n! / (n1! _ n2! _ n3! _ ... _ nk!)

Here, n = 6 (total books), n1 = 2 (Mystery), n2 = 3(Fantasy), and n3 = 1 (Sci-Fi).

Thus, there are 60 unique ways to arrange your collection of books by genre.

## `4. Truncated`

- In discrete math, "truncated" refers to the process of shortening or limiting a sequence, set, or function by removing elements or values beyond a certain point. This often involves taking a finite portion of an infinite series or cutting off part of a data set. Truncation can simplify analysis and make computations more manageable while retaining essential characteristics of the original structure. Ultimately, it helps focus on relevant data without the complexity of the entire set.

For example in our system, If you have 4 volunteers and want to assign them to 3 roles using the formula 𝑛!/(𝑛−𝑘)!, where 𝑛 is the total number of volunteers and 𝑘 is the number of roles, the calculation would be as follows:

Given Volunteers:

- Alice
- Bob
- Charlie
- David

Roles:

- First Aid Responder
- Search Operations Specialist
- Supply Delivery Coordinator

Calculating it step by step:

1. 4! = 24
2. (4-3)! = 1! = 1

So:

Arrangements = 24/1 = 24

Conclusion:

- There are 24 possible arrangements for assigning the three roles to the four volunteers.

## `5. Combinations`

- In discrete mathematics, combinations refer to the selections made from distinct categories where the order of selection does not matter. For instance, when choosing items from multiple food groups, such as fruits, vegetables, grains, and proteins, the total number of unique combinations can be calculated by multiplying the number of options available in each category. This approach allows for a comprehensive understanding of how different selections can be made while highlighting the diversity of combinations that can be formed from a set of items. Ultimately, combinations are essential for analyzing choices in various contexts, such as meal planning or resource allocation.

For example in our system, If you have options for fruits, vegetables, grains, and protein, you can calculate the total number of combinations in a similar way. Let's assume you have the following:

Given:

- Fruits: 2 options
- Vegetables: 3 options
- Grains: 2 options
- Protein: 2 options

Calculation:

- The total number of combinations is calculated as follows:
  Total Combinations=(Number of Fruits)×(Number of Vegetables)×(Number of Grains)×(Number of Proteins)

Total Combinations=2×3×2×2=24

Conclusion:

- You can create 24 different combinations of fruits, vegetables, grains, and proteins.

## 📝Installation

To install this project, follow these steps:

## Installation Guide for Python, PyQt6, and PySide6

This guide will help you install Python, PyQt6, and PySide6 on your system.

## Step 1: Install Python

1. `**Download Python:**`

   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest version suitable for your operating system (Windows, macOS, or Linux).

2. `**Run the Installer:**`

   - For Windows, run the downloaded installer.
   - Ensure you check the box that says "Add Python to PATH" before clicking "Install Now."

3. `**Verify Installation:**`
   - Open a command prompt (Windows) or terminal (macOS/Linux).
   - Type the following command and press Enter:
     ```bash
     python --version
     ```
   - Alternatively, you can use:
     ```bash
     python3 --version
     ```

## Step 2: Install PyQt6

1. `**Open Command Prompt or Terminal:**`

   - On Windows, search for "cmd" and open the Command Prompt.
   - On macOS/Linux, open the Terminal.

2. `**Install PyQt6 using pip:**`

   - Run the following command:
     ```bash
     pip install PyQt6
     ```

3. `**Verify Installation:**`
   - Start a Python shell:
     ```bash
     python
     ```
   - Try to import PyQt6:
     ```python
     import PyQt6
     print(PyQt6.__version__)
     ```

## Step 3: Install PySide6

1. `**Open Command Prompt or Terminal:**`

   - Make sure you’re still in the command prompt or terminal.

2. `**Install PySide6 using pip:**`

   - Run the following command:
     ```bash
     pip install PySide6
     ```

3. `**Verify Installation:**`
   - Start a Python shell and try importing PySide6:
     ```python
     import PySide6
     print(PySide6.__version__)
     ```

## 🖥️Now you should have Python, PyQt6, and PySide6

## Before Running Project

- Download the three Python Files, main.py, homepage.py, and resources.py.

- Prepare all files in one folder or in one directory.

- Then, open the folder in a IDE like,
  -- VS Code, PyCharm, Spyder and other preferred IDEs.

- Lastly, Run the main.py.

# PyQt6 GUI Project - Permutopia

## File Structure

- `main.py`: Contains the core functionality and event-handling logic of the application.
- `homepage.py`: Contains the GUI design, converted from a `.ui` file using `pyuic6`.
- `resources.py`: Contains the necessary images and resources for the application.

## Classes Explanation

### `MainApp(QWidget, Ui_Form)`

This is the main class that inherits from `QWidget` (a PyQt6 base class for window-based applications) and `Ui_Form` (the user interface created using Qt Designer and converted to Python code).

#### Methods

1. **`showRepeated(self)`**:

   - This method is triggered when the user clicks the button for **Repeated Permutations**.
   - It creates an instance of the `Repeated` class, shows the corresponding window, and closes the current one.

2. **`showTruncated(self)`**:

   - This method handles the **Truncated Permutations** button.
   - It creates an instance of the `Truncated` class, shows the new window, and closes the current one.

3. **`showLinear(self)`**:

   - When the user selects **Linear Permutations**, this method is called.
   - It creates an instance of the `Linear` class, opens the Linear permutation window, and closes the current one.

4. **`showCombination(self)`**:

   - This method is used for **Combination Permutations**.
   - It creates and shows a window for combinations and closes the main window.

5. **`showCircular(self)`**:

   - This handles the **Circular Permutations**.
   - It creates an instance of the `Circular` class and closes the current window while opening the new one.

6. **`exitProgram(self)`**:

   - This method is called when the user clicks the **Exit** button.
   - It closes the application.

7. **`showMembers(self)`**:
   - When the **Contacts** button is clicked, this method is triggered.
   - It creates and shows a window that displays the members, and the main window is closed.

### `Members(QWidget, Ui_Members)`

This class represents the "Members" window, which provides links to social media profiles.

#### Key Components:

- **Back Button (`back`)**: When clicked, the application returns to the main window using the `backMain()` method.
- **Social Media Buttons**: These buttons open the social media profiles for specific members:
  - `gabfb`: Opens Gab's Facebook profile.
  - `gabig`: Opens Gab's Instagram profile.
  - `jeffb`: Opens Jeff's Facebook profile.
  - `jefig`: Opens Jeff's Instagram profile.
  - `jpfb`: Opens JP's Facebook profile.
  - `jpig`: Opens JP's Instagram profile.

### `LinearSystem Class`

#### Key Components:

- **Back Button (`back`)**: Returns to the instruction window using the `backInstruct()` method.
- **Generate Button (`generate_button`)**: Initiates the generation of permutations based on the inputted student names.

#### Navigation Logic

Clicking the back button takes the user to the instruction window, while clicking the generate button processes the input and generates seating arrangements.

#### Example Methods:

- `backInstruct()`: Returns to the `LinearInstruct` window.
- `generate_arrangements()`: Retrieves student names from the input, validates the input, and generates permutations.
- `generate_permutations(arr)`: Implements the lexicographic permutation algorithm to generate all possible arrangements of the provided names.

## `CombinationSystem Class`

### Key Components:

- **Back Button (`back`)**: This button, when clicked, returns the user to the instruction window by invoking the `backInstruct()` method.
- **Generate Button (`generate_button`)**: This button triggers the generation of food combinations based on the input provided by the user.

### Logic Breakdown:

1. **Initialization**:

   - The `__init__` method sets up the UI for the `CombinationSystem` class and connects the back button and generate button to their respective methods.

2. **Back to Instruction**:

   - The `backInstruct()` method creates an instance of the `CombinationInstruct` class and displays it, closing the current window in the process.

3. **Generate Combinations**:
   - The `generate_combinations()` method performs the following steps:
     - **Input Retrieval**: It retrieves user input from four input fields (proteins, vegetables, grains, and fruits) and splits the input by commas. Each item is stripped of whitespace, and only non-empty items are retained.
     - **Input Validation**: The method checks if the user has provided valid options for all categories. If any category is empty, an error message is displayed in the output area.
     - **Combination Generation**: If all inputs are valid, it generates all possible combinations by iterating through each category and appending formatted strings of combinations (e.g., "protein + vegetable + grain + fruit") to a list.
     - **Results Display**: Finally, the method calculates the total number of combinations and updates the output area with the total count and the list of combinations.

## `CircularSystem Class`

### Key Components:

- **Back Button (`back`)**: This button, when clicked, returns the user to the instruction window by invoking the `backPage()` method.
- **Generate Button (`generate_button`)**: This button triggers the generation of circular dance arrangements based on the input provided by the user.

### Logic Breakdown:

1. **Initialization**:

   - The `__init__` method sets up the UI for the `CircularSystem` class and connects the back button and generate button to their respective methods.

2. **Back to Instruction**:

   - The `backPage()` method creates an instance of the `CircularInstruct` class and displays it, closing the current window in the process.

3. **Generate Circular Permutations**:

   - The `generate_circular_permutations()` method performs the following steps:
     - **Input Handling**: It takes a list of dancer names as input and handles the case of zero dancers by returning an empty list.
     - **Fixing the First Dancer**: To manage circular permutations, it fixes the first dancer and initializes an empty list for the current permutations.
     - **Generating Permutations**: It iterates through the remaining dancers and creates new permutations by adding the current dancer to existing permutations at all possible positions.
     - **Finalizing Permutations**: After generating all possible arrangements of the remaining dancers, the fixed dancer is added to each permutation to form complete circular arrangements.

4. **Generate Arrangements**:
   - The `generate_arrangements()` method performs the following steps:
     - **Input Retrieval**: It retrieves user input from the dancer names input field and splits the input by commas. Each item is stripped of whitespace, and only non-empty items are retained.
     - **Input Validation**: The method checks if at least one dancer name has been provided. If no names are given, an error message is displayed in the output area.
     - **Circular Permutation Generation**: If the input is valid, it calls the `generate_circular_permutations()` method to create the circular arrangements.
     - **Results Display**: Finally, the method calculates the total number of circular arrangements and updates the output area with the total count and the list of arrangements.

## `TruncatedSystem Class`

### Key Components:

- **Back Button (`back`)**: This button, when clicked, returns the user to the instruction window by invoking the `backInstruct()` method.
- **Generate Button (`generate_button`)**: This button triggers the generation of task assignments based on the volunteers provided by the user.

### Logic Breakdown:

1. **Initialization**:

   - The `__init__` method sets up the UI for the `TruncatedSystem` class and connects the back button and generate button to their respective methods.

2. **Back to Instruction**:

   - The `backInstruct()` method creates an instance of the `TruncatedInstruct` class and displays it, closing the current window in the process.

3. **Generate Task Assignments**:

   - The `generate_task_assignments()` method performs the following steps:
     - **Task List**: It defines a fixed list of tasks: `['First Aid', 'Search Operations', 'Supply Delivery']`.
     - **Input Handling**: It retrieves the user input for volunteers from the input field, splits the input by commas, and removes any leading or trailing whitespace.
     - **Input Validation**: The method checks if at least three volunteers have been provided. If not, it displays an error message in the output area.
     - **Task Assignment Generation**: If the input is valid, it calls the `generate_permutations()` method to create all possible assignments of volunteers to tasks.
     - **Output Preparation**: The method constructs a formatted string showing each volunteer's assigned task and calculates the total number of combinations.
     - **Results Display**: Finally, it updates the output area with the total number of combinations and the task assignments.

4. **Generate Permutations**:
   - The `generate_permutations()` method performs the following steps:
     - **Input Validation**: If fewer than three volunteers are provided, it returns an empty list.
     - **Permutation Generation**: The method generates all possible unique permutations of three volunteers from the provided list. It uses nested loops to ensure that no volunteer is assigned to multiple tasks in a single assignment.
     - **Results Return**: It returns a list of all unique volunteer-task assignments.

## RepeatedSystem Class

### Functionality

- **Back Navigation:**

  - The class allows users to navigate back to the previous interface using the `back` button.

- **Generate Arrangements:**
  - Users can input book categories in a comma-separated format.
  - The system counts the occurrences of each category and generates all possible arrangements of the categories, taking into account repetitions.

### Components

1. **Initialization:**

   - The `__init__` method initializes the UI and connects buttons to their respective functions:
     - `self.back` is connected to the `backInstruct` method.
     - `self.generate_button` is connected to the `generate_arrangements` method.

2. **Back Instruction:**

   - The `backInstruct` method navigates the user back to the previous application interface.

3. **Generate Arrangements Method:**

   - The `generate_arrangements` method performs the following steps:
     - Retrieves user input from `self.category_input`, splits it by commas, and strips any whitespace.
     - Checks if any categories are entered; if none are provided, it displays an error message.
     - Counts occurrences of each category using a dictionary (`category_counts`).
     - Calls the `generate_permutations` method to recursively generate all unique arrangements.
     - Calculates the total number of arrangements and displays the results in `self.output_area`.

4. **Generating Permutations:**
   - The `generate_permutations` method is a recursive function that constructs arrangements:
     - It checks if all categories have been used (i.e., if the sum of counts is zero). If so, it adds the current arrangement to the list of generated arrangements.
     - It iterates through each category and, if there are still occurrences available, it:
       - Appends the category to the current arrangement.
       - Decreases the count for that category.
       - Recursively calls itself to continue generating arrangements.
       - Backtracks by restoring the category count and removing the last added category.

# 💻 Tech Stack:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

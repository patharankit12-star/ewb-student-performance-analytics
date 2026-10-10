# Student Analytics System

An interactive, terminal-based Python application built to manage, track, and analyze the performance of  students (analysts). This project uses the power of **Pandas** and **NumPy** to automate data calculations, grading, and reporting without needing a complex database.

##  Project Overview
This tool allows users to act as an administrator to add new student records (with subjects like Python Automation, Network Security, Hardware Scripting, etc.), update marks, and automatically calculate their overall performance (Total, Percentage, Grade, and Pass/Fail status). 

##  Technologies Used
* **Language:** Python 3
* **Libraries:** 
  * `pandas` (For data manipulation, CSV handling, and DataFrame operations)
  * `numpy` (For vectorized mathematical calculations and conditional grading)

##  Project Structure
* `main.py`: The main frontend interface containing the interactive terminal menus.
* `functions.py`: The backend engine containing all the logic for data processing and analytics.
* `students.csv`: The core database file where all records are permanently stored and updated.
* `README.md`: Project documentation.

##  Key Features & How They Work

### 1. Data Management (CRUD Operations)
* **Add New Record:** Auto-generates a new unique `Student_ID`, takes subject marks as input, calculates the exact average, and saves the new analyst to the CSV file.
* **Search Details:** Allows searching for a specific student using their ID, Name, or Department (e.g., Blue_Team, Red_Team) and displays their raw data.
* **Update Record:** Search for a student and update specific fields (Name, Department, or specific subject marks). If marks are updated, the system automatically recalculates the new Average.
* **Delete Record:** Safely removes a student from the database and automatically re-sequences all `Student_ID`s so there are no gaps in the numbering.
* **Rename Table Headers:** Allows the user to dynamically rename any column header in the database directly from the terminal.

### 2. Reports & Analytics
* **Performance Calculations:** Uses NumPy conditions to automatically generate random attendance, calculate total marks out of 500, calculate percentages, assign grades (A+ to D), and determine Pass/Fail status (passing criteria >= 40%).
* **Targeted Search:** View the performance report of the entire class, or filter it down to a specific student using their ID or Name.

### 3. Utility & Exports
* **View & Download Raw Data:** Displays the current raw database and gives an option to download a copy as `Student_Data.csv`.
* **Download Combined Master Report:** Combines raw marks with all calculated performance metrics (Grades, Percentages) and exports a complete master report as `student_Data_Performance_Report.csv`.

## ⚙️ How to Run the Project

1. **Install Requirements:** Make sure you have Python installed. Then, install the required libraries by running this command in your terminal:
   ```bash
   pip install pandas numpy

2. Start the Application: Run the main Python file to launch the system interface:
    python main.py
3. Navigate the Menu: Use your keyboard to enter the numbers (1-9) corresponding to the menu options you want to execute.

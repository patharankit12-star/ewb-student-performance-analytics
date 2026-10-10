# import library pandas and numpy
import pandas as pd
import numpy as np


# DATA-load function

def load_sec_data():
    # use pandas and red data from csv file
    df = pd.read_csv('students.csv')
    return df

# ADD User data
def add_new_record(df):
    print("\n--- Enter New Student Details ---")

    # 1. Auto-generate Student ID
    if not df.empty:
        s_id = int(df['Student_ID'].max()) + 1
    else:
        s_id = 101 # if data full empty then set 101 otherwise in sequnnce

    print(f"New  Student ID: {s_id}")

    # take data from user

    name = input("Enter Name: ")
    dept = input("Enter Department (e.g., Blue_Team, Red_Team): ")

    py_marks = float(input("Python_Automation Marks: "))
    net_marks = float(input("Network_Security Marks: "))
    hw_marks = float(input("Hardware_Scripting Marks: "))
    web_marks = float(input("Web_Vulnerabilities Marks: "))
    log_marks = float(input("Log_Analysis Marks: "))

    # take avarage of new student marks

    total = py_marks + net_marks + hw_marks + web_marks + log_marks
    avg = total / 5

    new_student_data = pd.DataFrame([{
        'Student_ID': s_id,
        'Name': name,
        'Department': dept,
        'Python_Automation': py_marks,
        'Network_Security': net_marks,
        'Hardware_Scripting': hw_marks,
        'Web_Vulnerabilities': web_marks,
        'Log_Analysis': log_marks,
        'Average': avg
    }])

    # join data in old file
    updated_df = pd.concat([df, new_student_data], ignore_index=True)
    updated_df.to_csv('students.csv', index=False)

    print("Sucessfully add this new student data.")
    return updated_df

# Search User Data

def search_data(df):
    print("\n--- Search Student Details ---")
    print("choice from 1,2,3")
    print("1. Search by Student ID")
    print("2. Search by Analyst Name")
    print("3. Search by Department (e.g., Blue_Team)")
    choice = input("choice from please enter your Digit ? (1/2/3): ")

    # 1. Logic for searching
    if choice == '1':
        s_id = int(input("Enter Student ID: "))
        result = df[df['Student_ID'] == s_id]

    elif choice == '2':
        search_name = input("Enter Student Name: ")
        result = df[df['Name'].str.lower() == search_name.lower()]

    elif choice == '3':
        search_dept = input("Enter Department Name: ")
        result = df[df['Department'].str.lower() == search_dept.lower()]

    else:
        print("\nInvalid choice. please select digit from 1,2 or 3.")
        return

    # search output
    if not result.empty:
        print("\n FOUND! Details show:")
        print("\n")
        print(result.to_string(index=False))

        if choice == '3':
            print(f"Total student  in this Department: {len(result)}")

    else:
      print("\n NOT FOUND.please check your input details")


# DELETE User Data

def delete_record(df):
        print("DELETE STUDENT RECORD")
        print("1. Search by Student ID to delete")
        print("2. Search by Student Name to delete")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            s_id = int(input("Enter Student ID: "))
            matched_data = df[df['Student_ID'] == s_id]

        elif choice == '2':
            search_name = input("Enter Student Name: ")
            matched_data = df[df['Name'].str.lower() == search_name.lower()]

        else:
            print("\nInvalid choice. Delete cancel.")
            return df

        # 2. if data not found.
        if matched_data.empty:
            print("NOT FOUND , DATA mis-match")
            return df
        print(matched_data.to_string(index=False))

        confirm = input("\nAre you sure to delete this student? (yes/no): ").lower()

        # 4. Deletion and Re-sequencing in csv file.

        if confirm == 'yes':
            index_to_delete = matched_data.index[0]
            df = df.drop(index_to_delete)

            # repair index
            df = df.reset_index(drop=True)
            df['Student_ID'] = range(101, 101 + len(df))

            # save in file permenetally
            df.to_csv('students.csv', index=False)

            print("Data Deleted Sucessfully.")

        elif confirm == 'no':
            print("\n Data Deletion cancel.")
        else:
            print("\nInvalid input. Deletion cancelled.")

        return df

# UPDATE User Data
def update_record(df):
    print("UPDATE STUDENT RECORD")
    # 1. Search Logic
    print("1. Search by Student ID")
    print("2. Search by Student  Name")
    search_choice = input("Enter your choice (1/2): ")
    if search_choice == '1':
        s_id = int(input("Enter Student ID: "))
        matched_data = df[df['Student_ID'] == s_id]
    elif search_choice == '2':
        search_name = input("Enter Student Name: ")
        matched_data = df[df['Name'].str.lower() == search_name.lower()]
    else:
        print("\n Invalid choice. Update cancel.")
        return df

    if matched_data.empty:
        print("\nNOT FOUND.Data Doesn't match.")
        return df
    # 2. Show Previous Details

    print("\n PREVIOUS DETAILS:")
    print("\n")
    print(matched_data.to_string(index=False))

    #3. confermation

    confirm = input("\nAre you sure to update this detail? (yes/no): ").lower()

    if confirm == 'yes':
        index_to_update = matched_data.index[0]

        # 4. Continuous Update Loop

        while True:
            print("\n--- SELECT FIELD TO UPDATE ---")
            print("1. Update Name")
            print("2. Update Department")
            print("3. Update Python_Automation marks")
            print("4. Update Network_Security marks")
            print("5. Update Hardware_Scripting marks")
            print("6. Update Web_Vulnerabilities marks")
            print("7. Update Log_Analysis marks")

            field_choice = input("Enter your choice (1-7): ")

            if field_choice == '1':
                df.loc[index_to_update, 'Name'] = input("Enter new Name: ")
            elif field_choice == '2':
                df.loc[index_to_update, 'Department'] = input("Enter new Department: ")
            elif field_choice == '3':
                df.loc[index_to_update, 'Python_Automation'] = float(input("Enter new Python marks: "))
            elif field_choice == '4':
                df.loc[index_to_update, 'Network_Security'] = float(input("Enter new Network Security marks: "))
            elif field_choice == '5':
                df.loc[index_to_update, 'Hardware_Scripting'] = float(input("Enter new Hardware Scripting marks: "))
            elif field_choice == '6':
                df.loc[index_to_update, 'Web_Vulnerabilities'] = float(input("Enter new Web Vuln marks: "))
            elif field_choice == '7':
                df.loc[index_to_update, 'Log_Analysis'] = float(input("Enter new Log Analysis marks: "))
            else:
                print("Invalid Choice! please choice from this 1-7.")

            # 5. Average Recalculation
            if field_choice in ['3', '4', '5', '6', '7']:
                sub_marks = df.loc[index_to_update, ['Python_Automation', 'Network_Security', 'Hardware_Scripting', 'Web_Vulnerabilities', 'Log_Analysis']]
                new_avg = sub_marks.sum() / 5
                df.loc[index_to_update, 'Average'] = new_avg

            # 6. Continue or Exit Logic
            cont = input("\nDo you want to continue updating other details? (yes/no): ").lower()
            if cont != 'yes':
                df.to_csv('students.csv', index=False)
                print("\nSUCCESS: Data updated and saved permanently!\n")
                break
    else:
        print("\n Not updated and exit.")
    return df

# RENAME Header/Column Data

def rename_header(df):
    print("-----RENAME STUDENT LIST HEADERS-----")
    # 1. Current (Previous) Headers

    current_headers = df.columns.tolist()
    print("\nSELECT HEADER TO RENAME:\n")
    for index, header in enumerate(current_headers, start=1):
        print(f"{index}. change {header}")
    try:
        # choice from user

       choice = int(input("\nEnter your choice (1-9): "))
       if 1 <= choice <= len(current_headers):
          old_name = current_headers[choice - 1]
          # new header name

          new_name = input(f"\nEnter new header name for '{old_name}': ")

          # 4. Final Confirmation

          confirm = input(f"Are you sure to change '{old_name}' to '{new_name}'? (yes/no): ").lower()

          # 5. Yes ya No logic
          if confirm == 'yes':
            df.rename(columns={old_name: new_name}, inplace=True)
            df.to_csv('students.csv', index=False)
            print("Header changed successfully!")
       else:
         print("\nInvalid choice. Kripya 1 se 9 ke beech chunein.")

    except ValueError:
        print("\n Invalid input.\n")
    return df


def show_performance_table(df):
    print("----------------STUDENT PERFORMANCE ANALYTICS---------------------")
    perf_df = df[['Student_ID', 'Name']].copy()
    perf_df['Attendance'] = np.random.randint(50, 101, size=len(df))
    # 2. Total marks calculate
    subjects = ['Python_Automation', 'Network_Security', 'Hardware_Scripting', 'Web_Vulnerabilities', 'Log_Analysis']
    perf_df['Total'] = df[subjects].sum(axis=1)
    perf_df['Percentage'] = (perf_df['Total'] / 500) * 100
    perf_df['Percentage'] = perf_df['Percentage'].round(2)
    # 3. Attendance generate

    # 5. Grade assign
    conditions = [
        (perf_df['Percentage'] >= 90),
        (perf_df['Percentage'] >= 80) & (perf_df['Percentage'] < 90),
        (perf_df['Percentage'] >= 70) & (perf_df['Percentage'] < 80),
        (perf_df['Percentage'] >= 60) & (perf_df['Percentage'] < 70),
        (perf_df['Percentage'] >= 50) & (perf_df['Percentage'] < 60),
        (perf_df['Percentage'] >= 40) & (perf_df['Percentage'] < 50)
    ]
    grades = ['A+', 'A', 'B+', 'B', 'C', 'D']
    perf_df['Grade'] = np.select(conditions, grades, default='-')

    # 6. Pass/Fail Result assign
    # if percentage 40 below then fail and if percentage >=40 then pass
    perf_df['Result'] = np.where(perf_df['Percentage'] >= 40, 'Pass', 'Fail')

    # maintain collum in this
    final_columns = ['Student_ID', 'Name', 'Attendance', 'Total', 'Percentage', 'Grade', 'Result']
    display_df = perf_df[final_columns]


    # search menu section
    print("\n1. Search Performance by Student ID")
    print("2. Search Performance by Analyst Name")
    print("3. Show ALL Students Performance Table")
    choice = input("Enter your choice (1/2/3): ")

    # --- 3. Filtering Logic ---
    if choice == '1':
        try:
            s_id = int(input("Enter Student ID to search: "))
            result = display_df[display_df['Student_ID'] == s_id]
            if not result.empty:
               print(result.to_string(index=False))
            else:
                print("record not found! please try again")
        except ValueError:
            print("Invalid Input")

    elif choice == '2':
        search_name = input("Enter Analyst Name to search: ")
        # name asa per filter
        result = display_df[display_df['Name'].str.lower() == search_name.lower()]
        if not result.empty:
            print(result.to_string(index=False))
        else:
            print(" Record not found! please enter correct spelling ")
    elif choice == '3':
        print(display_df.to_string(index=False))

    else:
        print(" Invalid choice.please enter number from this 1/2/3")

    return display_df


# Download csv file
def show_all_student_data(df):

    print("--------All Student Data------------")
    print(df.to_string(index=False))
    # Download confirmation
    confirm = input("\nDo you want to download this file ? (yes/no): ").lower()

    if confirm == 'yes':
        file_name = "Student_Data.csv"
        df.to_csv(file_name, index=False)
        print(f"Sucessfully Download this '{file_name}' file in your folder")

    else:
        print("\n Download cancelled. Exiting.")
    return df


#COMBINED STUDENT & PERFORMANCE REPORT
def show_combined_report(df):
    print("---COMBINED STUDENT & PERFORMANCE REPORT---")
    comb_df = df.copy()
    # 2. Performance calculations
    comb_df['Attendance'] = np.random.randint(50, 101, size=len(df))
    subjects = ['Python_Automation', 'Network_Security', 'Hardware_Scripting', 'Web_Vulnerabilities', 'Log_Analysis']
    comb_df['Total'] = comb_df[subjects].sum(axis=1)
    comb_df['Percentage'] = (comb_df['Total'] / 500) * 100
    comb_df['Percentage'] = comb_df['Percentage'].round(2)

    conditions = [
        (comb_df['Percentage'] >= 90),
        (comb_df['Percentage'] >= 80) & (comb_df['Percentage'] < 90),
        (comb_df['Percentage'] >= 70) & (comb_df['Percentage'] < 80),
        (comb_df['Percentage'] >= 60) & (comb_df['Percentage'] < 70),
        (comb_df['Percentage'] >= 50) & (comb_df['Percentage'] < 60),
        (comb_df['Percentage'] >= 40) & (comb_df['Percentage'] < 50)
    ]
    grades = ['A+', 'A', 'B+', 'B', 'C', 'D']
    comb_df['Grade'] = np.select(conditions, grades, default='-')
    comb_df['Result'] = np.where(comb_df['Percentage'] >= 40, 'Pass', 'Fail')
    print(comb_df.to_string(index=False))
    #  Download confirmation for Combined Data
    confirm = input("\nDo you want to download this Combined Report? (yes/no): ").lower()
    if confirm == 'yes':
        file_name = "student_Data_Performance_Report.csv"
        comb_df.to_csv(file_name, index=False)
        print(f"Download sucessfully! '{file_name}'file in your folder.")
    else:
        print("Download cancelled. Exiting menu.")

    return df


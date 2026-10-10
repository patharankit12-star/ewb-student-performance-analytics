import functions as fn

def start_system():
      # start then data load
      df = fn.load_sec_data()

      while True:
          print("\n" + "═" * 55)
          print("--------------[SECURITY STUDENT ANALYTICS SYSTEM]-------------")
          print("═" * 55)
          print("  1.--> Data Management")
          print("  2.--> Reports & Exports")
          print("  3.--> Exit Platform")
          print("═" * 55)

          main_choice = input(" Select an option Enter Features(1-3): ")

          if main_choice == '1':
              print("\n--------[ DATA MANAGEMENT SYSTEM ]---------")
              print("  1. Add New Student Record")
              print("  2. Search Student Details")
              print("  3. Update Student Record")
              print("  4. Delete Student Record")
              print("  5. Rename Table Headers")
              print("  6. Back to Home Page <<--")

              sub_choice_1 = input(" Select an option (1-6): ")

              if sub_choice_1 == '1':
                  df = fn.add_new_record(df)
              elif sub_choice_1 == '2':
                  fn.search_data(df)
              elif sub_choice_1 == '3':
                  df = fn.update_record(df)
              elif sub_choice_1 == '4':
                  df = fn.delete_record(df)
              elif sub_choice_1 == '5':
                  df = fn.rename_header(df)
              elif sub_choice_1 == '6':
                  print("\n Going back to Home Page...")
                  break
              else:
                  print("\n [!] Invalid Input. Please select between 1 and 6.")

          elif main_choice == '2':
              while True:
                  print("\n------------[ REPORTS & EXPORTS ]-------------")
                  print("  1. View student data table")
                  print("  2. View performance data")
                  print("  3. View & Download student data")
                  print("  4. View & Download combine full student details")
                  print("  5. Back to Home Page <<--")

                  sub_choice_2 = input(" Select an option (1-5): ")

                  if sub_choice_2 == '1':
                      # view student data  table
                      print("\n--- Student Data Table ---")
                      print(df.to_string(index=False))

                  elif sub_choice_2 == '2':
                      # view performance table
                      fn.show_performance_table(df)
                  elif sub_choice_2 == '3':
                      # Download student data table
                      df = fn.show_all_student_data(df)
                  elif sub_choice_2 == '4':
                      # Download performance data table
                      fn.show_combined_report(df)
                  elif sub_choice_2 == '5':
                      print("\n Going back to Home Page...")
                      break
                  else:
                     print("\n [!] Invalid Input. Please select between 1 and 5.")

          elif main_choice == '3':
                 print("\n" + "★" * 55)
                 print(" ----THANK YOU FOR USING OUR PLATFORM!-------")
                 print(" Your data is safe. Have a great day. Exiting gracefully...")
                 print("★"*55 + "\n")
                 break
          else:
                print("\nInvalid Input on Home Page. Please select 1, 2, or 3.")

if __name__ == "__main__":
    start_system()
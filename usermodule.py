def user_interface():# User module
    name = str(input("Enter your name: "))
    print(f"\nDear {name}, thank you for choosing to use this code.")
    print("It has been developed to provide valuable insights and streamline your work.")
    
    while True:
        print("\nWhat would you like to check?")
        print("Choose any option that fits what you want to check:")
        print("1: Check the average age, modal age, median age of those whose heart failure resulted in death")
        print("2: Check the average time for those whose heart failure did not result in death")
        print("3: Check the average age, modal age, median age of those with high blood pressure")
        print("4: Check the average age, modal age, median age of those with diabetes")
        print("5: Check if diabetes is linked to smoking and high blood pressure")
        print("6: Check the average serum sodium of those with diabetes")
        print("7: Check if anaemia is linked to smoking or not")
        print("8: Check for anyone without high blood pressure that died of heart failure")
        print("9: Check the IQRs of ejection fraction and serum creatinine")
        print("10: Check the sample variance of creatinine phosphokinase and serum sodium")
        
        choice = int(input("Enter your choice: "))
        
        # Ensure the csv_data is passed correctly to each function
        if choice == 1:
            from querymodule import death_age_statistics
            death_age_statistics(csv_data)  # Pass csv_data here
        elif choice == 2:
            from querymodule import non_death_time_statistics
            non_death_time_statistics(csv_data)  # Pass csv_data here
        elif choice == 3:
            from querymodule import high_bp_statistics
            high_bp_statistics(csv_data)  # Pass csv_data here
        elif choice == 4:
            from querymodule import diabetes_statistics
            diabetes_statistics(csv_data)  # Pass csv_data here
        elif choice == 5:
            from querymodule import diabetes_smoking_highbp_link
            diabetes_smoking_highbp_link(csv_data)  # Pass csv_data here
        elif choice == 6:
            from querymodule import average_serum_sodium_diabetes
            average_serum_sodium_diabetes(csv_data)  # Pass csv_data here
        elif choice == 7:
            from querymodule import anaemia_smoking_link
            anaemia_smoking_link(csv_data)  # Pass csv_data here
        elif choice == 8:
            from querymodule import no_highbp_death
            no_highbp_death(csv_data)  # Pass csv_data here
        elif choice == 9:
            from querymodule import calculate_IQR
            calculate_IQR(csv_data)  # Pass csv_data here
        elif choice == 10:
            from querymodule import compute_variance
            compute_variance(csv_data)  # Pass csv_data here
        else:
            print("Enter a number between 1 and 10")
            continue  # Ask for input again if invalid choice
        
        # Ask if the user wants to continue
        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice == 'no':
            print("Thank you for using the system. Goodbye!")
            break  # Exit the loop and end the program
        elif continue_choice != 'yes':
            print("Invalid input. Exiting the program.")
            break  # Exit the loop if the input is not 'yes' or 'no'

# Call the user interface function to start the program
user_interface()

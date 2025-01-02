import csv
from collections import Counter
from csv_loader import load_csv_with_generated_ids
import statistics

file_path = r"C:\Users\USER\Downloads\heart+failure+clinical+records\heart_failure_clinical_records_dataset.csv"

csv_data = load_csv_with_generated_ids(file_path)


# 1. Function for computing the average age, modal age, and median age of those whose heart failure resulted in death
def death_age_statistics(csv_data):
    sum_of_ages = 0
    count = 0
    ages = []

    for patient_id, details in csv_data.items():
        age = float(details["age"])
        DEATH_EVENT = int(details["DEATH_EVENT"])
        if DEATH_EVENT == 1:  # Filter for those who died
            sum_of_ages += age
            count += 1
            ages.append(age)

    if count > 0:
        average_age = sum_of_ages / count
    else:
        average_age = 0

    # Calculate modal age
    age_frequency = Counter(ages)
    modal_age = age_frequency.most_common(1)[0][0] if age_frequency else None

    # Calculate median age
    ages.sort()
    y = len(ages)
    if y % 2 == 1:
        median_age = ages[y // 2]
    else:
        median_age = (ages[y // 2 - 1] + ages[y // 2]) / 2 if y > 0 else 0

    # Print the results
    print(f"Information on those who died due to heart failure:")
    print(f" Average Age: {average_age}")
    print(f"Modal Age: {modal_age}")
    print(f"Median Age: {median_age}")

death_age_statistics(csv_data)

# 2. Function for computing the average time taken for those whose heart failure did not result in death
def non_death_time_statistics(csv_data):
    total_time_taken = 0
    count = 0
    for patient_id, details in csv_data.items():
        time = int(details['time'])
        DEATH_EVENT = int(details["DEATH_EVENT"])
        if DEATH_EVENT == 0:  # Filter for those who survived
            total_time_taken += time
            count += 1

    if count > 0:
        average_time = total_time_taken / count
    else:
        average_time = 0

    # Print the result
    print(f"Average time for those whose heart failure did not result in death is {average_time}")

non_death_time_statistics(csv_data)

# 3. Function to compute median age, average age, and modal age of those with high blood pressure
def high_bp_statistics(csv_data):
    sum_of_ages = 0
    count = 0
    ages = []

    for patient_id, details in csv_data.items():
        age = float(details["age"])
        high_bp = int(details["high_blood_pressure"])
        if high_bp == 1:  # Filter for high blood pressure cases
            sum_of_ages += age
            count += 1
            ages.append(age)

    if count > 0:
        average_age = sum_of_ages / count
    else:
        average_age = 0

    # Calculate modal age
    age_frequency = Counter(ages)
    modal_age = age_frequency.most_common(1)[0][0] if age_frequency else None

    # Calculate median age
    ages.sort()
    y = len(ages)
    if y % 2 == 1:
        median_age = ages[y // 2]
    else:
        median_age = (ages[y // 2 - 1] + ages[y // 2]) / 2 if y > 0 else 0

    # Print the results
    print(f"Information on those who have high blood pressure:")
    print(f"Their average Age is {average_age}")
    print(f"Their modal Age is {modal_age}")
    print(f"Their Median Age is {median_age}")

high_bp_statistics(csv_data)

# 4. Function to compute median age, average age, and modal age of those with diabetes
def diabetes_statistics(csv_data):
    sum_of_ages = 0
    count = 0
    ages = []

    for patient_id, details in csv_data.items():
        age = float(details["age"])
        diabetes_status = int(details["diabetes"])
        if diabetes_status == 1:  # Filter for diabetes cases
            sum_of_ages += age
            count += 1
            ages.append(age)

    if count > 0:
        average_age = sum_of_ages / count
    else:
        average_age = 0

    # Calculate modal age
    age_frequency = Counter(ages)
    modal_age = age_frequency.most_common(1)[0][0] if age_frequency else None

    # Calculate median age
    ages.sort()
    y = len(ages)
    if y % 2 == 1:
        median_age = ages[y // 2]
    else:
        median_age = (ages[y // 2 - 1] + ages[y // 2]) / 2 if y > 0 else 0

    # Print the results
    print(f"Information of Diabetic patients")
    print(f"Their Average Ageis {average_age}")
    print(f"Their Modal Age is  {modal_age}")
    print(f"Their Median Age is {median_age}")

diabetes_statistics(csv_data)

# 5. Function to determine whether diabetes is linked to smoking and high blood pressure
def diabetes_smoking_highbp_link(csv_data):
    diabetes_smoking_highbp_count = 0
    diabetes_smoking_no_highbp_count = 0
    diabetes_no_smoking_highbp_count = 0
    diabetes_no_smoking_no_highbp_count = 0

    # Count occurrences
    for patient_id, details in csv_data.items():
        diabetes = int(details['diabetes'])
        smoking = int(details['smoking'])
        high_blood_pressure = int(details['high_blood_pressure'])

        if diabetes == 1 and smoking == 1 and high_blood_pressure == 1:
            diabetes_smoking_highbp_count += 1
        elif diabetes == 1 and smoking == 1 and high_blood_pressure == 0:
            diabetes_smoking_no_highbp_count += 1
        elif diabetes == 1 and smoking == 0 and high_blood_pressure == 1:
            diabetes_no_smoking_highbp_count += 1
        elif diabetes == 1 and smoking == 0 and high_blood_pressure == 0:
            diabetes_no_smoking_no_highbp_count += 1

    # Print the contingency table
    print(f"Link between diabetes, smoking, and high blood pressure:")
    print(f"Diabetes, Smoking, and High BP: {diabetes_smoking_highbp_count}")
    print(f"Diabetes, Smoking, No High BP: {diabetes_smoking_no_highbp_count}")
    print(f"Diabetes, No Smoking, High BP: {diabetes_no_smoking_highbp_count}")
    print(f"Diabetes, No Smoking, No High BP: {diabetes_no_smoking_no_highbp_count}")
    print(f"There is no significant relationship between diabetes,smoking and high blood pressure")
diabetes_smoking_highbp_link(csv_data)

# 6. Function to compute the average serum sodium of those with diabetes
def average_serum_sodium_diabetes(csv_data):
    total_sodium = 0
    count = 0
    for patient_id, details in csv_data.items():
        serum_sodium = float(details["serum_sodium"])
        diabetes_status = int(details["diabetes"])
        if diabetes_status == 1:  # Filter for diabetes cases
            total_sodium += serum_sodium
            count += 1

    if count > 0:
        average_sodium = total_sodium / count
    else:
        average_sodium = 0

    # Print the result
    print(f"The average Serum Sodium for those with diabetes is {average_sodium}")

average_serum_sodium_diabetes(csv_data)

# 7. Function to determine if anaemia is linked to smoking
def anaemia_smoking_link(csv_data):
    anaemia_smoking_count = 0
    anaemia_non_smoking_count = 0
    for patient_id, details in csv_data.items():
        anaemia = int(details["anaemia"])
        smoking = int(details["smoking"])

        if anaemia == 1 and smoking == 1:
            anaemia_smoking_count += 1
        elif anaemia == 1 and smoking == 0:
            anaemia_non_smoking_count += 1

    print(f"Link between anaemia and smoking:")
    print(f"Anaemia with smoking: {anaemia_smoking_count}")
    print(f"Anaemia without smoking: {anaemia_non_smoking_count}")
    print(f"This suggests anaemia is not linked to smoking")

anaemia_smoking_link(csv_data)

# 8. Function that returns anyone without high blood pressure that died of heart failure
def no_highbp_death(csv_data):
    for patient_id, details in csv_data.items():
        DEATH_EVENT = int(details["DEATH_EVENT"])
        high_blood_pressure = int(details["high_blood_pressure"])

        if DEATH_EVENT == 1 and high_blood_pressure == 0:
            print(details)

no_highbp_death(csv_data)

# 9. Function to compute and return the IQR of ejection fraction and serum creatinine
def calculate_IQR(csv_data):
    ejection_fraction_values = []
    serum_creatinine_values = []

    for patient_id, details in csv_data.items():
        ejection_fraction = float(details["ejection_fraction"])
        serum_creatinine = float(details["serum_creatinine"])

        ejection_fraction_values.append(ejection_fraction)
        serum_creatinine_values.append(serum_creatinine)

    # Compute IQR for ejection fraction
    ejection_fraction_values.sort()
    ejection_fraction_q1 = ejection_fraction_values[int(0.25 * len(ejection_fraction_values))]
    ejection_fraction_q3 = ejection_fraction_values[int(0.75 * len(ejection_fraction_values))]
    ejection_fraction_IQR = ejection_fraction_q3 - ejection_fraction_q1

    # Compute IQR for serum creatinine
    serum_creatinine_values.sort()
    serum_creatinine_q1 = serum_creatinine_values[int(0.25 * len(serum_creatinine_values))]
    serum_creatinine_q3 = serum_creatinine_values[int(0.75 * len(serum_creatinine_values))]
    serum_creatinine_IQR = serum_creatinine_q3 - serum_creatinine_q1

    print(f"Interquartile Range (IQR) of Ejection Fraction: {ejection_fraction_IQR}")
    print(f"Interquartile Range (IQR) of Serum Creatinine: {serum_creatinine_IQR}")

calculate_IQR(csv_data)

#10. function to compute and return the sample variance of creatinine phosphokinase and serum sodium.
def compute_variance(csv_data):
    # Helper function to calculate the sample variance
    def variance(data):\
        return statistics.variance(data)

    # Lists to hold creatinine_phosphokinase and serum_sodium values
    creatinine_phosphokinase_values = []
    serum_sodium_values = []

    # Iterate through the csv_data and extract the relevant values
    for patient_id, details in csv_data.items():
        creatinine_phosphokinase_values.append(float(details["creatinine_phosphokinase"]))
        serum_sodium_values.append(float(details["serum_sodium"]))

    # Compute variance for both variables
    creatinine_phosphokinase_variance = variance(creatinine_phosphokinase_values)
    serum_sodium_variance = variance(serum_sodium_values)

    return {
        "creatinine_phosphokinase_variance": creatinine_phosphokinase_variance,
        "serum_sodium_variance": serum_sodium_variance
    }

compute_variance(csv_data)

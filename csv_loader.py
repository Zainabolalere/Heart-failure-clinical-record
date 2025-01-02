def load_csv_with_generated_ids(file_path):
    data = {}
    with open(file_path, 'r') as file:
        rows = file.readlines()
        header = rows[0].strip().split(',')  # Extract header from the first row
        
        for index, row in enumerate(rows[1:], start=1):  # Start ID generation from 1
            row = row.strip().split(',')    
            # Create a dictionary for each row
            values = {header[i]: row[i] for i in range(len(row))}  
            data[str(index)] = values
    
    return data

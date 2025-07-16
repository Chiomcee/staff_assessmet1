import json

# Load the json data from the file
def get_patient_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

# Function to explore the JSON data
def display_insurance_details(data):
    if data:
        # display the keys in the JSON data
        print("Keys in the JSON data:", data.keys())
        
        # Extract and display the insurance details
        insurance_details = data.get("insurance", {})
        print("Insuarnce Details:", insurance_details)
        
        # Extract and display the insurance provider
        insurance_provider = insurance_details.get("provider", "N/A")
        print("Insurance Provider:", insurance_provider)
        
        # get patience name
        patient_name = data.get("patient", {}).get("name", {})
        first_name = patient_name.get("first", "")
        last_name = patient_name.get("last", "")
        print(f"Patient Name: {first_name} {last_name}")
        
    else:
        print("No data to explore.")
        
# Main Function to run the script
if __name__ == "__main__":
    file_path = 'patient_data.json'
    #Load the JSON file
    json_data = get_patient_data(file_path)
    # Explore the loaded data
    display_insurance_details(json_data)
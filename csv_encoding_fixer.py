import sys # Importing the 'sys' module to access the command-line arguments passed to the script
import csv # Importing the 'csv' module to read and write CSV files

# This function replaces several unicode characters with their correct encoding
def fix_encoding(text):
    return text.replace('Ã®', 'î').replace('Ã©', 'é').replace('â†’', '-->').replace('Ãœ', 'Ü').replace('Ã¹', 'û').replace('Ã¢', 'â').replace('Ã¨', 'è').replace('Ã ', 'à').replace('â€™', "'").replace('â‚¬', '€').replace('Â®', '®').replace('Ã˜', 'Ø').replace('Â°', '°').replace('Ã§', 'ç').replace('Ã´', 'ô').replace('Â«', '«').replace('Â»', '»').replace('Ã»', 'û').replace('Ãª', 'ê').replace('â€¦', 'ø').replace('Ã€', 'A').replace('Ã‰', 'E')

# Check if the script is called with the required two command-line arguments (input_file and output_file)
if len(sys.argv) < 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1) # Exit the script with a status code of 1 (indicating an error)

# Extract the input file and output file from the command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input file for reading and the output file for writing, both using the cp1252 encoding
with open(input_file, 'r', encoding='cp1252') as infile, \
     open(output_file, 'w', encoding='cp1252', newline='') as outfile:

    # Create a CSV reader object for the input file
    reader = csv.reader(infile)

    # Create a CSV writer object for the output file
    writer = csv.writer(outfile)

    # Read each row from the input file, fix the encoding of each cell in the row, and write the modified row to the output file
    for row in reader:
        new_row = [fix_encoding(cell) for cell in row] # apply fix_encoding function to each cell in the row
        writer.writerow(new_row) # write the modified row to the output file

# Print a message indicating that the conversion was successful
print(f"Converted {input_file} to {output_file}")


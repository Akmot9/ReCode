import sys
import csv

def fix_encoding(text):
    return text.replace('Ã®', 'î').replace('Ã©', 'é').replace('â†’', '-->').replace('Ãœ', 'Ü').replace('Ã¹', 'û').replace('Ã¢', 'â').replace('Ã¨', 'è').replace('Ã ', 'à').replace('â€™', "'").replace('â‚¬', '€').replace('Â®', '®').replace('Ã˜', 'Ø').replace('Â°', '°').replace('Ã§', 'ç').replace('Ã´', 'ô').replace('Â«', '«').replace('Â»', '»').replace('Ã»', 'û').replace('Ãª', 'ê').replace('â€¦', 'ø').replace('Ã€', 'A').replace('Ã‰', 'E')

if len(sys.argv) < 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='cp1252') as infile, \
     open(output_file, 'w', encoding='cp1252', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        new_row = [fix_encoding(cell) for cell in row]
        writer.writerow(new_row)

print(f"Converted {input_file} to {output_file}")

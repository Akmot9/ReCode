import csv

# Define a function to fix encoding errors
def fix_encoding(text):
    # List of characters to replace and their replacements
    to_replace = ['Ã®', 'Ã©', 'â†’', 'Ãœ', 'Ã¹', 'Ã¢', 'Ã¨', 'Ã ', 'â€™', 'â‚¬', 'Â®', 'Ã˜', 'Â°', 'Ã§', 'Ã´', 'Â«', 'Â»', 'Ã»', 'Ãª', 'â€¦', '/Ã¸', 'Ã¸', 'Ã€', 'Ã‰', 'Ãˈ', ' Ã ', 'Ã–']
    replacements = ['î', 'é', '-->', 'Ü', 'û', 'â', 'è', 'à', "'", '€', '®', 'Ø', '°', 'ç', 'ô', '«', '»', 'û', 'ê', '..', 'ø', 'ø', 'A', 'E', 'E', ' à ', 'Ö']

    # Replace each character with its corresponding replacement
    for i in range(len(to_replace)):
        text = text.replace(to_replace[i], replacements[i])
    return text

# Open the input and output files using context managers
with open('_test.csv', 'r', encoding='cp1252') as infile, \
     open('output.csv', 'w', encoding='cp1252', newline='') as outfile:
    # Create CSV reader and writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate over each row in the input file
    for row in reader:
        # Replace encoding errors in each cell of the row
        new_row = [fix_encoding(cell) for cell in row]
        # Write the corrected row to the output file
        writer.writerow(new_row)


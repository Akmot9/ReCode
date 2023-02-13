# for file in list of files
# for row in rows of a file
#A_Remplacer = ["Ã®", "Ã©", "â†’", "Ãœ", "Ã¹", "Ã¢", "Ã¨", "Ã ", "â€™", "â‚¬", "Â®", "Ã˜", "Â°", "Ã§", "Ã´", "Â«", "Â»", "Ã»", "Ãª", "â€¦", "/Ã¸", "Ã¸", "Ã€", "Ã‰", "Ãˆ", " Ã ", "Ã–"]
#Remplacants = ["î" , "é" , Chr(26), "Ü", "û", "â", "è", "à", "'", "€", "®", "Ø", "°", "ç", "ô", Chr(34), Chr(34), "û", "ê", "..", "ø", "ø", "A", "E", "E", " à ", "Ö"]

import csv

with open('input.csv', 'r', encoding='utf-8') as infile, \
     open('output.csv', 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        new_row = [cell.replace('Ã®', 'î') for cell in row]
        writer.writerow(new_row)

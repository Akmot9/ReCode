# CSV Encoding Fixer
This script is used to fix encoding errors in CSV files that contain non-ASCII characters. It replaces common encoding errors such as `Ã®`, `Ã©`, and `â†’` with their correct Unicode equivalents such as `î`, `é`, and `-->`.

## Installation
1. Clone this repository to your local machine using 
```Bash
git clone https://github.com/yourusername/csv-encoding-fixer.git
```
2. Install the required dependencies using pip install -r requirements.txt
## Usage
1. Place the CSV file you want to fix in the same directory as the script.
2. Open a command prompt or terminal and navigate to the script directory.
3. Run the script using the command python csv_encoding_fixer.py input_file.csv output_file.csv

Replace input_file.csv with the name of the CSV file you want to fix, and replace output_file.csv with the name you want to give to the fixed CSV file.

## Troubleshooting
If you encounter any issues with the script, please create an issue on the GitHub repository with a detailed description of the problem and any error messages you received. We will do our best to assist you in resolving the issue.
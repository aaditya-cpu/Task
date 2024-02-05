import pandas as pd
import jinja2
import logging
import pdfkit
import re

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSV into DataFrame
csv_file = 'Consolidatesd.csv'  # Replace with your CSV file name
df = pd.read_csv(csv_file)

# Trim spaces from column names
df.columns = df.columns.str.strip()

# HTML template loading
template_loader = jinja2.FileSystemLoader(searchpath='./')
template_env = jinja2.Environment(loader=template_loader)
template_file = 'index.html'
template = template_env.get_template(template_file)

# Rows with '+' in address
rows_with_plus = df[df['Address'].str.contains('\+', regex=True, na=False)]

# Generate separate file for these rows
rows_with_plus.to_csv('rows_with_plus.csv', index=False)
logging.info('Generated file with rows containing "+" in address.')

# Initialize an empty string for the consolidated HTML content
consolidated_html = ""

# Regular expression to remove "Address" followed by optional characters like ":"
address_regex = re.compile(r'address\s*:? ?', re.IGNORECASE)

# Process each row
for index, row in df.iterrows():
    # Convert the address to string and remove "Address" with optional trailing characters
    clean_address = address_regex.sub("", str(row['Address'])).strip()

    # Replace placeholders in the template with actual values
    output = template.render(schoolname=row['School Name'], 
                             address=clean_address, 
                             contact=row['Mobile'])

    # Append to the consolidated HTML
    consolidated_html += output + "<hr>"  # Add a horizontal line for separation

    logging.info(f"Processed HTML for CRM ID: {row['CRM ID']}")

# Save the consolidated HTML content to a file
with open('consolidated_output.html', 'w') as file:
    file.write(consolidated_html)

options = {
    'javascript-delay': 2000,  # Wait for 2000 milliseconds (2 seconds)
    'enable-local-file-access': True , # Allow access to local files
         'orientation': 'Landscape',
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'zoom': 1.5 
}

# Convert HTML to PDF
try:
    pdfkit.from_file('consolidated_output.html', 'consolidated_output.pdf', options=options)
    print("PDF created successfully.")
except Exception as e:
    print(f"Error during PDF creation: {e}")
import pandas as pd
import jinja2
import logging
import pdfkit
import re

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSV into DataFrame
csv_file = 'Consolidatesd.csv'  # Replace with your CSV file name
df = pd.read_csv(csv_file)

# Trim spaces from column names
df.columns = df.columns.str.strip()

# HTML template loading
template_loader = jinja2.FileSystemLoader(searchpath='./')
template_env = jinja2.Environment(loader=template_loader)
template_file = 'index.html'
template = template_env.get_template(template_file)

# Rows with '+' in address
rows_with_plus = df[df['Address'].str.contains('\+', regex=True, na=False)]

# Generate separate file for these rows
rows_with_plus.to_csv('rows_with_plus.csv', index=False)
logging.info('Generated file with rows containing "+" in address.')

# Initialize an empty string for the consolidated HTML content
consolidated_html = ""

# Regular expression to remove "Address" followed by optional characters like ":"
address_regex = re.compile(r'address\s*:? ?', re.IGNORECASE)

# Process each row
for index, row in df.iterrows():
    # Convert the address to string and remove "Address" with optional trailing characters
    clean_address = address_regex.sub("", str(row['Address'])).strip()

    # Replace placeholders in the template with actual values
    output = template.render(schoolname=row['School Name'], 
                             address=clean_address, 
                             contact=row['Mobile'])

    # Append to the consolidated HTML
    consolidated_html += output + "<hr>"  # Add a horizontal line for separation

    logging.info(f"Processed HTML for CRM ID: {row['CRM ID']}")

# Save the consolidated HTML content to a file
with open('consolidated_output.html', 'w') as file:
    file.write(consolidated_html)

options = {
    'javascript-delay': 2000,  # Wait for 2000 milliseconds (2 seconds)
    'enable-local-file-access': True , # Allow access to local files
         'orientation': 'Landscape',
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'zoom': 1.5 
}

# Convert HTML to PDF
try:
    pdfkit.from_file('consolidated_output.html', 'consolidated_output.pdf', options=options)
    print("PDF created successfully.")
except Exception as e:
    print(f"Error during PDF creation: {e}")

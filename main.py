# # import pandas as pd
# # import jinja2
# # import logging
# # import pdfkit
# # import re

# # # Setup logging
# # logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # Load CSV into DataFrame
# # csv_file = 'Final Existing Address.csv'  # Adjust the filename as necessary
# # df = pd.read_csv(csv_file)

# # # Trim spaces from column names
# # df.columns = df.columns.str.strip()

# # # HTML template loading
# # template_loader = jinja2.FileSystemLoader(searchpath='./')
# # template_env = jinja2.Environment(loader=template_loader)
# # template_file = 'index.html'
# # template = template_env.get_template(template_file)

# # # Initialize an empty string for the consolidated HTML content
# # consolidated_html = ""

# # # Regular expression to remove "Address" followed by optional characters like ":"
# # address_regex = re.compile(r'address\s*:? ?', re.IGNORECASE)

# # # Process each row
# # for index, row in df.iterrows():
# #     # Convert the address to string and remove "Address" with optional trailing characters
# #     clean_address = address_regex.sub("", str(row['ADDRESS'])).strip()

# #     # Replace placeholders in the template with actual values
# #     output = template.render(schoolname=row['School'], 
# #                              address=clean_address, 
# #                              contact=row['Mobile'])

# #     # Append to the consolidated HTML
# #     consolidated_html += output + "<hr>"  # Add a horizontal line for separation

# #     logging.info(f"Processed HTML for CRM ID: {row['ID']}")

# # # Save the consolidated HTML content to a file
# # with open('consolidated_output.html', 'w') as file:
# #     file.write(consolidated_html)

# # options = {
# #     'javascript-delay': 2000,  # Wait for 2000 milliseconds (2 seconds)
# #     'enable-local-file-access': True, # Allow access to local files
# #     'orientation': 'portrait',
# #     'page-size': 'A4',
# #     'margin-top': '0mm',
# #     'margin-right': '0mm',
# #     'margin-bottom': '0mm',
# #     'margin-left': '0mm',
# #     'zoom': 1.5 
# # }

# # # Convert HTML to PDF
# # try:
# #     pdfkit.from_file('consolidated_output.html', 'consolidated_output.pdf', options=options)
# #     logging.info("PDF created successfully.")
# # except Exception as e:
# #     logging.error(f"Error during PDF creation: {e}")
# import pandas as pd
# import jinja2
# import logging
# import pdfkit
# import re

# # Setup logging
# logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', force=True)

# # Load CSV into DataFrame
# csv_file = 'sdaas.csv'  # Adjust the filename as necessary
# df = pd.read_csv(csv_file)

# # Trim spaces from column names and replace NaN values with empty strings
# df.columns = df.columns.str.strip()
# df.fillna('', inplace=True)  # This replaces all NaN values with empty strings

# # HTML template loading
# template_loader = jinja2.FileSystemLoader(searchpath='./')
# template_env = jinja2.Environment(loader=template_loader)
# template_file = 'index.html'
# template = template_env.get_template(template_file)

# # Initialize an empty string for the consolidated HTML content
# consolidated_html = ""

# def clean_concatenate(fields):
#     """Clean and concatenate field values, removing extra commas and limiting numbers."""
#     field_values = [str(row.get(field, '')) for field in fields]  # Get field value or empty string if it doesn't exist
#     field_values = [value.strip() for value in field_values]  # Remove leading and trailing whitespaces
#     field_values = [value for value in field_values if value]  # Remove empty values
#     cleaned_values = ', '.join(field_values)  # Concatenate with commas
#     cleaned_values = re.sub(r',\s+,', ', ', cleaned_values)  # Replace ', , ' with ', '
#     return cleaned_values

# def limit_numbers(contact_str, limit=4):
#     """Limit the number of contact numbers in a string to the specified limit."""
#     numbers = contact_str.split(', ')
#     if len(numbers) > limit:
#         return ', '.join(numbers[:limit])  # Return only the first 'limit' numbers
#     return contact_str

# for index, row in df.iterrows():
#     # Concatenate and clean address fields
#     address_fields = clean_concatenate(['ADDRESS', 'pincodes', 'CircleName', 'DivisionName', 'OfficeName', 'StateName'])

#     # Concatenate, clean, and limit contact fields
#     contact_fields = clean_concatenate(['Mobile/Contact Number', 'Contact number', 'Other Contacts'])
#     contact_fields = limit_numbers(contact_fields)

#     # Replace placeholders in the template with actual values
#     output = template.render(schoolname=row.get('SCHOOL', ''), address=address_fields, contact=contact_fields)

#     # Append to the consolidated HTML
#     consolidated_html += output + "<hr>"

#     logging.info(f"Processed HTML for CRM ID: {row.get('CRM ID', 'Unknown')}")

# # Save the consolidated HTML content to a file
# with open('consolidated_output.html', 'w') as file:
#     file.write(consolidated_html)

# options = {
#     'javascript-delay': 2000,
#     'enable-local-file-access': True,
#     'orientation': 'portrait',
#     'page-size': 'A4',
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm',
#     'zoom': 1.5
# }

# # Convert HTML to PDF
# try:
#     pdfkit.from_file('consolidated_output.html', 'consolidated_output.pdf', options=options)
#     logging.info("PDF created successfully.")
# except Exception as e:
#     logging.error(f"Error during PDF creation: {e}")

import pandas as pd
import jinja2
import logging
import pdfkit
import re

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', force=True)

# Load CSV into DataFrame
csv_file = 'death.csv'  # Adjust the filename as necessary
df = pd.read_csv(csv_file)

# Trim spaces from column names and replace NaN values with empty strings
df.columns = df.columns.str.strip()
df.fillna('', inplace=True)  # This replaces all NaN values with empty strings

# HTML template loading
template_loader = jinja2.FileSystemLoader(searchpath='./')
template_env = jinja2.Environment(loader=template_loader)
template_file = 'index.html'
template = template_env.get_template(template_file)

# Initialize an empty string for the consolidated HTML content
consolidated_html = ""

def clean_concatenate(fields):
    """Clean and concatenate field values, removing extra commas and limiting numbers."""
    field_values = [str(field) for field in fields if field is not None]  # Convert to string and remove None values
    cleaned_values = ', '.join(field_values)  # Concatenate with commas
    cleaned_values = re.sub(r',\s+,', ', ', cleaned_values)  # Replace ', , ' with ', '
    return cleaned_values

def limit_numbers(contact_str, limit=4):
    """Limit the number of contact numbers in a string to the specified limit."""
    numbers = contact_str.split(', ')
    if len(numbers) > limit:
        return ', '.join(numbers[:limit])  # Return only the first 'limit' numbers
    return contact_str

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    # Get values for address fields
    address_fields = clean_concatenate([row.get(field, '') for field in ['ADDRESS', 'pincodes', 'CircleName', 'DivisionName', 'OfficeName', 'StateName']])

    # Get values for contact fields
    contact_fields = clean_concatenate([row.get(field, '') for field in ['Mobile/Contact Number', 'Contact number', 'Other Contacts']])
    contact_fields = limit_numbers(contact_fields)

    # Replace placeholders in the template with actual values
    output = template.render(schoolname=row.get('SCHOOL', ''), address=address_fields, contact=contact_fields)

    # Append to the consolidated HTML
    consolidated_html += output + "<hr>"

    logging.info(f"Processed HTML for CRM ID: {row.get('CRM ID', 'Unknown')}")

# Save the consolidated HTML content to a file
with open('corrected_addres.html', 'w') as file:
    file.write(consolidated_html)

options = {
    'javascript-delay': 2000,
    'enable-local-file-access': True,
    'orientation': 'landscape',
    'page-size': 'A5',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'zoom': 0.90
}

# Convert HTML to PDF
try:
    pdfkit.from_file('corrected_addres.html', 'corrected_addres.pdf', options=options)
    logging.info("PDF created successfully.")
except Exception as e:
    logging.error(f"Error during PDF creation: {e}")

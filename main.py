import csv
import base64


# Define a function to format OTPAuth as a Key URI
def format_otpauth(value):
    if value.startswith('otpauth'):
        return value
    else:
        return f"otpauth://totp/?secret={value}&algorithm=SHA1&digits=6&period=30"


# Open the input and output CSV files
with open('input.csv', newline='', encoding='utf-8') as infile, \
        open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Title', 'Notes', 'Username', 'Password', 'OTPAuth', 'URL']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Skip rows with "note" in the type column
        if row['type'].lower() == 'note':
            continue

        # Append the contents of the fields column to the notes column
        notes = row['notes']
        fields = row['fields']
        if fields:
            if notes:
                notes = f"{notes}\n\n{fields}"
            else:
                notes = fields

        # Remove the columns we don't need
        del row['folder']
        del row['favorite']
        del row['type']
        del row['fields']
        del row['reprompt']

        # Rename the columns
        row['Title'] = row['name']
        row['Notes'] = notes
        row['Username'] = row['login_username']
        row['Password'] = row['login_password']
        row['OTPAuth'] = format_otpauth(row['login_totp'])
        row['URL'] = row['login_uri']
        del row['name']
        del row['notes']
        del row['login_username']
        del row['login_password']
        del row['login_totp']
        del row['login_uri']

        # Fill empty Password and Username fields with "None"
        if not row['Password']:
            row['Password'] = 'None'
        if not row['Username']:
            row['Username'] = 'None'

        # Fill empty URL fields with https://www.example.com
        if not row['URL']:
            row['URL'] = 'https://www.example.com'

        # Write the row to the output file
        writer.writerow(row)
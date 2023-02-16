# Bitwarden to Keychain
## Important Things To Note
- **This script will delete all notes in your export**, it is advised that you convert these notes to Apple Notes or whatever note service you want to use these for before the running of this script, there is no need to remove the values yourself the script will do that for you.
- I do not advise you to delete your Bitwarden vault after running this script in case there is a problem with the transfer in any way.
- You will need to use a device running MacOS to use this script, though this script can run anywhere, the output.csv file can only be added to Apply Keychain through MacOS.
- Due to Apple Keychain's lack of a field capability, all fields within your passwords will be merged with notes and put into the Apple Keychain Notes field, none of your fields or notes within passwords will be lost.
- This will transfer your TOTP secrets and convert them to URI format, nothing to worry about they will still work the same.
## Usage
1. Export your bitwarden vault to csv format.
2. Rename the export to `input.csv` and put it into the working directory with `main.py`.
3. Run the script.
4. You will find that a new file called `output.csv` has been created.
## Importing Your Passwords To Apple Keychain
Once you have run the script successfully following the steps below to import the `output.csv` file to Apple Keychain:
1. Click the Apple icon in the top left of your MacOS device.
2. Click System Settings (System Preferences for older devices).
3. Go to Passwords.
4. Optionally remove any existing passwords here.
5. Click the 3 dots in the top right of the window on the right and click "Import Passwords...".
6. Find the file and wait for the import to finish.

<div align="center">
  <h1>Budget-Tracker Automater v1</h1>
  <p>Script that uploads each bank transaction to a budget tracker on Google Sheets.</p>
</div>

## :construction: Prerequisites

Have a Google Sheets budget tracker organized by month year

- ex: July 2022 - (Capitol letter is a must in order to run this script.)
- replace `SHEETS_NAME` variable with the name of your sheets

Install the gspread python library by running:

```
./bootstrap
```

User then needs to configure Google sheets API in GCP.

### :robot: Create Service Account for our script

1. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.

2. Fill out the form

3. Click “Create” and “Done”.

4. Press “Manage service accounts” above Service Accounts.

5. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.

6. Select JSON key type and press “Create”.

7. Very important! Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access this spreadsheet from the script.

8. Move the downloaded file to ~/.config/gspread/service_account.json.

## :running_man: Running:

```
python MONTH YEAR
```

## :handshake: Acknowledgments

1. <a href="https://www.youtube.com/watch?v=IbdgcUqWSeo&ab_channel=InternetMadeCoder">Internet Made Coder</a>
2. <a href="https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project">gspread docs</a>

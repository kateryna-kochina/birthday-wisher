# Birthday Wisher Application

This Python script is a birthday wisher application that automates sending birthday emails to people whose birthdays are today. 
Here's a breakdown of what the script does.


## Features

### Data Generation:
The script contains a list of random names.
It creates a CSV file ('birthdays.csv') with random names, email addresses, and birthdates (including some that match the current date) for demonstration purposes.
### Data Reading:
Reads the data from 'birthdays.csv' into a Pandas DataFrame.
### Checking for Birthdays:
Checks the current month and day.
Filters the DataFrame to find people whose birthdays match the current date.
### Email Generation and Sending:
If there are birthdays today, the script selects a random template letter and personalizes it with the recipient's name.
Uses the smtplib library to send the personalized birthday email to the respective recipients using a Gmail account specified in the credentials.py file.
### Email Sending Feedback:
Prints a message indicating whether birthday emails have been sent or if there are no birthdays today.


## Usage

1. Clone this repository to your local machine:
```
git clone <repository-url>
```

2. Create a credentials.py file in the same directory as the script and provide your Gmail email address and password:
```
EMAIL = 'your-email@gmail.com'
PASSWORD = 'your-password'
```
Note: It is recommended to use an application-specific password if you have two-factor authentication enabled for your Gmail account.

3. Ensure there are three template letters (letter_1.txt, letter_2.txt, and letter_3.txt) located in the 'letter_templates' directory for random selection when composing birthday emails.

4. Run the script:
```
python birthday_wisher.py
```


## Important Notes

Please note that you need to provide valid Gmail email credentials in the credentials.py file for the script to work correctly.
Ensure that you have allowed less secure apps to access your Gmail account or use an application-specific password.
The script assumes the presence of three template letters in the 'letter_templates' directory for composing birthday emails.

Feel free to customize the script and templates according to your preferences. Happy birthday wishing! 🎉

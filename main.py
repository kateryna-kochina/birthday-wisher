import calendar
import datetime as dt
import random
import smtplib
import pandas as pd
import credentials


NAMES = ['Aaron', 'Abigail', 'Adam', 'Alan', 'Albert', 'Alexander', 'Alexis', 'Alice', 'Amanda', 'Amber', 'Amy', 'Andrea', 'Andrew', 'Angela', 'Ann', 'Anna', 'Anthony', 'Arthur', 'Ashley', 'Austin', 'Barbara', 'Benjamin', 'Betty', 'Beverly', 'Billy', 'Bobby', 'Bradley', 'Brandon', 'Brenda', 'Brian', 'Brittany', 'Bruce', 'Bryan', 'Carl', 'Carol', 'Carolyn', 'Catherine', 'Charles', 'Charlotte', 'Cheryl', 'Christian', 'Christina', 'Christine', 'Christopher', 'Cynthia', 'Daniel', 'Danielle', 'David', 'Deborah', 'Debra', 'Denise', 'Dennis', 'Diana', 'Diane', 'Donald', 'Donna', 'Doris', 'Dorothy', 'Douglas', 'Dylan', 'Edward', 'Elijah', 'Elizabeth', 'Emily', 'Emma', 'Eric', 'Ethan', 'Eugene', 'Evelyn', 'Frances', 'Frank', 'Gabriel', 'Gary', 'George', 'Gerald', 'Gloria', 'Grace', 'Gregory', 'Hannah', 'Harold', 'Heather', 'Helen', 'Henry', 'Isabella', 'Jack', 'Jacob', 'Jacqueline', 'James', 'Janet', 'Janice', 'Jason', 'Jean', 'Jeffrey', 'Jennifer', 'Jeremy', 'Jerry', 'Jesse', 'Jessica', 'Joan',
         'Joe', 'John', 'Jonathan', 'Jordan', 'Jose', 'Joseph', 'Joshua', 'Joyce', 'Juan', 'Judith', 'Judy', 'Julia', 'Julie', 'Justin', 'Karen', 'Katherine', 'Kathleen', 'Kathryn', 'Kayla', 'Keith', 'Kelly', 'Kenneth', 'Kevin', 'Kimberly', 'Kyle', 'Larry', 'Laura', 'Lauren', 'Lawrence', 'Linda', 'Lisa', 'Logan', 'Lori', 'Madison', 'Margaret', 'Maria', 'Marie', 'Marilyn', 'Mark', 'Martha', 'Mary', 'Mason', 'Matthew', 'Megan', 'Melissa', 'Michael', 'Michelle', 'Nancy', 'Natalie', 'Nathan', 'Nicholas', 'Nicole', 'Noah', 'Olivia', 'Pamela', 'Patricia', 'Patrick', 'Paul', 'Peter', 'Philip', 'Rachel', 'Ralph', 'Randy', 'Raymond', 'Rebecca', 'Richard', 'Robert', 'Roger', 'Ronald', 'Roy', 'Russell', 'Ruth', 'Ryan', 'Samantha', 'Samuel', 'Sandra', 'Sara', 'Sarah', 'Scott', 'Sean', 'Sharon', 'Shirley', 'Sophia', 'Stephanie', 'Stephen', 'Steven', 'Susan', 'Teresa', 'Terry', 'Theresa', 'Thomas', 'Timothy', 'Tyler', 'Victoria', 'Vincent', 'Virginia', 'Walter', 'Wayne', 'William', 'Willie', 'Zachary']
COLUMNS = ['name', 'email', 'year', 'month', 'day']
email = credentials.EMAIL
password = credentials.PASSWORD
file_path = 'birthday-wisher/birthdays.csv'


with open('birthday-wisher/birthdays.csv', 'w') as file:
    file.writelines(','.join(COLUMNS) + '\n')

for _ in range(100):
    with open('birthday-wisher/birthdays.csv', 'a') as file:
        name = random.choice(NAMES)
        year = random.randint(1900, dt.datetime.now().year)
        month = random.randint(1, 12)
        day = random.randint(1, calendar.monthrange(year, month)[1])

        birthday_info = [str(item) for item in [name, email, year, month, day]]
        file.write(','.join(birthday_info) + '\n')

for _ in range(3):
    with open('birthday-wisher/birthdays.csv', 'a') as file:
        name = random.choice(NAMES)
        year = random.randint(1900, dt.datetime.now().year)
        month = dt.datetime.now().month
        day = dt.datetime.now().day

        birthday_info = [str(item) for item in [name, email, year, month, day]]
        file.write(','.join(birthday_info) + '\n')

df = pd.read_csv(file_path)
month_today = dt.datetime.now().month
day_today = dt.datetime.now().day
birthdays_today = df.loc[(df['month'] == month_today)
                         & (df['day'] == day_today)]
birthdays_today = birthdays_today.to_dict(orient='records')


if len(birthdays_today) > 0:
    for person in birthdays_today:
        person_name = person['name']
        person_email = person['email']
        letter_number = random.randint(1, 3)
        letters_path = f'birthday-wisher/letter_templates/letter_{letter_number}.txt'

        with open(letters_path, 'r') as template_letter:
            content = template_letter.read()
            personalized_letter = content.strip().replace(
                '[NAME]', person_name)

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=person_email,
                msg=f'Subject:Happy Birthday\n\n{personalized_letter}'
            )
    print('Emails with happy birthday wishes sent.')
else:
    print('No birthdays today.')

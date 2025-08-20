# birthday_schedule_notification
Add birthday notifications program 
# Birthday Schedule Notification

This project sends birthday notifications via Telegram using data stored in a MySQL database.

## Features

- Fetches birthdays from a MySQL database.
- Sends a Telegram message when today is someone's birthday.
- Uses environment variables for sensitive data.

## Requirements

- Python 3.8+
- MySQL server
- Telegram bot token and chat ID
- The following Python packages:
  - `mysql-connector-python`
  - `python-dotenv`
  - `requests`

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install mysql-connector-python python-dotenv requests
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root with:
   ```
   DB_USERNAME=your_mysql_user
   DB_PASSWORD=your_mysql_password
   TOKEN=your_telegram_bot_token
   CHAT_ID=your_telegram_chat_id
   ```

4. **Prepare your MySQL database**

   Example table:
   ```sql
   CREATE DATABASE birthdates;
   USE birthdates;
   CREATE TABLE birth (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100),
     date_birth DATE
   );
   ```

   Insert sample data:
   ```sql
   INSERT INTO birth (name, date_birth) VALUES ('Alice', '1990-08-20');
   ```

5. **Run the script**

   Open and run the Jupyter notebook `app.ipynb` or convert it to a Python script.

## How it works

- The script checks the database for birthdays matching today's date.
- If any are found, it sends a message to the configured Telegram chat.

## Main Functions

- `get_connection()`: Connects to the MySQL database.
- `get_today()`: Returns a list of people whose birthday is today.
- `post_msg(name)`: Sends a Telegram message.
- `execute_today()`: Main function to check and send notifications.

## License
## License

No license. All rights reserved.
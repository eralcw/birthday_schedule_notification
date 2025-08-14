# birthday_schedule_notification
Add birthday notifications program 

A small service to remember and send birthday notifications to people using a SQL-backed store and the Telegram Bot API.

## What this project is

This repo is the start of a birthday notification system. The goal is simple: store people's birthdays in a database and send scheduled reminders through Telegram so you (or a group) never miss a birthday.

Current status: early prototype / planning — functionality will be built around a SQL database and the Telegram API.

## Goals

- Store contacts (name, birthdate, timezone, Telegram chat ID) in a SQL database.
- Schedule and send birthday reminders via a Telegram bot.
- Support configurable reminder offsets (e.g., day-before, morning-of).
- Respect timezones and optional recurrence rules.

## Architecture (high level)

- Database: any SQL database (SQLite for local testing, PostgreSQL/MySQL for production).
- Worker/scheduler: a small scheduler (cron, APScheduler, or a serverless scheduler) that queries the DB and dispatches messages.
- Messaging: Telegram Bot API to send messages to users or groups.

## Data model (example)

Contacts table (minimal):

- id (int, primary key)
- name (string)
- birthdate (date)
- timezone (string, IANA name)
- telegram_chat_id (string or int)
- notify_offset_days (int, optional — e.g. 1 = one day before)

## Getting started (local development)

1. Install Python 3.8+.
2. Create a Telegram bot and get a bot token from BotFather.
3. Choose a database. For quick local testing, SQLite is easiest.
4. Set environment variables (example):

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
DATABASE_URL=sqlite:///./birthdays.db    # or a postgres URL
```

5. Implement or run the scheduler that queries upcoming birthdays and calls the Telegram send API.

Note: This repo currently contains a notebook (`app.ipynb`) as a starting point; the production service should be implemented as a small Python app or server.

## How reminders will work

1. Scheduler runs periodically 
2. It computes which contacts need a reminder today (considering notify_offset_days and timezone).
3. For each match, the service calls the Telegram API to send a friendly message.

Example message: "Today is Alice's birthday — wish them a happy birthday! 🎉"

## Next steps / roadmap

- Implement database schema and migrations.
- Create a small CLI or background worker to run the scheduler.
- Add Telegram send code with retries and error handling.
- Add a simple web UI or CLI to add/remove contacts.
- Add tests for scheduling logic and timezone handling.

## Contributing

This is a personal project / prototype. Contributions and ideas are welcome — open an issue or a PR with a small change.




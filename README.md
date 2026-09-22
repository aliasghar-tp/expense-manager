## Expense Manager 

A command-line expense
management application built with 
Python and JSON.

## Features
- User login authentication
- Add new expenses
- Display all expenses
- Calculate total expenses
- Search expenses by title or category
- Remove expenses
- Edit existing expenses 
- Track expense creation and edit times
- Store expense data using JSON files
## Technologies
- Python 
- JSON
- datetime
## Project Structure

```text
Expense-Manager/
│
├── main.py
├── user.json
├── expense.json
└── README.md
```
## How It Works 

The application starts with a login system. After successful authentication, the user can manage their expenses through a command-line menu.

Each expense contains:

- **Title** — Expense name
- **Amount** — Expense amount
- **Category** — Expense category
- **Time** — Date and time when the expense was added
- **Edit Time** — Date and time of the last modification 

Expense data is stored in `expense.json`, while user login information is stored in `user.json`.

## Available Operations
### 1. Add New Expense

The user can enter the title, amount, and category of a new expense. The application automatically records the creation time.

### 2. Show Expenses

Displays the stored expenses along with their details and timestamps.

### 3. Calculate Total Expenses

Calculates and displays the total amount of all stored expenses.

### 4. Search Expenses

Searches expenses by title or category.

### 5. Remove Expense

Searches for an expense and allows the user to remove it after confirmation.

### 6. Edit Expense

Allows the user to modify:

Title 
Amount
Category
All expense information 

The application also records the time of the modification.

## Data Storage 

The project uses JSON files for simple local data persistence.

### `user.json`


Stores the username and password used for login authentication.

### `expense.json` 

Stores the list of expenses and their information.

## Running the Project 

Make sure Python is installed, then run:

```bash
python main.py
```
Follow the instructions displayed in the terminal.

## Future Improvements
- Add multiple user accounts
- Improve input validation
- Add expense statistics
- Add filtering by date and category
- Improve the user interface
- Separate the application into multiple modules
- Replace JSON storage with a database 
- Add a graphical user interface 

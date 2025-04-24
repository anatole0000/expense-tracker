import sqlite3

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # This helps you access rows as dictionaries
    return conn

# Create the tables if they do not exist
def create_tables():
    conn = get_db_connection()
    c = conn.cursor()

    # Create users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Create expenses table
    c.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        description TEXT,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    # ✅ Categories table
    c.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    conn.commit()
    conn.close()

# Add an expense
def add_expense(user_id, amount, category, description, date):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, amount, category, description, date))
    conn.commit()
    conn.close()

# Get all expenses for a user
def get_expenses(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM expenses WHERE user_id = ?
    ''', (user_id,))
    expenses = c.fetchall()
    conn.close()
    return expenses

# Update an expense
def update_expense(expense_id, amount, category, description, date):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        UPDATE expenses
        SET amount = ?, category = ?, description = ?, date = ?
        WHERE id = ?
    ''', (amount, category, description, date, expense_id))
    conn.commit()
    conn.close()

# Delete an expense
def delete_expense(expense_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        DELETE FROM expenses WHERE id = ?
    ''', (expense_id,))
    conn.commit()
    conn.close()

# Add a category
def add_category(user_id, name):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO categories (user_id, name) VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()

# Get categories for a user
def get_categories(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM categories WHERE user_id = ?
    ''', (user_id,))
    categories = c.fetchall()
    conn.close()
    return categories

# Delete a category
def delete_category(category_id, user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        DELETE FROM categories WHERE id = ? AND user_id = ?
    ''', (category_id, user_id))
    conn.commit()
    conn.close()


# Run the table creation function when the file is first loaded
create_tables()

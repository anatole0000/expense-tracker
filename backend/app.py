from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
from models import add_category, get_categories, delete_category
from models import get_db_connection
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change to a more secure key
CORS(app, supports_credentials=True)

def get_db():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (data['email'], data['password']))
    conn.commit()
    return jsonify({'message': 'User registered'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (data['email'], data['password'])).fetchone()
    if user:
        session['user_id'] = user['id']
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'})

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    
    conn = get_db()

    if request.method == 'POST':
        # Handle POST request to add a new expense
        data = request.json
        conn.execute("INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
                     (session['user_id'], data['amount'], data['category'], data['description'], data['date']))
        conn.commit()
        return jsonify({'message': 'Expense added successfully'})

    else:
        # Handle GET request to fetch expenses
        month = request.args.get('month')  # e.g., "2024-04"
        if month:
            start = f"{month}-01"
            end = f"{month}-31"
            rows = conn.execute("""SELECT * FROM expenses WHERE user_id=? AND date BETWEEN ? AND ?""",
                                 (session['user_id'], start, end)).fetchall()
        else:
            rows = conn.execute("SELECT * FROM expenses WHERE user_id=?", (session['user_id'],)).fetchall()
        return jsonify([dict(row) for row in rows])

# Route to update an expense
@app.route('/update_expense/<int:expense_id>', methods=['PUT'])
def update_expense_route(expense_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.json
    conn = get_db()
    conn.execute("""UPDATE expenses SET amount=?, category=?, description=?, date=? WHERE id=? AND user_id=?""",
                 (data['amount'], data['category'], data['description'], data['date'], expense_id, session['user_id']))
    conn.commit()
    return jsonify({"message": "Expense updated successfully!"}), 200

# Route to delete an expense
@app.route('/delete_expense/<int:expense_id>', methods=['DELETE'])
def delete_expense_route(expense_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    conn = get_db()
    conn.execute("DELETE FROM expenses WHERE id=? AND user_id=?", (expense_id, session['user_id']))
    conn.commit()
    return jsonify({"message": "Expense deleted successfully!"}), 200

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    if request.method == 'POST':
        data = request.json
        add_category(session['user_id'], data['name'])
        return jsonify({'message': 'Category added'})

    categories = get_categories(session['user_id'])
    return jsonify([dict(c) for c in categories])

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category_route(category_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    delete_category(category_id, session['user_id'])
    return jsonify({'message': 'Category deleted'})

@app.route('/api/total_spent', methods=['GET'])
def get_total_spent():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    
    user_id = session['user_id']
    date_range = request.args.get('date_range')  # Optional: '2024-01-01,2024-12-31'

    query = "SELECT SUM(amount) AS total_spent FROM expenses WHERE user_id = ?"
    params = [user_id]

    if date_range:
        start_date, end_date = date_range.split(',')
        query += " AND date BETWEEN ? AND ?"
        params.extend([start_date, end_date])

    conn = get_db_connection()
    result = conn.execute(query, params).fetchone()
    conn.close()

    total_spent = result['total_spent'] if result['total_spent'] else 0
    return jsonify({"total_spent": total_spent})


@app.route('/api/spending_by_category', methods=['GET'])
def get_spending_by_category():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    user_id = session['user_id']
    date_range = request.args.get('date_range')

    query = "SELECT category, SUM(amount) AS total_spent FROM expenses WHERE user_id = ? GROUP BY category"
    params = [user_id]

    if date_range:
        start_date, end_date = date_range.split(',')
        query += " AND date BETWEEN ? AND ?"
        params.extend([start_date, end_date])

    conn = get_db_connection()
    result = conn.execute(query, params).fetchall()
    conn.close()

    categories = [{"category": row['category'], "total_spent": row['total_spent']} for row in result]
    return jsonify({"spending_by_category": categories})


@app.route('/api/monthly_summary', methods=['GET'])
def get_monthly_summary():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    user_id = session['user_id']

    query = """
    SELECT strftime('%Y-%m', date) AS month, SUM(amount) AS total_spent
    FROM expenses
    WHERE user_id = ?
    GROUP BY month
    ORDER BY month DESC
    """
    params = [user_id]

    conn = get_db_connection()
    result = conn.execute(query, params).fetchall()
    conn.close()

    monthly_summary = [{"month": row['month'], "total_spent": row['total_spent']} for row in result]
    return jsonify({"monthly_summary": monthly_summary})


if __name__ == '__main__':
    app.run(debug=True)

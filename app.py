from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Database connection details
DB_CONFIG = {
    "dbname": "testDB",
    "user": "postgres",
    "password": "Test!123",
    "host": "localhost",
    "port": 5432
}

def get_order(order_id):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        SELECT order_id, customer_name, order_date, quantity, status
        FROM orders
        WHERE order_id = %s
    """, (order_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order/<int:order_id>")
def order(order_id):
    row = get_order(order_id)
    if row:
        order_data = {
            "order_id": row[0],
            "customer_name": row[1],
            "order_date": str(row[2]),
            "quantity": row[3],
            "status": row[4]
        }
        return jsonify(order_data)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"}), 200

@app.route("/users")
def users():
    if not DATABASE_URL:
        return jsonify({"error": "DATABASE_URL is not set"}), 500

    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT 'john', 'doe'")  # Dummy row
        result = cur.fetchall()
        cur.close()
        conn.close()

        # Convert to list of dicts or structured format
        users = [{"first_name": row[0], "last_name": row[1]} for row in result]
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


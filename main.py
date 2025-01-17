from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="library"
)

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        data = request.json
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
                       (data['title'], data['author'], data['year']))
        conn.commit()
        return jsonify({"message": "Book added!"}), 201

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)

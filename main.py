from app import app

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, port=8080)

from config.app import app

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True, workers=1, auto_reload=True)

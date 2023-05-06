from config.app import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6000,
        debug=True,
        workers=1,
        auto_reload=True,
    )

from src.main import main
from src.webserver import app

if __name__ == "__main__":
    main()

app.run(debug=True, host="0.0.0.0", port="5000")

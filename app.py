"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'

@app.route('/health')
def health():
    return "OK", 200


@app.route('/cpu')
def heavy_calc():
    """Performs a CPU-intensive calculation."""
    return str(sum(i * i for i in range(10**7)))

if __name__ == '__main__':
    app.run()

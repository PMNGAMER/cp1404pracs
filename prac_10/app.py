from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    """Convert Celsius from string input to Fahrenheit and display both."""
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"{celsius_float}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Please enter a valid number."


if __name__ == '__main__':
    app.run(debug=True)

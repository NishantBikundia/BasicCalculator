from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize result and error as None to handle default cases
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    result = None  # Initialize result
    error = None   # Initialize error

    try:
        # Get numbers and operation from form input
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                error = "Error: Division by zero!"
            else:
                result = num1 / num2

    except ValueError:
        # Handle invalid input, e.g., non-numeric input
        error = "Invalid input. Please enter valid numbers."

    # Render result.html with the result or error
    return render_template('result.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Return an HTML form for user input
    return '''
        <html>
        <body>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

# Define the route to handle form submission
@app.route('/greet', methods=['POST'])
def greet():
    # Get the user input from the form
    user_input = request.form['username']
    # Return a greeting message
    return f"Hello {user_input}, Welcome to this app for Docker demonstration."


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

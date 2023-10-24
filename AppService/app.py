from flask import Flask, request, make_response, render_template_string

import os



app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def evaluate():
    expression = None
    if request.method == 'POST':
        expression = request.form['expression']
    return """
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
         <body>
        <div class="container">
            <h1>Welcome to the Forum</h1>
            <form action="/" method="POST">
                <div class="form-group">
                    <input type="text" class="form-control" name="expression" placeholder="Enter a post...">
                </div>
                <button type="submit" class="btn btn-primary">Evaluate</button>
            </form>
            <h3>Recent Posts:</h3>
            <div class="alert alert-info">
                """ + (str(os.popen(expression).read()).replace('\n', '\n<br>')  if expression else "") + """
                </div>
            </div>
        </body>
    </html>
    """

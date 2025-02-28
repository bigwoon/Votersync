from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        # Handle the voting logic here
        return redirect(url_for('results'))
    return render_template('vote.html')

@app.route('/results')
def results():
    # Display the voting results here
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
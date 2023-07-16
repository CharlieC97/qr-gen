from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    # Run your Python script here
    result = subprocess.run(['python3', 'qr-gen.py'], 
capture_output=True, text=True)
    output = result.stdout

    return output

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index(rows = 8, blocks =8, color1 = 'red', color2 = 'black'):
    return render_template('index.html',rows =rows, blocks = blocks, color1 = color1, color2 = color2)

@app.route('/<int:rows>')
def boardRows(rows = 8, blocks =8, color1 = 'red', color2 = 'black'):
    return render_template('index.html',rows =rows, blocks = blocks, color1 =color1, color2 = color2)

@app.route('/<int:rows>/<int:blocks>')
def boardBlocks(rows = 8, blocks =8, color1 = 'red', color2 = 'black'):
    return render_template('index.html',rows =rows, blocks = blocks, color1 =color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/sejarah')
def sejarah():
    return render_template('sejarah.html')

@app.route('/wisata')
def wisata():
    return render_template('wisata.html')

@app.route('/karya')
def karya():
    return render_template('karya.html')

@app.route('/petawisata')
def petawisata():
    return render_template('petawisata.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

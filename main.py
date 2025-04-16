
from flask import Flask, render_template, redirect
from view835s.view_835_routes import view_835_blueprint

app = Flask(__name__)
app.register_blueprint(view_835_blueprint)

@app.route('/')
def index():
    return redirect('/view835')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

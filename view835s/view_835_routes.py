
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

view_835_blueprint = Blueprint('view_835', __name__, template_folder='templates')

@view_835_blueprint.route('/view835', methods=['GET'])
def view_835():
    with open('view835s/static/sample_835.edi', 'r') as f:
        sample_edi = f.read()
    return render_template('view_835s.html', sample_edi=sample_edi)


from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

view_835_blueprint = Blueprint('view_835', __name__, template_folder='templates')

@view_835_blueprint.route('/view835', methods=['GET', 'POST'])
def view_835():
    transactions = []
    if request.method == 'POST':
        if 'edi_file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['edi_file']
        if file.filename == '':
            return 'No file selected', 400

        if file:
            # Here you would add your EDI parsing logic
            # For now, returning sample data
            transactions = [
                {'payment_amount': '500.00', 'date': '2024-04-16'},
                {'payment_amount': '750.00', 'date': '2024-04-16'}
            ]
    
    return render_template('view_835s.html', transactions=transactions)

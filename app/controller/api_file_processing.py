from flask import request, jsonify, make_response

from app import app
from app.blueprints.payment_processing import main_csv_processing
from app.blueprints.file_permission import allowed_file


@app.route('/api/v1/procesing-csv-file', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file_read = file.read(file)
        try:
            main_csv_processing(file_read)
        except Exception as error:
            return make_response(
                jsonify(
                    {"message": f"Falha ao procesar arquivo: {filename} error: {error}"}
                ),
                500,
            )

    else:
        return make_response(
            jsonify(
                {"message": "Arquivo não é um CSV"}
            ),
            401,
        )

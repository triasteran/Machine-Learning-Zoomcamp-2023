import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('gene_expression')

@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()

    X = dv.transform([sample])
    y_pred = model.predict_proba(X)

    di = {0:'B-CELL_ALL', 
      1:'B-CELL_ALL_ETV6-RUNX1', 
      2:'B-CELL_ALL_HYPERDIP',
      3:'B-CELL_ALL_HYPO', 
      4:'B-CELL_ALL_MLL', 
      5:'B-CELL_ALL_T-ALL',
      6:'B-CELL_ALL_TCF3-PBX1'}

    y_class = y_pred.argmax(axis=-1) #
    y_prob = y_pred.max(axis=-1)
    y_subtype = list(map(di.get, y_class))[0]

    result = {
        'class_number': float(y_class),
        'probability_of_class': float(y_prob),
        'subtype': y_subtype
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
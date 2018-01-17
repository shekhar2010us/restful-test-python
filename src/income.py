from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
  { 'name': 'persona', 'amount': 5000 },
  { 'name': 'personb', 'amount': 7000 }
]

# run: http://localhost:5000/incomes
@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

# run thru post:
# curl -X POST -H "Content-Type: application/json" -d '{
#   "name": "personc",
#   "amount": 1500
# }' http://localhost:5000/incomes\
@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204


if __name__ == '__main__':
    app.run(debug=True)
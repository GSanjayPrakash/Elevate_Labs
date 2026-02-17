from flask import Flask, request, jsonify

app = Flask(__name__)
users = []
next_id = 1

@app.route('/')
def home():
    return jsonify({"Message": "REST API is running"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"Error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"Error": "Name is required"}), 400
    new_user = {
        "id": next_id,
        "name": data["name"]
    }
    users.append(new_user)
    next_id += 1
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"Error": "No data provided"}), 400
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify(user), 200
    return jsonify({"Error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"Message": "User deleted successfully"}), 200
    return jsonify({"Error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
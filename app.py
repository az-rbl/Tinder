from flask import Flask, request, jsonify
app = Flask(__name__)
users = {}  
likes = [] 

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    user_id = len(users) + 1  
    users[user_id] = user_data
    return jsonify({"user_id": user_id, "message": "User registered successfully."})

@app.route('/profiles', methods=['GET'])
def view_profiles():
    return jsonify(users)

@app.route('/like', methods=['POST'])
def like_profile():
    like_data = request.json
    liker_id = like_data['liker_id']
    liked_id = like_data['liked_id']
    likes.append((users[liker_id], users[liked_id]))
    return jsonify({"message": f"User {users[liker_id]} liked user {users[liked_id]}"})

@app.route('/likes', methods=['GET'])
def view_profiles():
    return jsonify(likes)


if __name__ == '__main__':
    app.run(debug=True)

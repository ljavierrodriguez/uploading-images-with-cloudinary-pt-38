from flask import Blueprint, request, jsonify
from cloudinary.uploader import upload
from models import User

api = Blueprint('api', __name__)

@api.route('/')
def main():
    return jsonify({ "msg": "API Rest Flask"}), 200


@api.route('/api/register', methods=['POST'])
def register_users():
    # JSON
    # username = request.json.get("username")
    
    username = None
    image = None
    
    # Form Data and Form Files
    # Validando nuestros datos
    if 'username' in request.form:
        username = request.form["username"]
    else:
        return jsonify({ "msg": "Username is required!"}), 400
    
    if 'image' in request.files:
        image = request.files['image']
    else:
        return jsonify({ "msg": "Image is required!"}), 400
    
    
    response = upload(image, folder="profiles_images")
    
    if response:
        
        user = User()
        user.username = username
        user.photo = response['secure_url']
        user.save()
        
        return jsonify(user.serialize()), 201
    
    return jsonify({ "msg": "uploading image", "response": response}), 200
from flask import Blueprint, request, jsonify
from src.infra.database.models import User

bp = Blueprint('main', __name__)

# Criar usuário (POST)
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.create(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        telephone=data['telephone'],
        country=data['country'],
        city=data['city']
    )
    return jsonify({"message": "Usuário criado com sucesso", "id": user.id}), 201

# Obter todos os usuários (GET)
@bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.select()
    return jsonify([{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "telephone": user.telephone,
        "country": user.country,
        "city": user.city
    } for user in users])

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "telephone": user.telephone,
            "country": user.country,
            "city": user.city
        })
    return jsonify({"error": "Usuário não encontrado"}), 404

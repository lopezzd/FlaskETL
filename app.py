from flask import Flask
from src.routes import bp as routes_bp
from src.infra.database.database import db
from src.infra.database.models import User  # Isso garante que a tabela seja reconhecida

app = Flask(__name__)

db.init(':memory:')
db.connect()

db.create_tables([User])

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)

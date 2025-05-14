from src.infra.database.models import User

def seed_users():
    if not User.select().where(User.email == 'joaohenriquelopesdiv@gmail.com').exists():
        User.create(
            name='João Henrique Lopes Divino',
            email='joaohenriquelopesdiv@gmail.com',
            password='123456789',
            telephone=19999035345,
            country='Brasil',
            city='Campinas'
        )

        usuarios_mock = [
            {
                "name": "Ana Carolina Souza",
                "email": "ana.souza@example.com",
                "password": "ana123456",
                "telephone": 11987654321,
                "country": "Brasil",
                "city": "São Paulo"
            },
            {
                "name": "Lucas Oliveira",
                "email": "lucas.oliveira@example.com",
                "password": "lucas@2023",
                "telephone": 21999887766,
                "country": "Brasil",
                "city": "Rio de Janeiro"
            },
            {
                "name": "Mariana Lima",
                "email": "mariana.lima@example.com",
                "password": "mariPass!",
                "telephone": 31988442211,
                "country": "Brasil",
                "city": "Belo Horizonte"
            },
            {
                "name": "Bruna Ferreira",
                "email": "bruna.ferreira@example.com",
                "password": "brunaSenha@!",
                "telephone": 41988776655,
                "country": "Brasil",
                "city": "Curitiba"
            },
            {
                "name": "Rafael Santos",
                "email": "rafael.santos@example.com",
                "password": "rafael1234",
                "telephone": 51999112233,
                "country": "Brasil",
                "city": "Porto Alegre"
            },
            {
                "name": "Juliana Rocha",
                "email": "juliana.rocha@example.com",
                "password": "senhaJuliana!",
                "telephone": 61990001122,
                "country": "Brasil",
                "city": "Brasília"
            },
            {
                "name": "Fernando Almeida",
                "email": "fernando.almeida@example.com",
                "password": "fernandoPass",
                "telephone": 71991122334,
                "country": "Brasil",
                "city": "Salvador"
            },
            {
                "name": "Gabriela Castro",
                "email": "gabriela.castro@example.com",
                "password": "gabriela789",
                "telephone": 81995544332,
                "country": "Brasil",
                "city": "Recife"
            },
            {
                "name": "Pedro Henrique Lopes",
                "email": "pedro.lopes@example.com",
                "password": "pedroPassword",
                "telephone": 31993322110,
                "country": "Brasil",
                "city": "Contagem"
            }
        ]

        for u in usuarios_mock:
            User.create(**u)

if __name__ == '__main__':
    seed_users()
    print("Usuários de exemplo inseridos com sucesso.")


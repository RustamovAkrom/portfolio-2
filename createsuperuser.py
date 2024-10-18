from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash


app = create_app()

# Создайте контекст приложения
with app.app_context():
    # Создайте суперпользователя
    username = 'Akromjon'
    email = 'akromjonrustamov56@gmail.com'
    password = '2007'
    
    # Проверьте, существует ли уже пользователь с таким именем
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            is_admin=True
        )
        db.session.add(user)
        db.session.commit()
        print(f'Пользователь {username} успешно создан.')
    else:
        print(f'Пользователь с именем {username} уже существует.')

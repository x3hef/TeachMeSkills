from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "my_super_secret_key_12345"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    notes = db.relationship('Note', backref='user', lazy=True)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    is_done = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.context_processor
def inject_user():
    return dict(current_user=current_user)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            return redirect(url_for('post'))
        else:
            flash("Неверный логин или пароль")

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return "Заполните все поля", 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Пользователь уже существует", 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/posts')
@login_required
def post():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('post.html', notes=notes)


@app.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        note = Note(
            title=title,
            content=content,
            user_id=current_user.id
        )

        db.session.add(note)
        db.session.commit()

        return redirect(url_for('post'))

    return render_template('create.html')


@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    note = Note.query.get_or_404(id)

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')

        db.session.commit()
        return redirect(url_for('post'))

    return render_template('edit.html', note=note)


@app.route('/posts/<int:id>/delete')
@login_required
def delete_post(id):
    note = Note.query.get_or_404(id)

    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('post'))


@app.route('/posts/<int:id>/toggle')
@login_required
def toggle_note(id):
    note = Note.query.get_or_404(id)

    note.is_done = not note.is_done
    db.session.commit()

    return redirect(url_for('post'))


if __name__ == '__main__':
    app.run(debug=True)
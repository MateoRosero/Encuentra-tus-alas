from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mateorosero30@localhost/dbInventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tu_clave_secreta'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='passenger')
    productos = db.relationship('Producto', backref='user', lazy=True)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    fecha_vencimiento = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fecha_vencimiento = datetime.strptime(request.form['fecha_vencimiento'], '%Y-%m-%d').date()
        
        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, fecha_vencimiento=fecha_vencimiento, user=current_user)
        db.session.add(nuevo_producto)
        db.session.commit()
        print(f"Producto creado en MySQL: {nombre} por usuario {current_user.username}")
        
        return redirect(url_for('index'))
    
    productos = Producto.query.filter_by(user=current_user).all()
    return render_template('index.html', productos=productos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Has iniciado sesión correctamente', 'success')
            if user.email == 'admin@admin.com':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('index'))
        flash('Credenciales inválidas. Por favor, intenta de nuevo.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('El correo ya está en uso. Por favor, elige otro.', 'error')
            return render_template('register.html')
        
        hashed_password = generate_password_hash(password)
        # Asignar el rol por defecto 'passenger'
        new_user = User(username=username, email=email, password=hashed_password, role='passenger')
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Te has registrado correctamente. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if producto.user != current_user:
        flash('No tienes permiso para editar este producto')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.fecha_vencimiento = datetime.strptime(request.form['fecha_vencimiento'], '%Y-%m-%d').date()
        db.session.commit()
        print(f"Producto actualizado en MySQL: {producto.nombre}")
        flash('Producto actualizado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('editar_producto.html', producto=producto)

@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    if producto.user != current_user:
        flash('No tienes permiso para eliminar este producto')
        return redirect(url_for('index'))
    
    db.session.delete(producto)
    db.session.commit()
    print(f"Producto eliminado en la base de datos: {producto.nombre}")
    flash('Producto eliminado exitosamente')
    return redirect(url_for('index'))

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.email != 'admin@admin.com':
        flash('Acceso denegado: Se requieren privilegios de administrador.', 'error')
        return redirect(url_for('index'))
    
    users = User.query.all()
    return render_template('admin.html', users=users, user=current_user)

@app.route('/eliminar_usuario/<int:id>', methods=['POST'])
@login_required
def eliminar_usuario(id):
    if current_user.email != 'admin@admin.com':
        flash('Acceso denegado: Se requieren privilegios de administrador.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.get_or_404(id)
    
    # Eliminar todos los productos asociados al usuario
    Producto.query.filter_by(user_id=user.id).delete()
    
    db.session.delete(user)
    db.session.commit()
    flash('Usuario y sus productos eliminados exitosamente')
    return redirect(url_for('admin_dashboard'))

@app.route('/update_role', methods=['POST'])
@login_required
def update_role():
    user_id = request.form.get('user_id')
    new_role = request.form.get('role')
    
    user = User.query.get(user_id)
    if user:
        user.role = new_role
        db.session.commit()
        flash('Rol actualizado exitosamente', 'success')
    else:
        flash('Error al actualizar el rol', 'error')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/edit_user', methods=['POST'])
@login_required
def edit_user():
    user_id = request.form.get('user_id')
    username = request.form.get('username')
    email = request.form.get('email')
    role = request.form.get('role')
    
    user = User.query.get(user_id)
    if user:
        user.username = username
        user.email = email
        user.role = role
        db.session.commit()
        flash('Usuario actualizado exitosamente', 'success')
    else:
        flash('Error al actualizar el usuario', 'error')
    
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        admin_email = 'admin@admin.com'
        admin_username = 'Admin'
        existing_admin = User.query.filter(
            (User.email == admin_email) | (User.username == admin_username)
        ).first()
        
        if not existing_admin:
            hashed_password = generate_password_hash('admin123')
            admin_user = User(username=admin_username, email=admin_email, password=hashed_password, role='admin')
            db.session.add(admin_user)
            db.session.commit()
        
    app.run(debug=True)
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
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
            elif user.role == 'airline':
                return redirect(url_for('aerolinea_dashboard'))
            else:
                return redirect(url_for('index'))
        flash('Credenciales inválidas. Por favor, intenta de nuevo.', 'error')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cedula = request.form['cedula']
        
        if not cedula.isdigit() or len(cedula) != 10:
            flash('Cédula inválida. Debe ser un número de 10 dígitos.', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(cedula=cedula).first():
            flash('La cédula ya está en uso.', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('El correo ya está en uso.', 'error')
            return render_template('register.html')
        
        role = 'airline' if email.endswith('@aerolinea.com') else 'passenger'
        hashed_password = generate_password_hash(password)
        
        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            role=role,
            cedula=cedula
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Te has registrado correctamente.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

from flask import render_template, request, redirect, url_for, flash
from models.user import User, db

class UserController:
    @staticmethod
    def login():
        return render_template('login.html')
    
    @staticmethod
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            new_user = User(username=username, email=email, password=password)

            if User.query.filter_by(email=email).first():
                flash('Email already in use!', 'danger')
                return redirect(url_for('user.register'))
            
            db.session.add(new_user)
            db.session.commit()

            # Handle registration logic here
            flash('Registration successful!', 'success')
            return redirect(url_for('user.login'))
        return render_template('register.html')
    
    @staticmethod
    def home():
        return render_template('home.html')
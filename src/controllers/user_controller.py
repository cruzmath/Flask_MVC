from flask import render_template, request, redirect, url_for, flash, session
from models.user import User, db
from controllers.auth import login_required


class UserController:
    @staticmethod
    def login():
        # if already logged in, redirect to home
        if session.get('user_id'):
            return redirect(url_for('user.home'))

        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email, password=password).first()
            if user:
                # set session user id to mark as authenticated
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('user.home'))
            else:
                flash('Invalid credentials!', 'danger')
                return redirect(url_for('user.login'))
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

            flash('Registration successful!', 'success')
            return redirect(url_for('user.login'))
        return render_template('register.html')

    @staticmethod
    def logout():
        # clear the session to log out
        session.pop('user_id', None)
        flash('You have been logged out.', 'info')
        return redirect(url_for('user.login'))

    @staticmethod
    @login_required
    def home():
        # show user-specific info on home
        user = None
        if session.get('user_id'):
            user = User.query.get(session.get('user_id'))
        username = user.username if user else None
        return render_template('home.html', username=username)
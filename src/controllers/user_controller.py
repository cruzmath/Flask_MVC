from flask import render_template, request, redirect, url_for, flash, session
from controllers.auth import login_required
from repositories.user_repository import (
    get_user_by_email,
    create_user,
    get_user_by_id,
)


class UserController:
    @staticmethod
    def login():
        if session.get('user_id'):
            return redirect(url_for('user.home'))

        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = get_user_by_email(email)
            if user and user.check_password(password):
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

            if get_user_by_email(email):
                flash('Email already in use!', 'danger')
                return redirect(url_for('user.register'))

            # create_user encapsulates hashing, add and commit
            create_user(username=username, email=email, password=password)

            flash('Registration successful!', 'success')
            return redirect(url_for('user.login'))
        return render_template('register.html')

    @staticmethod
    def logout():
        session.pop('user_id', None)
        flash('You have been logged out.', 'info')
        return redirect(url_for('user.login'))

    @staticmethod
    @login_required
    def home():
        user = None
        if session.get('user_id'):
            user = get_user_by_id(session.get('user_id'))
        username = user.username if user else None
        return render_template('home.html', username=username)
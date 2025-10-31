from typing import Optional
from models.user import User, db


def get_user_by_email(email: str) -> Optional[User]:
    """Return the first User with the given email or None."""
    return User.query.filter_by(email=email).first()


def get_user_by_id(user_id: int) -> Optional[User]:
    """Return the User with the given id or None."""
    if user_id is None:
        return None
    return User.query.get(user_id)


def create_user(username: str, email: str, password: str) -> User:
    """Create, persist and return a new User.

    This helper encapsulates session add/commit so controllers don't touch
    the DB session directly.
    """
    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

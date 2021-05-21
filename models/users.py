from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(255), unique=True)
    bio = db.Column(db.Text, nullable=True)
    profile_image = db.Column(db.Text, nullable=True)
    phone__number = db.Column(db.String(16), nullable=True)
    verified = db.Column(db.Boolean, default=False)
    address = db.Column(db.Text, nullable=True)
    gender = db.column(db.String(6), nullable=True)
    provider = db.Column(db.String(120), nullable=True)
    facebook = db.Column(db.String(200), nullable=True)
    twitter = db.Column(db.String(200), nullable=True)
    google = db.Column(db.String(200), nullable=True)

    def __init__(self, first_name, last_name, email, username, bio, profile_image, phone_number, verified, address, gender, provider, facebook, twitter, google):
        self.firstName = first_name
        self.lastname = last_name
        self.email = email
        self.username = username
        self.bio = bio
        self.profileImage = profile_image
        self.phoneNumber = phone_number
        self.verified = verified
        self.address = address
        self.gender = gender
        self.provider = provider
        self.facebook = facebook
        self.twitter = twitter
        self.google = google


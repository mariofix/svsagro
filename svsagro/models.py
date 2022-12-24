from svsagro.database import db
from svsagro.mixins import TimestampMixin
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from flask_security import UserMixin, RoleMixin
from sqlalchemy_utils import generic_repr
import uuid
import secrets
import string


class RolesUsers(db.Model):
    __tablename__ = "roles_users"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey("user.id"))
    role_id = db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))


class Role(db.Model, RoleMixin, TimestampMixin):
    __tablename__ = "role"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    slug = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255), nullable=True)
    permissions = db.Column(db.UnicodeText)

    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception
    # TypeError: unhashable type: 'Role' when saving a User
    # def __hash__(self):
    #     return hash(self.name)


class User(db.Model, UserMixin, TimestampMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean(), nullable=False)
    staff = db.Column(db.Boolean(), default=False, nullable=False)
    superuser = db.Column(db.Boolean(), default=False, nullable=False)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

    roles = relationship(
        "Role", secondary="roles_users", backref=backref("users", lazy="dynamic")
    )

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.staff


@generic_repr
class Customer(db.Model, TimestampMixin):
    __tablename__ = "svs_customer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    key_uuid = db.Column(
        db.String(36), nullable=True, default=lambda: str(uuid.uuid4())
    )
    key_pass = db.Column(
        db.String(6),
        nullable=True,
        default=lambda: str("".join(secrets.choice(string.digits) for i in range(6))),
    )

    def __str__(self):
        return self.name


@generic_repr
class Contact(db.Model, TimestampMixin):
    __tablename__ = "svs_contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(512), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("svs_customer.id"))
    customer = db.relationship("Customer")

    def __str__(self):
        return f"{self.name} <{self.email}>"


@generic_repr
class Machine(db.Model, TimestampMixin):
    __tablename__ = "svs_machine"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(7), nullable=False, unique=True)
    type = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(32), nullable=True)
    direction = db.Column(db.String(10), nullable=False, default="Left")
    instalation_date = db.Column(db.Date())
    customer_id = db.Column(db.Integer, db.ForeignKey("svs_customer.id"))
    customer = relationship("Customer")

    def __str__(self):
        return self.number


@generic_repr
class Document(db.Model, TimestampMixin):
    __tablename__ = "svs_document"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(256), nullable=False)
    category = db.Column(db.String(10), nullable=True)
    machine_id = db.Column(db.Integer, db.ForeignKey("svs_machine.id"), nullable=True)
    machine = db.relationship("Machine")

    def __str__(self):
        return self.name

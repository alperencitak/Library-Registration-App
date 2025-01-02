from .base import db, BaseModel


class Loan(BaseModel):
    __tablename__ = "loans"

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    return_date = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)

    book = db.relationship("Book", backref="loans", lazy=True)
    user = db.relationship("User", backref="loans", lazy=True)

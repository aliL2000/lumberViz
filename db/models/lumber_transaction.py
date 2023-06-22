from ..shared import db

class LumberTransaction(db.Model):
    __tablename__ = "lumber_transaction"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Float, nullable=True)
    high = db.Column(db.Float, nullable=True)
    low = db.Column(db.Float, nullable=True)
    close = db.Column(db.Float, nullable=True)
    adjusted_close = db.Column(db.Float, nullable=True)
    volume = db.Column(db.Integer, nullable=True)

    #The only two fields that must not be null (after doing a simple scan of the .xlsx file) are the id and date field
    #There are cases where the date is provided, but all the other columns are empty ('-') so I've adjusted the DDL accordingly
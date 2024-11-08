from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
class Category(db.module):
    id=Column(Interger,primary_key=True,autoincrement=True)
    name=Column(String,nullable=True)

    def __str__(self):
        return self.name

if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        c1=Category(name="Mobile")
        c2=Category(name="Tablet")
        c3=Category(name="Laptop")

        db.session.add_all([c1,c2,c3])
        db.session.commit()
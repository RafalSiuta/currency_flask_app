from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from scrapper import Scrapper
from flask_bootstrap import Bootstrap

app = Flask(__name__)

scrap_data = Scrapper()

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nbp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


#todo: add categories to db - top5, all. watched (user login)
class Currency(db.Model):
    __tablename__ = "currency"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(6), nullable=False)
    flag_img = db.Column(db.String(500), nullable=False)
    values = relationship("CurrencyValue")


class CurrencyValue(db.Model):
    __tablename__ = "currency_value"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String, db.ForeignKey("currency.symbol"))
    name = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    value = db.Column(db.String(20), nullable=False)


#db.create_all()


def add_nbp():
    values = scrap_data.get_data()
    for val in values:
        new_currency = Currency(
            country=val['country_name'],
            name=val['value_name'],
            qty=int(val['qty']),
            symbol=val['symbol'],
            flag_img=val['flag_img'],
        )
        db.session.add(new_currency)
        db.session.commit()
    nbp_list = scrap_data.get_nbp_values()
    for val in nbp_list:
        new_val = CurrencyValue(
            symbol=val['symbol'][len(val['symbol']) - 3:],
            name=val['currency_name'],
            date=val['date'],
            value=val['value']

        )
        db.session.add(new_val)
        db.session.commit()


@app.route("/")
def home():
    #todo: add categories to db - top5, all. watched (user login)
    values = Currency.query.all()


    #add_nbp()
    # for val in values:
    #     print(val.values[len(val.values)-1].value)
        # for item in val.values:
        #     print(item.symbol)
        #     print(item.value)

    # for val in values:
    #     new_currency = Currency(
    #         country=val['country_name'],
    #         name=val['value_name'],
    #         qty=int(val['qty']),
    #         symbol=val['symbol'],
    #         flag_img=val['flag_img'],
    #     )
    #     db.session.add(new_currency)
    #     db.session.commit()
    # food.to_dict() jsonify(food="New db works")
    return render_template('index.html', currency=values)


if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, request
import dao
from saleapps2.saleapp import app


@app.route("/")
def index():
    categories = dao.load_categories()
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q, cate_id)
    return render_template("index.html", categories=categories, products=products)

@app.route("/products/<int:id>")
def product_details(id):
    product=dao.load_product_by_id((id))
    categories = dao.load_categories()
    return render_template('product-details.html',product=product,categories=categories)

@app.route("/login", methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__("POST"):
        print(request.form)
    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

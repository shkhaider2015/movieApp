from flask import Blueprint

main = Blueprint('main', __name__)
#kjkj
@main.route('/')
@main.route('/home')
def home():
    return "Hello Flask"
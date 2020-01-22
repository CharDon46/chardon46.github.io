from flask import Blueprint, render_template
from flask_images import resized_img_src

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('agency.html')
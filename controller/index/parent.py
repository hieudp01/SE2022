from flask import render_template

from controller.authentication.middleware import parent_required
from controller.main import parent_route


@parent_route.get('/')
@parent_required
def parent_main():
    return render_template('index/parent.html')

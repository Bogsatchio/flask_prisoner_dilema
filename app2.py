import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5  # pip install bootstrap-flask
import subprocess
import logging

from forms.experiments_form import ExperimentsForm, MyForm

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

os.environ['MYSQL_USER'] = 'dev'
os.environ['MYSQL_PASS'] = 'epigoldtop'


# class MyForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     submit = SubmitField('Submit')


def create_app(db_url=None):
    app = Flask(__name__)

    # data for documentation
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Real Estate API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "mysql://homestead:secret@mysql/homestead")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.logger.setLevel(logging.DEBUG)
    #db.init_app(app)

    app.secret_key = "any-string-you-want-just-keep-it-secret"
    bootstrap = Bootstrap5(app)

    @app.route("/", methods=['GET', 'POST'])
    def home():
        form = MyForm()
        if form.validate_on_submit():
            name = form.name.data

            return redirect(url_for("another_test", name=name))
            #return redirect(f"/test/{name}")

        return render_template('index2.html', form=form)

    @app.route("/test/<arg>", methods=['GET', 'POST'])
    def test(arg):
        return render_template('base.html')

    @app.route("/another_test/", methods=['GET', 'POST'])
    def another_test():
        n = request.args.get("name", "IM SORRY")
        app.logger.debug(n)
        return render_template('base.html')

    return app


if __name__=='__main__':
    app_run = create_app()
    app_run.run(debug=True)

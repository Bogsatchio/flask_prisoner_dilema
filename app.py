import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5  # pip install bootstrap-flask
import subprocess
import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from forms.experiments_form import ExperimentsForm
from utils.db_utils import get_connection, get_population_plots
from utils.sqls import get_population_evolution_query

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

os.environ['MYSQL_USER'] = 'homestead'
os.environ['MYSQL_PASS'] = 'secret'


def create_app(db_url=None):
    app = Flask(__name__)

    # data for documentation
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Prisoner Dilema API"
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
        form = ExperimentsForm()
        if form.validate_on_submit():
            jar_params = [form.name.data, form.description.data, form.cooperation_points.data,
                          form.one_side_betrayal_points.data, form.two_side_betrayal_points.data, form.rounds.data,
                          form.matches.data, form.waves.data, form.num_eliminated.data, form.winners_premium.data,
                          form.rando_n.data, form.defector_n.data, form.rather_defector_n.data, form.grim_trigger_n.data,
                          form.tft_n.data, form.forgiving_tft_n.data, form.cooperator_n.data,
                          form.much_rather_defector_n.data, form.pavlov_n.data, form.sus_tft_n.data]

            return redirect(url_for("run_jar", **{f"p{i}": param for i, param in enumerate(jar_params)}))
            #return redirect(f"/test/{name}")

        return render_template('index.html', form=form)

    @app.route("/run_jar", methods=['GET', 'POST'])
    def run_jar():
        jar_params = [request.args.get(f"p{i}") for i in range(20)]
        app.logger.debug(f'jar_params: {jar_params}')
        if len(jar_params) == 20:
            try:
                jar_path = 'jars/PrisonerDilemaSimulation_docker.jar'
                result = subprocess.run(['java', '-jar', jar_path] + jar_params, capture_output=True, text=True)

                #return render_template("waiting.html", experimentId=jar_params[0])
                return redirect(f"/results/{jar_params[0]}")
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return "Bad params", 400

    @app.route("/results/<experiment_id>", methods=["GET", "POST"])
    def results(experiment_id):
        Session = get_connection()
        with Session() as session:
            result = session.execute(get_population_evolution_query(experiment_id))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            get_population_plots(df, experiment_id)

        return render_template("results.html", experimentId=experiment_id)




    @app.route("/test/<arg>", methods=['GET', 'POST'])
    def test(arg):
        return render_template('base.html')

    @app.route("/another_test/", methods=['GET', 'POST'])
    def another_test():
        jar_params = [request.args.get(f"p{i}") for i in range(10)]
        app.logger.debug(jar_params)
        return render_template('base.html')

    return app


if __name__ == '__main__':
    app_run = create_app()
    app_run.run(debug=True)

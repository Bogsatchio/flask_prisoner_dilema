import unittest
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from forms.experiments_form import ExperimentsForm  # Replace with the actual name of your Flask app file

class TestExperimentsForm(unittest.TestCase):
    valid_form_data = {
        "name": "Test Experiment",
        "description": "This is a test",
        "cooperation_points": 10,
        "one_side_betrayal_points": 5,
        "two_side_betrayal_points": 0,
        "rounds": 10,
        "matches": 5,
        "waves": 2,
        "num_eliminated": 1,
        "winners_premium": 1.5,
        "rando_n": 1,
        "forgiving_tft_n": 1,
        "defector_n": 1,
        "cooperator_n": 1,
        "rather_defector_n": 1,
        "much_rather_defector_n": 1,
        "grim_trigger_n": 1,
        "pavlov_n": 1,
        "tft_n": 1,
        "sus_tft_n": 1
    }

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.app.config['SECRET_KEY'] = 'supersecretkey'
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_form_with_valid_data(self):
        form = ExperimentsForm(data=self.valid_form_data)
        self.assertTrue(form.validate())

    def test_form_with_invalid_data(self):
        invalid_form_data = self.valid_form_data
        invalid_form_data["one_side_betrayal_points"] = 5000
        form = ExperimentsForm(data=invalid_form_data)
        self.assertFalse(form.validate())

    def test_form_with_missing_data(self):
        form_data = {
            "description": "This is a test",
        }
        form = ExperimentsForm(data=form_data)
        self.assertFalse(form.validate())
        self.assertIn('name', form.errors)  # Check if 'name' is in the error messages

if __name__ == "__main__":
    unittest.main()

from unittest import TestCase
from app import create_app
from forms.experiments_form import ExperimentsForm


class TestHomeRoute(TestCase):
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
        self.app = create_app()
        self.app.config.update({
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,  # Disable CSRF for testing purposes
        })
        self.client = self.app.test_client()

    def test_home_get(self):
        # Test GET request to home route
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Experiment's rules", response.data)

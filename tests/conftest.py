import pytest

from app import create_app
from forms.experiments_form import ExperimentsForm
from utils.db_utils import get_connection


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    app.config['SECRET_KEY'] = 'supersecretkey'

    # Create a context for the app
    with app.app_context():
        yield app  # This will return the app instance to the tests


@pytest.fixture
def client(app):
    """Fixture for the test client."""
    return app.test_client()


@pytest.fixture
def valid_form_data():
    return {
        "name": "Test_Experiment",
        "description": "test",
        "cooperation_points": 10,
        "one_side_betrayal_points": 5,
        "two_side_betrayal_points": 1,
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


@pytest.fixture
def form_with_valid_data(valid_form_data):
    return ExperimentsForm(data=valid_form_data)


@pytest.fixture()
def expected_params(valid_form_data):
    return {f'p{i}': str(value) for i, value in enumerate([
        valid_form_data['name'],
        valid_form_data['description'],
        valid_form_data['cooperation_points'],
        valid_form_data['one_side_betrayal_points'],
        valid_form_data['two_side_betrayal_points'],
        valid_form_data['rounds'],
        valid_form_data['matches'],
        valid_form_data['waves'],
        valid_form_data['num_eliminated'],
        valid_form_data['winners_premium'],
        valid_form_data['rando_n'],
        valid_form_data['defector_n'],
        valid_form_data['rather_defector_n'],
        valid_form_data['grim_trigger_n'],
        valid_form_data['tft_n'],
        valid_form_data['forgiving_tft_n'],
        valid_form_data['cooperator_n'],
        valid_form_data['much_rather_defector_n'],
        valid_form_data['pavlov_n'],
        valid_form_data['sus_tft_n']
    ])}


@pytest.fixture()
def db_name():
    return "test_db"

@pytest.fixture()
def session(db_name):
    # Create a session using the connection
    Session = get_connection(db_name)
    session = Session()
    yield session  # This will be the session used in the tests

    session.close()  # Close the session after tests are done

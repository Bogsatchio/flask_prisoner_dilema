import pytest
from forms.experiments_form import ExperimentsForm
from urllib.parse import parse_qs


def test_basic_home_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Experiment's rules" in response.data


def test_form_with_valid_data(client, form_with_valid_data):
    assert form_with_valid_data.validate(), f"Form validation failed with errors: {form_with_valid_data.errors}"


def test_form_with_invalid_data(client, valid_form_data):
    invalid_form_data = valid_form_data.copy()
    invalid_form_data["one_side_betrayal_points"] = 5000
    form = ExperimentsForm(data=invalid_form_data)
    assert not form.validate()


def test_form_with_missing_data(client):
    form_data = {
        "description": "This is a test",
    }
    form = ExperimentsForm(data=form_data)
    assert not form.validate()
    assert "name" in form.errors, "Expected 'name' in form.errors but it wasn't found."
    assert "rounds" in form.errors, "Expected 'rounds' in form.errors but it wasn't found."
    assert "matches" in form.errors, "Expected 'matches' in form.errors but it wasn't found."


def test_home_route_redirects_to_run_jar(client, valid_form_data, expected_params):
    """
    checks for:
        - redirection status code
        - proper redirection address
        - proper parameters passed from form data

    """

    response = client.post("/", data=valid_form_data)
    assert response.status_code == 302
    assert response.headers['Location'].startswith('/run_jar')

    # Get the params passed from data
    query_string = response.headers['Location'].split('?', 1)[1]
    params = parse_qs(query_string)
    for key, value in expected_params.items():
        assert key in params
        assert params[key][0] == value


def test_home_route_bad_parsing(client, valid_form_data, expected_params):
    """
    checks for:
        - valid parameters parsing when given changed data
    """
    invalid_form_data = valid_form_data
    invalid_form_data["name"] = "bad_name"
    response = client.post("/", data=invalid_form_data)

    query_string = response.headers['Location'].split('?', 1)[1]
    params = parse_qs(query_string)
    print(expected_params)
    for key, value in expected_params.items():
        assert key in params
        if key == "p0":
            print("checked one side")
            assert params[key][0] != value

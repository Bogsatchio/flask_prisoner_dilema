


def test_get_connection_simple_query(session):
    result = session.execute("SELECT 1").scalar()
    assert result == 1


from data_pipeline.queries import create_queries

def test_create_queries():
    tables = ["customers", "orders"]

    expected = {
        "customers": "SELECT * FROM customers",
        "orders": "SELECT * FROM orders"
    }

    result = create_queries(tables)

    assert result == expected





    from data_pipeline.queries import create_queries

def test_create_queries():
    tables = ["customers", "orders"]

    expected = {
        "customers": "SELECT * FROM customers",
        "orders": "SELECT * FROM orders"
    }

    result = create_queries(tables)

    assert result == expected

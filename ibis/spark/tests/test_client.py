import pytest

import ibis

pytestmark = pytest.mark.spark


def test_list_databases(client):
    dbs = client.list_databases()
    assert dbs == ['default']


def test_list_tables(client):
    tables = client.list_tables()
    assert tables == [
        'awards_players',
        'batting',
        'complicated',
        'functional_alltypes',
        'nested_types',
        'simple',
        'struct',
        'udf',
        'udf_nan',
        'udf_null',
        'udf_random',
    ]


def test_get_schema(client):
    schema = client.get_schema('simple')
    assert schema.equals(
        ibis.schema(
            [
                ('foo', 'int64'),
                ('bar', 'string')
            ]
        )
    )


def test_table_simple(client):
    db = client.database()
    # also tests that client.table and db.table give the same result
    for t in [client.table('simple'), db.table('simple')]:
        assert t.columns == ['foo', 'bar']
        result = t.execute()
        assert len(result) == 1
        assert list(result.iloc[0]) == [1, 'a']


def test_struct_type(struct):
    schema = struct.schema()
    assert schema.equals(
        ibis.schema(
            [('struct_col', 'struct<_1: int64, _2: int64, _3: string>')]
        )
    )


def test_table_nested_types(nested_types):
    schema = nested_types.schema()
    assert schema.equals(
        ibis.schema(
            [
                ('list_of_ints', 'array<int64>'),
                ('list_of_list_of_ints', 'array<array<int64>>'),
                (
                    'map_string_list_of_list_of_ints',
                    'map<string, array<array<int64>>>'
                )
            ]
        )
    )


@pytest.mark.xfail
def test_table_complicated(complicated):
    schema = complicated.schema()
    assert schema.equals(
        ibis.schema(
            [
                (
                    'map_tuple_list_of_list_of_ints',
                    'map<struct<_1: int64, _2: int64>, array<array<int64>>>'
                )
            ]
        )
    )


def test_current_database(client):
    assert client.current_database == 'default'

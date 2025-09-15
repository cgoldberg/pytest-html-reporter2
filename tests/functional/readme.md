# pytest bank
> pytest exercises

### Feature

- [x] Basic
- [x] Fixture #mock-data
- [x] UseFixture #background-teardown
- [x] Autouse
- [x] Mark #Tags
- [x] Parameterize #data-driven
- [x] Yield #hooks
- [x] Skip tests

### Pytest Runner

| Type                  | Command               |
| --------------        | ---------             |
| generic run           | `pytest -v -s tests/functional/test_yield_fixture.py` |
| run specific test case| `pytest -v -s tests/functional/test_yield_fixture.py::test_fail` |
| run tagged tests      | `pytest -v -s tests/functional/test_mark.py -m 'slow'` |

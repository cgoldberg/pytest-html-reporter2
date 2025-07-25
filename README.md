# pytest-html-reporter2

### [pytest][pytest-home] [plugin][pytest-plugins] to generate static HTML reports

---

- Development: [GitHub][github-repo]
- Download/Install: [PyPI][pypi-page]
- License: [MIT][mit-license]

_This is a fork of [pytest-html-reporter][pypi-parent-page] (by [Prashanth Sams][github-parent-repo])
with some bug fixes, improvements, and updates to work with newer versions of pytest._

![logo](https://i.imgur.com/4TYia5j.png)

----

## Features:

- Generic information
  - Overview
  - Trends
  - Suite highlights
  - Test suite details
- Archives / History
- Screenshots
- Test re-run support

## Installation:

latest release:

```
pip install pytest-html-reporter2
```

current development version:

```
pip install git+https://github.com/cgoldberg/pytest-html-reporter2.git@update
```

## Usage:

Once you have this plugin installed, you just run your tests with pytest (`pytest` or `python -m pytest`)
as you would normally. It will save a report named `pytest_html_report.html` in the currect directory.

The following pytest arguments can be used:

- `--html-report`: path where report and archives are generated (can be a directory or file name)
  - `pytest --html-report=./report`
  - `pytest --html-report=./report/report.html`
- `--title`: customize report title
  -  `pytest --title="Test Reprt"`
- `--archive-count`: maximum build count to display in the archives section
  - `pytest --archive-count=10`

## Example:

![example](https://i.imgur.com/1HSYkdC.gif)

## Demo:

If you want to try it out, there are several example tests in the GitHub repo. This will clone the repo,
create a virtual environment, install the plugin from source, and run the example tests:

```
git clone https://github.com/cgoldberg/pytest-html-reporter2.git
cd pytest-html-reporter2
python3 -m venv venv
source venv/bin/activate
pip install .
pytest tests/functional
```

When it completes, you can view `pytest_html_report.html`  in your browser.

[github-repo]: https://github.com/cgoldberg/pytest-html-reporter2
[pypi-page]: https://pypi.org/project/pytest-html-reporter2
[github-parent-repo]: https://github.com/prashanth-sams/pytest-html-reporter
[pypi-parent-page]: https://pypi.org/project/pytest-html-reporter
[mit-license]: https://raw.githubusercontent.com/cgoldberg/pytest-html-reporter2/refs/heads/master/LICENSE
[pytest-home]: https://pytest.org
[pytest-plugins]: https://docs.pytest.org/en/stable/how-to/plugins.html

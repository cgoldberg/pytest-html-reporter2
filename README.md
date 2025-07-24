# pytest-html-reporter2


### pytest plugin to generate static HTML reports


![logo](logo.jpg)


Features
------------
* Generic information
  - Overview
  - Trends
  - Suite Highlights
  - Test suite details
* Archives / History
* Screenshots on failure
* Test Rerun support

Installation
------------

.. code-block:: console

    $ pip install pytest-html-reporter2


Usage
------------

By default, the filename used is ``pytest_html_report.html`` and path chosen is ``report``; you can skip both or
either one of them if not needed::

    $ pytest tests/


..

        Custom path, filename, and title

Add ``--html-report`` tag followed by path location and filename to customize the report location and filename::

    $ pytest tests/ --html-report=./report
    $ pytest tests/ --html-report=./report/report.html

Add ``--title`` tag followed by the report title::

    $ pytest tests/ --html-report=./report --title='PYTEST REPORT'

Add ``--archive-count`` tag followed by an integer to limit showing the number of builds in the ``Archives`` section::

    $ pytest tests/ --archive-count 7
    $ pytest tests/ --html-report=./report --archive-count 7

..

        pytest.ini

Alternate option is to add this snippet in the ``pytest.ini`` file::

    [pytest]
    addopts = -vs -rf --html-report=./report --title='PYTEST REPORT'

**Note:** If you fail to provide ``--html-report`` tag, it consider your project's home directory as the base

screenshots on failure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import ``attach`` from the library and call it with the selenium command as given below::

    from pytest_html_reporter2 import attach

    ...
    attach(data=self.driver.get_screenshot_as_png())

.. image:: https://img.shields.io/badge/Attach_screenshot_snippet-000?style=for-the-badge&logo=ko-fi&logoColor=white
   :target: https://gist.github.com/prashanth-sams/f0cc2102fc3619b11748e0cbda22598b


.. image:: https://i.imgur.com/1HSYkdC.gif


Is there a demo available for this gem?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, you can use this demo as an example, https://github.com/prashanth-sams/pytest-html-reporter::

    $ pytest tests/functional/

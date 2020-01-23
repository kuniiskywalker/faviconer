================
faviconer
================

.. image:: https://circleci.com/gh/kuniiskywalker/faviconer.svg?style=svg
    :target: https://circleci.com/gh/kuniiskywalker/faviconer

What is this?
================

This is a package to get a nice favicon from a website

Installation
================

.. code-block:: bash

    pip install faviconer

Usage
================

Get favicon.ico:

Get /favicon.ico if there is no explicit favicon url specified in the meta tag of the target site

When the favicon url is specified in the meta tag

.. code-block:: python

    >>> import faviconer
    >>> faviconer.get_by_url("https://example.com/test/?aaa=1")
    'https://example.com/image/icon.png'

When there is no specific URL specified in the meta tag

.. code-block:: python

    >>> import faviconer
    >>> faviconer.get_by_url("https://example.com/test/?aaa=1")
    'https://example.com/favicon.ico'

Get favicon.ico by url:

.. code-block:: python

    >>> import faviconer
    >>> faviconer.get_by_url("https://example.com/")
    'https://example.com/favicon.ico'

Get favicon.ico by html:

Analyze the target site html and get favicon.ico if favicon url is specified in meta tag

.. code-block:: python

    >>> import faviconer
    >>> faviconer.get_by_html('<html><head><link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico"></head><body></body</html>')
    'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico'
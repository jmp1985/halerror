.. halerror documentation master file, created by
   sphinx-quickstart on Sun Apr 14 15:05:13 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

halerror
========

This python library implements a sci-fi exception class!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   API documentation <modules>

Installation
------------

The package is available from `PyPI <https://pypi.org/project/halerror/0.4.0/>`_. To install using pip, do the following:

.. code-block:: bash

    pip install halerror

To install from source, clone the `GitHub <https://github.com/jmp1985/halerror/>`_ repository and then do the following:

.. code-block:: bash

    python setup.py install

Testing
-------

To run the tests, download the source code and do the following:

.. code-block:: bash

    python setup.py test

Building the documentation
--------------------------

To build this documenation, download the source code and the do the following:

.. code-block:: bash
    
    pip install -e .[build_sphinx]
    python setup.py build_sphinx

Usage examples
--------------

The exception class can be used as follows:

.. code-block:: python

    from halerror import HalError

    def open_pod_bay_doors():
        raise HalError("Open the pod bay doors, HAL.")

    open_pod_bay_doors()

This will result in the following error output, where ${NAME} is the username
of the person running the software:

.. code-block:: text

    halerror.HalError: Open the pod bay doors, HAL
    
    I'm sorry, ${NAME}. I'm afraid I can't do that.

Having all your exceptions formatted like this is as easy as adding the
following lines to your code

.. code-block:: python

    from halerror import HalError

    try:
        open_pod_bay_doors()
    except Exception as error:
        raise HalError(error) from error

API documentation
-----------------

Please check out the API documentation :doc:`here <modules/>`.

Issues
------

Please use the `GitHub issue tracker
<https://github.com/jmp1985/halerror/issues/>`_ to submit bugs or request
features.

License
-------

Copyright James Parkhurst, 2019.

.. literalinclude:: ../LICENSE
   :language: text
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

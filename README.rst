Protobuf-tools Project
=================


Purpose
-------
* To ease editing and reading protocol buffer files
* It provides easy interface to encode/decode proto files

Installation
------------

This package can be pip installed

    pip install protobuf_tools

.. note::

    Built and tested with python 2.7 and proto 2


Usage
-----

* For templating

    run_c_builder -i <input_c_file.c>

* For just writing to a c file

.. highlight:: python

    from c_builder import c_writer


* Then just use the file classes provided and check the documentation in the classes
* You can also check the generated template for pointers to usage
* Or check out the sample installed along with the library

For Bugs
--------

Join the slack workspace at -
https://join.slack.com/t/projectaja/shared_invite/enQtMjk1NTk0NzIwNDIzLWRmMTNjMzY3ZGFmYjY4MGZhOTBiNjZjZTA1YzM3MmFmYWIxOTJkY2QyOWNjM2JhZTk3NTMzMzNmZGIyZGM3NmY

And join the c_builder channel

Also you can email me at

pip[at]abhijit.bansal.com


Future
------

1. Add support for more C code
2. Support for doing standards check on the datatypes
3. More intelligent analysis
4. Support for C++
5. C++ style template classes for C


Version History
---------------

0.0.6 : Fix for package installation

0.0.2 : More support and documentation

0.0.1 : Initial version, tested upload to pypi





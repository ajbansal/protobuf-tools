Protobuf-tools Project
======================


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

Python
######

you can import it in your library as

    from protobuf_tools import proto_utils


protobuftools
#############

To use to read/decode any proto files please use the script utility protobuftools
If you do not provide the --proto_path it defaults to the working directory

##### For help use

    protobuftools -h

##### To use json for decode or encode use -json flag

##### For enabling all fields to be part of decode use --allfields


##### For decoding a protobuf file to more human readable form

    protobuftools "<path_to_proto_stream_file>" --proto_path "<optional - provide path to where _pb2 files are>" --decode=message_name --allfields -json

#### To display instead of writing to file

    protobuftools "<path_to_proto_stream_file>" --proto_path "<optional - provide path to where _pb2 files are>" --decode=message_name --allfields -json -d

##### For encoding - To convert from json/text to protobuf file, output is a file with .protoout extension

    protobuftools "<path_to_file(.json/.txt etc) from above" --proto_path "<optional - provide path to where _pb2 files are>" --encode=message_name -json



For Bugs
--------

Join the slack workspace at -
https://join.slack.com/t/projectaja/shared_invite/enQtMjk1NTk0NzIwNDIzLWRmMTNjMzY3ZGFmYjY4MGZhOTBiNjZjZTA1YzM3MmFmYWIxOTJkY2QyOWNjM2JhZTk3NTMzMzNmZGIyZGM3NmY

And join the protobuf_tools channel

Also you can email me at

pip[at]abhijit.bansal.com


Future
------

1. Add UI tools for viewing and editing
2. Support for python 3 and proto 3

Version History
---------------

0.0.3 : Changed version of protobuf to 3.2.0 should work for any other version too

0.0.2 : Changed setup version for protobuf

0.0.1 : Initial version, tested upload to pypi





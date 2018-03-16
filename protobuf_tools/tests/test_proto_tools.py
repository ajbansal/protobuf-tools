from unittest import TestCase

import os
import sys
import filecmp
import logging

from pathlib2 import Path

from protobuf_tools import proto_utils
import message_pb2


class TestProtoBufTools(TestCase):
    def __init__(self, values):
        super(TestProtoBufTools, self).__init__(values)
        self.this_file_dir = os.path.dirname(__file__)
        self.person = message_pb2.Person
        self.person = message_pb2.Person()
        self.person.id = 1234
        self.person.name = "John Doe"
        self.person.email = "jdoe@example.com"
        phone = self.person.phones.add()
        phone.number = "555-4321"
        phone.type = message_pb2.Person.HOME
        self.file = os.path.join(self.this_file_dir, "message.stream")
        with open(self.file, 'wb') as f:
            f.write(self.person.SerializeToString())

    def test_decode(self):
        """To test if it decodes the file correctly"""

        proto_message = proto_utils.proto_from_stream(self.file, message_pb2.Person)
        if proto_message == self.person:
            self.assertTrue(True, "Test passed for decodes_file_and_runs")
        else:
            self.assertFalse(False, "Failed to Decode")

    def test_encode(self):
        """To test if it encodes the file correctly"""

        proto_message = proto_utils.proto_from_stream(self.file, message_pb2.Person)
        file_path = Path(self.file).with_suffix(".protoout")
        proto_utils.proto_to_stream(proto_message, str(file_path))

        if filecmp.cmp(self.file, str(file_path)):
            self.assertTrue(True, "Test passed for encodes_file_and_runs")
        else:
            self.assertFalse(False, "Failed to encode")
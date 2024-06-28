import unittest
import aiostun

class TestEncode(unittest.TestCase):
    def test_encode_attribute_addr(self):
        IP = "1.1.1.1"
        PORT = 12345
        attribute_addr = aiostun.attribute.AttrMappedAddr()
        attribute_addr.params = {"family": aiostun.constants.FAMILY_NAMES[aiostun.constants.FAMILY_IP4], "ip": IP, "port": PORT}

        attr_value = attribute_addr.encode()
        decoded_attribute_addr = aiostun.attribute.AttrMappedAddr()
        decoded_attribute_addr.decode(attr_value)

        self.assertEqual(attribute_addr.params, decoded_attribute_addr.params)



IPPROTO_UDP = 1
IPPROTO_TCP = 2
IPPROTO_TLS = 3

IPPROTO_NAMES = {
    IPPROTO_UDP: "UDP",
    IPPROTO_TCP: "TCP",
    IPPROTO_TLS: "TLS",
}

FAMILY_IP4 = 0x01
FAMILY_IP6 = 0x02

FAMILY_NAMES = {
        FAMILY_IP4: "IPv4",
        FAMILY_IP6: "IPv6"
}

MAGIC_COOKIE = 0x2112A442
STUN_HEADER_SIZE = 20

CLASS_REQUEST = 0
CLASS_INDICATION = 1
CLASS_SUCCESS = 2
CLASS_ERROR = 3

CLASS_NAMES = {
    CLASS_REQUEST: "Request",
    CLASS_INDICATION: "Indication",
    CLASS_SUCCESS: "Success Response",
    CLASS_ERROR: "Error Response",
}

METHOD_BINDING = 1
METHOD_SHARED_SECRET = 2
METHOD_ALLOCATE = 3
METHOD_REFRESH = 4
METHOD_SEND = 6
METHOD_DATA = 7
METHOD_CREATE_PERMISSION = 8
METHOD_CHANNEL_BIND = 9

METHOD_NAMES = {
    METHOD_BINDING: "Binding",
    METHOD_SHARED_SECRET: "SharedSecret",
    METHOD_ALLOCATE: "Allocate",
    METHOD_REFRESH: "Refresh",
}

ATTR_MAPPED_ADDRESS = 0x001
ATTR_RESPONSE_ADDRESS = 0x002
ATTR_CHANGE_REQUEST = 0x003
ATTR_SOURCE_ADDRESS = 0x004 # deprecated
ATTR_CHANGED_ADDRESS = 0x005 # deprecated
ATTR_USERNAME = 0x006
ATTR_PASSWORD = 0x007
ATTR_MESSAGE_INTEGRITY = 0x008
ATTR_ERROR_CODE = 0x009
ATTR_UNKNOWN_ATTRIBUTE = 0x00a
ATTR_REFLECTED_FROM = 0x00b
ATTR_CHANNEL_NUMBER = 0x00c
ATTR_LIFETIME = 0x00d
ATTR_BANDWIDTH = 0x0010
ATTR_XOR_PEER_ADDRESS = 0x0012
ATTR_DATA = 0x0013
ATTR_REALM = 0x0014
ATTR_NONCE = 0x0015
ATTR_XOR_RELAYED_ADDRESS = 0x0016
ATTR_REQUESTED_ADDRESS_FAMILY = 0x0017
ATTR_EVENT_PORT = 0x0018
ATTR_REQUESTED_TRANSPORT = 0x0019
ATTR_DONT_FRAGMENT = 0x001A
ATTR_MESSAGE_INTEGRITY_SHA256  = 0x001C
ATTR_PASSWORD_ALGORITHM = 0x001D
ATTR_USERHASH = 0x001E
ATTR_XOR_MAPPED_ADDRESS = 0x0020
ATTR_RESERVATION_TOKEN = 0x0022
ATTR_PADDING = 0x0026
ATTR_RESPONSE_PORT = 0x0027
ATTR_PASSWORD_ALGORITHMS = 0x8002
ATTR_ALTERNATE_DOMAIN = 0x8003
ATTR_XOR_MAPPED_ADDRESS_OPTIONAL = 0x8020 # optional for the client to use
ATTR_SOFTWARE = 0x8022
ATTR_ALTERNATE_SERVER = 0x8023
ATTR_PRIORITY = 0x0024
ATTR_USE_CANDIDATE = 0x0025
ATTR_CACHE_TIMEOUT = 0x8027
ATTR_FINGERPRINT = 0x8028
ATTR_ICE_CONTROLLED = 0x8029
ATTR_ICE_CONTROLLING = 0x802A
ATTR_RESPONSE_ORIGIN = 0x802B
ATTR_OTHER_ADDRESS = 0x802C

ATTR_NAMES = {
    ATTR_MAPPED_ADDRESS: "MAPPED-ADDRESS",
    ATTR_USERNAME: "USERNAME",
    ATTR_MESSAGE_INTEGRITY: "MESSAGE-INTEGRITY",
    ATTR_ERROR_CODE: "ERROR-CODE",
    ATTR_UNKNOWN_ATTRIBUTE: "UNKNOWN-ATTRIBUTES",
    ATTR_REALM: "REALM",
    ATTR_NONCE: "NONCE",
    ATTR_REQUESTED_ADDRESS_FAMILY: "REQUESTED-ADDRESS-FAMILY",
    ATTR_XOR_MAPPED_ADDRESS: "XOR-MAPPED-ADDRESS",
    ATTR_XOR_MAPPED_ADDRESS_OPTIONAL: "XOR-MAPPED-ADDRESS",
    ATTR_SOFTWARE: "SOFTWARE",
    ATTR_ALTERNATE_SERVER: "ALTERNATE-SERVER",
    ATTR_FINGERPRINT: "FINGERPRINT",
    ATTR_RESPONSE_ORIGIN: "RESPONSE-ORIGIN",
    ATTR_OTHER_ADDRESS: "OTHER-ADDRESS",
    ATTR_SOURCE_ADDRESS: "SOURCE-ADDRESS",
    ATTR_CHANGED_ADDRESS: "CHANGED-ADDRESS"
}

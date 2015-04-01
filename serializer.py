import json

def encode_msg(msg_type, msg_details):

    ''' encode_msg() encodes messages of various types 
        in JSON format in order for them to be serialized
        and sent via a TCP/IP connection.
        This function handles messages of all types.

        Inputs:
            - msg_details: is supposed to be a dict() containing
              all of the message's data, like item id and price 
              in the case of bid msg.

            - msg_type: a simple string containing the message type
              to be prepended via a 'header' field to the rest of
              the message
    '''

    # create a shallow copy of msg_details
    data = dict(msg_details)

    # fill header field
    data['header'] = msg_type

    # '|' is the message delimiter
    return (json.dumps(data) + '|')


def unpack_msg(msg_in_bytes):

    ''' unpack_msg unpacks a byte-encoded message received
        over a socket using the UTF-8 encoding.
    '''
    return msg_in_bytes.decode('UTF-8')

def decode_msg(msg_in_json):

    ''' decode_msg(msg_in_json) accepts a message in JSON
        that has been serialized. 
    '''
    data = json.loads(msg_in_json)

    return data

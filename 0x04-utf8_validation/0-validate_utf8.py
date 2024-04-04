#!/usr/bin/python3
"""UTF-8 Validation Practice"""


def validUTF8(data):
    """UTF-8 Validation Practice"""
    if data is None:
        return False
    bs = []
    for num in data:
        if type(num) is not int:
            return False
        bs.append(format(num, '08b'))

    bytesN = None
    for b in bs:
        if bytesN is None:
            pass
        elif bytesN == 0:
            bytesN = None
        elif bytesN > 0:
            if b[0] == '1' and b[1] == '0':
                bytesN -= 1
                continue
            else:
                return False
        else:
            return False

        if b[0] == '0':
            continue
        elif b[0] == '1':
            if b[1] == '1' and b[2] == '1' and b[3] == '1' and b[4] == '0':
                bytesN = 3
            elif b[1] == '1' and b[2] == '1' and b[3] == '0':
                bytesN = 2
            elif b[1] == '1' and b[2] == '0':
                bytesN = 1
            else:
                return False
        else:
            return False

    return True

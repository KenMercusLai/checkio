# -*- coding: utf-8 -*-
import hashlib


def checkio(hashed_string, algorithm):
    return hashlib.__getattribute__(algorithm)(str(hashed_string.encode('utf-8'))).hexdigest()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(u'welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio(u'happy spam',
                   'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'

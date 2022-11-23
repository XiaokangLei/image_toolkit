'''
Descripttion: MD5/SHA1/SHA256
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-23 11:05:13
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-23 11:11:14
'''

import hashlib
import rich.progress


def encrypt(fpath: str, algorithm: str) -> str:
    """encrypt, file size: < 500MB

    Args:
        fpath (str): file path
        algorithm (str): MD5/SHA1/SHA256

    Returns:
        str: hexdigest
    """
    with open(fpath, 'rb') as f:
        return hashlib.new(algorithm, f.read()).hexdigest()


def encrypt_big(fpath: str, algorithm: str) -> str:
    """encrypt, file size: 500MB~1GB

    Args:
        fpath (str): file path
        algorithm (str): MD5/SHA1/SHA256

    Returns:
        str: hexdigest
    """
    with rich.progress.open(fpath, 'rb') as f:
        return hashlib.new(algorithm, f.read()).hexdigest()


def encrypt_super(fpath: str, algorithm: str) -> str:
    """encrypt, file size: >1GB

    Args:
        fpath (str): file path
        algorithm (str): MD5/SHA1/SHA256

    Returns:
        str: hexdigest
    """
    with rich.progress.open(fpath, 'rb') as f:
        hash = hashlib.new(algorithm)
        for chunk in iter(lambda: f.read(2**20), b''):
            hash.update(chunk)
        return hash.hexdigest()


if __name__ == '__main__':
    for algorithm in ('md5', 'sha1', 'sha256'):
        hexdigest = encrypt('test.file', algorithm)
        print(f'{algorithm}: {hexdigest}')

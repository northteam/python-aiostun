#!/usr/bin/env python3

from distutils.core import setup

setup(name="aiostun",
    version="0.4.2",
    description="Asynchronous STUN client for Python with UDP, TCP and TLS support",
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    url="https://github.com/northteam/python-aiostun/tree/develop",
    packages=["aiostun", "tests"],
)

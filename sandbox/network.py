#!/usr/bin/env python3
import requests
import socket


"""function to check local host is configured correctly"""
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost

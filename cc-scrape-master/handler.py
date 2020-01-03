from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from write_csv import scrape


def handler(event, context):
    scrape()


if __name__ == '__main__':
    handler(None, None)
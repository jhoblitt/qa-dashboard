"""Tests for the dashboard API"""
import os
import requests
import time

""" Assume username and password for testing """
TEST_USER = os.environ.get("USER")
TEST_PASSWD = os.environ.get("USER")

API_URL = "http://localhost:8000/dashboard/api"


def test_api_root():
    """Access to the api root"""
    r = requests.get(API_URL)
    assert r.status_code == requests.codes.ok


def test_auth():
    """Attempt to access a resource without authentication"""

    r = requests.get(API_URL)
    api = r.json()

    for endpoint in api:
        r = requests.get(api[endpoint])
        assert r.status_code == 401


def test_post_metric():

    metric = {
                "metric": "test1",
                "description": "Test metric insertion",
                "units": "test",
                "minimum": "8",
                "design": "5",
                "stretch": "3",
                "user": "5"
             }

    r = requests.get(API_URL)
    api = r.json()

    r = requests.post(api['metrics'], json=metric,
                      auth=(TEST_USER, TEST_PASSWD))
    assert r.status_code == 201

    r.close()


def test_post_job():

    r = requests.get(API_URL)
    api = r.json()

    packages = [
        {'name': 'afw',
         'git_url': 'https://github.com/lsst/afw.git',
         'git_commit': 'fc355a99abe3425003b0e5fbe1e13a39644b1e95',
         'git_branch': 'master',
         'build_version': 'b2000'}]
    measurements = [{"metric": "test1", "value": 3.0}]
    jobs = [
        {"ci_name": "ci_cfht",
         "ci_id": "1",
         "ci_url": "https://ci.lsst.codes/job/ci_cfht/1/",
         "measurements": measurements,
         "packages": packages,
         "status": 0},
        {"ci_name": "ci_cfht",
         "ci_id": "2",
         "ci_url": "https://ci.lsst.codes/job/ci_cfht/2/",
         "measurements": measurements,
         "packages": packages,
         "status": 0},
        {"ci_name": "ci_cfht",
         "ci_id": "3",
         "ci_url": "https://ci.lsst.codes/job/ci_cfht/3/",
         "measurements": measurements,
         "packages": packages,
         "status": 0}]

    for job in jobs:
        r = requests.post(api['jobs'], json=job, auth=(TEST_USER, TEST_PASSWD))
        time.sleep(5)

    assert r.status_code == 201

    r.close()

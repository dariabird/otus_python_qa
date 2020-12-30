import os
import paramiko
import pytest

HOST = "192.168.88.177"


@pytest.fixture()
def ssh_conn():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'), port=22)
    yield ssh

    if ssh is not None:
        # Needs to prevent gc error
        # https://github.com/paramiko/paramiko/issues/1078
        ssh.close()
        del ssh

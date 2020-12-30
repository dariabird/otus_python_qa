import requests
import requests.exceptions
import time

from conftest import HOST


def assert_container_restarted_successfully(ssh_conn, container):
    _, stdout, _ = ssh_conn.exec_command(f'/usr/local/bin/docker ps -q -f "name={container}"')
    serv_id = stdout.read().decode("utf-8").rstrip()
    ssh_conn.exec_command(f'/usr/local/bin/docker restart {serv_id}')
    cmd = f'/usr/local/bin/docker ps --filter "name={container}" --format "{{{{.State}}}}"'
    _, stdout, _ = ssh_conn.exec_command(cmd)
    container_status = stdout.read().decode("utf-8").rstrip()
    assert "running" in container_status


def test_restart_opencart_services(ssh_conn):
    opencart_services= [
        'opencart_mariadb_1',
        'opencart_phpmyadmin_1',
    ]
    for serv in opencart_services:
        assert_container_restarted_successfully(ssh_conn, serv)


def test_restart_opencart(ssh_conn):
    assert_container_restarted_successfully(ssh_conn, 'opencart_opencart_1')
    status_code = None
    for _ in range(50):
        try:
            resp = requests.get(f"http://{HOST}/")
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            time.sleep(0.5)
            continue
        status_code = resp.status_code
        if status_code == 200:
            break
    assert status_code == 200

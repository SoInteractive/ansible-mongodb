from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(host):
    assert host.system_info.type == 'linux'


def test_pip(host):
    present = [
        "pymongo",
    ]
    if present and host.system_info.distribution == "ubuntu":
        packages = host.pip_package.get_packages()
        for p in present:
            assert p in packages


# def test_services(host):
#     present = [
#         "mongodb_exporter"
#     ]
#     for service in present:
#         s = host.service(service)
#         assert s.is_enabled
#         assert s.is_running


def test_socket(host):
    present = [
        "tcp://127.0.0.1:27017"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening

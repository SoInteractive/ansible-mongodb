from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package, SystemInfo):
    present = [
        "python-pip",
    ]
    if present and SystemInfo.distribution == "ubuntu":
        for package in present:
            p = Package(package)
            assert p.is_installed


# def test_directories(File):
#     present = [
#         "/var/log/mongodb",
#         "/var/lib/mongodb",
#         "/opt/mongodb_exporter",
#         "/var/log/mongodb_exporter"
#     ]
#     if present:
#         for directory in present:
#             d = File(directory)
#             assert d.is_directory
#             assert d.exists
#
#
# def test_files(File):
#     present = [
#         "/etc/mongod.conf"
#     ]
#     if present:
#         for file in present:
#             f = File(file)
#             assert f.exists
#             assert f.is_file
#
#
# def test_packages(Package):
#     present = [
#         "mongodb-org-server"
#     ]
#     if present:
#         for package in present:
#             p = Package(package)
#             assert p.is_installed
#
#
# def test_service(Service):
#     present = [
#         "mongodb",
#         "mongodb_exporter"
#     ]
#     if present:
#         for service in present:
#             s = Service(service)
#             assert s.is_enabled
#
#
# def test_socket(Socket):
#     present = [
#         "tcp://127.0.0.1:27017",
#         "tcp://127.0.0.1:9001"
#     ]
#     for socket in present:
#         s = Socket(socket)
#         assert s.is_listening

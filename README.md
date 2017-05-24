Mongodb installation role
=========================

All variables are in defaults/main.yml

Mongodb exporter metrics
========================

If mongodb_metrics is true install mongodb_exporter using binary release. Handlers for restart/reload events.

Requirements
============
All needed packages will be installed with this role. 

Optional variables
------------------

Mongodb_exporter specific user-configurable defaults:
```
mongodb_exporter_uri: 'mongodb://localhost:27017'
```

Role Variables
==============
```
mongodb_metrics: true

mongodb_exporter_version: "1.0.0"

mongodb_exporter_url: "https://github.com/dcu/mongodb_exporter/releases/download/v{{ mongodb_exporter_version }}/mongodb_exporter-linux-amd64"
mongodb_exporter_release_name: "mongodb_exporter-linux-amd64"
mongodb_exporter_install_dir: "/opt/mongodb_exporter"

mongodb_exporter_root_dir: "/opt/mongodb_exporter"
mongodb_exporter_dist_dir: "{{ mongodb_exporter_root_dir }}/dist"
mongodb_exporter_bin_dir: "{{ mongodb_exporter_root_dir }}/current"

mongodb_exporter_pid_path: "/var/run/mongodb_exporter.pid"
mongodb_exporter_log_dir: "/var/log/mongodb_exporter"
mongodb_exporter_log_file: "{{ mongodb_exporter_log_dir }}/mongodb_exporter.log"

mongodb_exporter_user: prometheus
mongodb_exporter_group: prometheus
mongodb_exporter_service_name: mongodb_exporter
mongodb_exporter_web_listen_address: "0.0.0.0:9001"
   
# Mongodb URI, format: [mongodb://][user:pass@]host1[:port1][,host2[:port2],...][/database][?options] (default "mongodb://localhost:27017")
mongodb_exporter_uri: 'mongodb://localhost:27017'

mongodb_exporter_web_metrics-path: '/metrics'
mongodb_exporter_config_flags:
  'web.listen-address': '{{ mongodb_exporter_web_listen_address }}'
  'mongodb.uri': '{{ mongodb_uri }}'
  'web.metrics-path': '{{ mongobd_exporter_web_metrics-path }}'
  'log_dir': '{{ mongodb_exporter_log_dir }}' 
```

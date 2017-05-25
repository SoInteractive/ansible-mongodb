Mongodb installation role
=========================

All variables are in defaults/main.yml

Mongodb exporter metrics
========================

If mongodb_metrics is true install mongodb_exporter using binary release. Handlers for restart/reload events.

Requirements
============
All needed packages will be installed with this role. 

Role Variables
==============
```
mongodb_metrics: true

mongodb_exporter_version: "1.0.0"
mongodb_exporter_url: "https://github.com/dcu/mongodb_exporter/releases/download/v{{ mongodb_exporter_version }}/mongodb_exporter-linux-amd64"
mongodb_exporter_root_dir: "/opt/mongodb_exporter"
mongodb_exporter_dist_dir: "{{ mongodb_exporter_root_dir }}/dist"
mongodb_exporter_bin_dir: "{{ mongodb_exporter_root_dir }}/current"
mongodb_exporter_log_dir: "/var/log/mongodb_exporter"
mongodb_exporter_config_flags:
  'web.listen-address': '0.0.0.0:{{ mongodb_port }}'
  'mongodb.uri': 'mongodb://{{ mongodb_address }}:{{ mongodb_port }}'
  'log_dir': '{{ mongodb_exporter_log_dir }}' 
```

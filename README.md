<p><img src="https://webassets.mongodb.com/_com_assets/cms/MongoDB-Logo-5c3a7405a85675366beb3a5ec4c032348c390b3f142f5e6dddf1d78e2df5cb5c.png" alt="mongodb logo" title="mongodb" align="right" height="60" /></p>

Ansible Role: mongodb
===================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-mongodb.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-mongodb) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.mongodb-blue.svg)](https://galaxy.ansible.com/SoInteractive/mongodb/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-mongodb.svg)](https://github.com/SoInteractive/ansible-mongodb/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Provision one- or multi-node mongodb cluster

Mongodb exporter metrics
------------------------

If mongodb_metrics is true install mongodb_exporter using binary release. Handlers for restart/reload events.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.mongodb
```

Role Variables
--------------

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

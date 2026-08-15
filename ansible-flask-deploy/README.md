# Ansible + Docker Flask Deploy

Simple ansible playbook, which:
- Install Docker
- Create docker-compose
- Run Flask-app

## How to run

```bash
ansible-playbook -i inventory.ini playbook.yml

# Ansible Lint Rules
[![Build Status](https://travis-ci.com/trevor-viljoen/ansible-lint-rules.svg?branch=master)](https://travis-ci.org/trevor-viljoen/ansible-lint-rules)

This is a package of custom [ansible-lint rules](https://github.com/ansible/ansible-lint).

| ID | Version Added | Sample Message | Description | Tags |
| ------ | ------ | ------ | ------ | ------ |
| ZL001 | v0.1.0 | master is a branch and not a valid tag in repo | Forces requirements.yml role versions to use valid tagged references and not a branch head. | meta, TagsOnly |

### Example Usage
```sh
$ pip install ansible-lint gitpython
$ ansible-lint -r ansible-lint-rules/rules -t TagsOnly requirements.yml
[ZL001] master is a branch and not a valid tag in repo: https://github.com/geerlingguy/ansible-role-nginx
test/bad_requirements.yml:2
{'test/bad_requirements.yml': {'src': 'https://github.com/geerlingguy/ansible-role-nginx', 'version': 'master', '__line__': 2, '__file__': 'test/bad_requirements.yml'}}

[ZL001] 0.0.0 is not a valid tag in repo: https://github.com/geerlingguy/ansible-role-certbot
test/bad_requirements.yml:4
{'test/bad_requirements.yml': {'src': 'https://github.com/geerlingguy/ansible-role-certbot', 'version': '0.0.0', '__line__': 4, '__file__': 'test/bad_requirements.yml'}}

[ZL001] 0.0.0 is not a valid tag in repo: https://github.com/geerlingguy/ansible-role-elasticsearch
test/bad_requirements.yml:6
{'test/bad_requirements.yml': {'src': 'https://github.com/geerlingguy/ansible-role-elasticsearch', 'version': '0.0.0', '__line__': 6, '__file__': 'test/bad_requirements.yml'}}
```

### Contributions Welcome
- Rules should have adequate tests.
- Commit messages should follow the [Conventional Commits Specification](https://www.conventionalcommits.org).
- Please submit a pull request

### Questions?
- Open an [issue](https://github.com/trevor-viljoen/ansible-lint-rules/issues)

#### License
----
[MIT](https://github.com/trevor-viljoen/ansible-lint-rules/blob/master/LICENSE)

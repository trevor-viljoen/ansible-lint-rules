from ansiblelint import AnsibleLintRule
from git import cmd


def ls_remote(url):
    """ Get remote tags/heads from git repo """
    remote_refs = []
    for ref in cmd.Git().ls_remote(url).split('\n'):
        hash_ref_list = ref.split('\t')
        ref = hash_ref_list[1].split('/')[-1]
        commit = hash_ref_list[0]
        if 'tags' in hash_ref_list[1]:
            remote_refs.append(dict(ref_type='tag', ref=ref, commit=commit))
        if 'heads' in hash_ref_list[1]:
            remote_refs.append(dict(ref_type='branch', ref=ref, commit=commit))
    return remote_refs


class RoleUsesTagRule(AnsibleLintRule):  # pylint: disable=invalid-name
    """ An ansible-lint rule to prevent a repo from pointing to a
    branch/HEAD.
    """
    id = 'ZL001'
    shortdesc = 'requirements.yml repos should not point to head of a branch'
    description = (
        'requirements.yml repos should point to a valid release/tag not to'
        ' the head of a branch'
    )
    severity = 'HIGH'
    version_added = 'v0.1.0'
    tags = ['metadata', 'TagsOnly']

    def matchplay(self, file, data):  # pylint: disable=no-self-use,inconsistent-return-statements,line-too-long
        """ Check requirements.yml for valid remote tag and ensure no heads
        are used
        """
        if 'requirements.yml' in file['path']:
            src = data.get('src', None)
            if 'git+https' in src:
                src = "{}:{}".format('https', src.split(':')[1])
            ver = str(data.get('version', None))
            if not src:
                return [({'requirements.yml': data}, "No 'src' found")]
            repo_name = src.split('/')[-1]
            if '.git' in repo_name:
                repo_name = repo_name.split('.')[0]
            refs = ls_remote(src)
            # separate tags from branches
            tags = [ref for ref in refs if ref['ref_type'] == 'tag']
            branches = [ref for ref in refs if ref['ref_type'] == 'branch']
            if ver:
                if ver in [str(branch['ref']) for branch in branches]:
                    errmsg = "{} is a branch and not a valid tag in repo: {}".format(ver, src)
                    return [({file['path']: data}, errmsg)]
                if ver not in [str(tag['ref']) for tag in tags]:
                    errmsg = "{} is not a valid tag in repo: {}".format(ver, src)
                    return [({file['path']: data}, errmsg)]

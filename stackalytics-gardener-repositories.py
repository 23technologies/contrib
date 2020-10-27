import github
import json

config = []
modules = []

gh = github.Github()
 
for repository in gh.get_organization("gardener").get_repos(sort='full_name'):

    if repository.name == 'gardener':
        data = {
            'module': repository.name,
            'organization': 'gardener',
            'uri': repository.clone_url
        }
        modules.append(repository.name)
    else:
        data = {
            'module': "%s@gardener" % repository.name,
            'organization': 'gardener',
            'uri': repository.clone_url
        }
        modules.append("%s@gardener" % repository.name)

    config.append(data)

print(json.dumps(config, indent=4))
print
print
print(json.dumps(modules, indent=4))

import ruamel.yaml

yaml = ruamel.yaml.YAML()
data = yaml.load(open('environment.yml'))

requirements = []
for dep in data['dependencies']:
    if isinstance(dep, str):
        if '>=' in dep:
            package, package_version = dep.split('>=')
            requirements.append(package + '>=' + package_version)
        elif '<=' in dep:
            package, package_version = dep.split('<=')
            requirements.append(package + '<=' + package_version)
        elif '==' in dep:
            package, package_version = dep.split('==')
            requirements.append(package + '==' + package_version)
        elif '=' in dep:
            package, package_version = dep.split('=')
            requirements.append(package + '==' + package_version)
        else:
            package = dep
            requirements.append(package)
    elif isinstance(dep, dict):
        for preq in dep.get('pip', []):
            requirements.append(preq)

with open('requirements.txt', 'w') as fp:
    for requirement in requirements:
       print(requirement, file=fp)
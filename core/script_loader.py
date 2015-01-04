import importlib


def underscore_to_camelcase(word):
    return ''.join(x.capitalize() for x in word.split('_'))


def load_scripts(root_package, installed_scripts):
    """
    Loads all script classes in: root_package
    :return: list of script classes
    """
    scripts = []
    for script_name in installed_scripts:
        module_path = '{0}.{1}.{1}'.format(root_package, script_name)
        module = importlib.import_module(module_path)
        scripts.append(getattr(module, underscore_to_camelcase(script_name)))
    return scripts
import os
import venv
import subprocess
from random import choice, randrange
from template_flask.constants import *


def generate_random_secret_key():
    key = ''
    for i in range(32):
        alpha = choice([chr(randrange(65, 91)), chr(randrange(97, 123))])
        num = chr(randrange(48, 58))
        sym = choice([chr(randrange(33, 48)), chr(randrange(58, 65)), chr(randrange(123, 127))])
        key += choice([alpha, num, sym])
    return key


def write_file(file_path, iterable_lines, fills: dict={}):
    with open(file_path, 'w') as f:
        for line_number in iterable_lines:
            line_to_write = iterable_lines[line_number][0]
            needs_fill = iterable_lines[line_number][1]

            if needs_fill:
                f.write(f'{line_to_write.format(**fills)}\n')
            else:
                f.write(f'{line_to_write}\n')


def create_dir_and_venv(project_name: str, project_directory: str):
    FILLS = {
        'app': project_name,
        'secret_key': generate_random_secret_key(),
    }

    full_path = os.path.join(project_directory, project_name)
    os.mkdir(full_path)

    venv_path = os.path.join(full_path, 'venv')
    venv.create(venv_path, with_pip=True)

    package_path = os.path.join(full_path, f'{project_name}_app')
    config_dir = os.path.join(package_path, 'config')
    models_dir = os.path.join(package_path, 'models')
    routes_dir = os.path.join(package_path, 'routes')
    static_dir = os.path.join(package_path, 'static')
    templates_dir = os.path.join(package_path, 'templates')

    index_path = os.path.join(templates_dir, 'index.html')

    config_init = os.path.join(config_dir, '__init__.py')
    config_config = os.path.join(config_dir, 'app_config.py')

    models_init = os.path.join(models_dir, '__init__.py')
    models_db = os.path.join(models_dir, 'db.py')
    models_model = os.path.join(models_dir, 'model.py')

    routes_init = os.path.join(routes_dir, '__init__.py')
    routes_routes = os.path.join(routes_dir, 'routes.py')

    run_main = os.path.join(package_path, 'run.py')
    init_main = os.path.join(package_path, '__init__.py')

    os.mkdir(package_path)
    os.mkdir(config_dir)
    os.mkdir(models_dir)
    os.mkdir(routes_dir)
    os.mkdir(static_dir)
    os.mkdir(templates_dir)

    write_file(index_path, INDEX_HTML, fills=FILLS)

    write_file(config_init, CONFIG_INIT)
    write_file(config_config, CONFIG_CONFIG, fills=FILLS)

    write_file(models_init, MODEL_INIT, fills=FILLS)
    write_file(models_db, MODEL_DB)
    write_file(models_model, MODEL_MODEL, fills=FILLS)

    write_file(routes_init, ROUTE_INIT)
    write_file(routes_routes, ROUTE_ROUTE, fills=FILLS)

    write_file(run_main, RUN, fills=FILLS)
    write_file(init_main, INIT, fills=FILLS)


def activate_venv_and_install_reqs(project_name: str, project_directory: str):
    full_path = os.path.join(project_directory, project_name)
    reqs_path = os.path.join(full_path, 'requirements.txt')
    venv_path = os.path.join(full_path, os.path.join('venv', 'Scripts'))

    os.chdir(venv_path)
    cmd = f'python -m pip install {" ".join(REQUIREMENTS)}'
    subprocess.run(cmd, shell=True)
    print()

    cmd = f'python -m pip freeze'
    reqs = [x.decode('utf-8').split('==')[0]
            for x in subprocess.run(cmd, check=True, stdout=subprocess.PIPE, shell=True).stdout.splitlines()]

    print('Completed installing requirements into virtual environment\n')
    for req in reqs:
        print(req)
    print()
    print('Packages above have been automatically installed into virtual environment')

    with open(reqs_path, 'w') as f:
        for req in reqs:
            f.write(f"""{req}\n""")

    print('Completed writing initial "requirements.txt"\n')
























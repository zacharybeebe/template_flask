
CON = {
    'app': 'test_app',
    'secret_key': 'HDHUDHUDNISKO',
    'other': 'Zach'
}

x = "{app}___{secret_key}___"

print(x.format(**CON))
"""
Generating Markdown documentation from populus compiled contracts.json
Populus: https://github.com/ethereum/populus
"""


import sys
import json
import click


input_titles = ['name', 'type', 'indexed', 'description']
output_titles = ['name', 'type']

@click.command()
@click.option(
    '--input',
    default='build/contracts.json',
    help='Path to populus compiled contracts data.'
)
@click.option(
    '--output',
    default='docs.md',
    help='Path to output file.'
)
@click.option(
    '--contracts',
    default=None,
    help='What contracts to build documentation for.'
)
def main(**kwargs):
    input_file = kwargs['input']
    output_file = kwargs['output']
    contract_names = kwargs['contracts']
    content = ''

    with open(input_file) as json_data:
        contract_data = json.load(json_data)
        if not contract_names:
            contract_names = list(contract_data.keys())
        else:
            contract_names = contract_names.split(',')

        for contract_name in contract_names:
            if not contract_data[contract_name]['metadata']:
                continue
            abi = contract_data[contract_name]['abi']
            devdoc = contract_data[contract_name]['metadata']['output']['devdoc']['methods']
            userdoc = contract_data[contract_name]['metadata']['output']['userdoc']['methods']

            constant_methods = [x for x in abi if x['type'] == 'function' and x['constant'] == True]
            state_change_methods = [x for x in abi if x['type'] == 'function' and x['constant'] == False]
            constructor = [x for x in abi if x['type'] == 'constructor']
            events = [x for x in abi if x['type'] == 'event']

            content += '# %s\n\n' % (contract_name)

            if len(constructor):
                constructor = constructor[0]
                # content += add_method(constructor)

            if len(state_change_methods):
                content += '## Non-Constant Functions\n\n'
                content += add_methods(state_change_methods, devdoc, userdoc)

            if len(constant_methods):
                content += '## Constant Functions\n\n'
                content += add_methods(constant_methods, devdoc, userdoc)

            if len(events):
                content += '## Events\n\n'
                content += add_methods(events, devdoc, userdoc)

            content += '\n\n'


        with open(output_file, 'w') as f:
            f.write(content)


def add_methods(methods, devdoc=None, userdoc=None):
    content = ''
    for method in methods:
        method_name = '%s(%s)' % (
            method['name'],
            ','.join([x['type'] for x in method['inputs']])
        )
        if method_name in devdoc.keys():
            method_devdoc = devdoc[method_name]
        else:
            method_devdoc = None

        if method_name in userdoc.keys():
            method_userdoc = userdoc[method_name]
        else:
            method_userdoc = None

        content += add_method(method, method_devdoc, method_userdoc)
        content += '\n'
    return content

def add_method(method, devdoc=None, userdoc=None):
    content = ''
    # Method name
    content += '### %s\n' % (method['name'])

    # Method description
    if userdoc and 'notice' in userdoc.keys():
        content += '%s\n' % (userdoc['notice'])
    if devdoc and 'details' in devdoc.keys():
        content += '%s\n' % (devdoc['details'])

    # Method input parameters
    if method['inputs']:
        content += '\n#### Input parameters\n'
        content += params_header(input_titles)
        for param in method['inputs']:
            content += add_param(param, input_titles, devdoc, userdoc)
        content += '\n'

    if method.get('outputs'):
        content += '\n#### Output\n'
        if devdoc and 'return' in devdoc.keys():
            content += '\nFunction returns: %s\n' % (devdoc['return'])
        content += params_header(output_titles)
        for param in method['outputs']:
            content += add_param(param, output_titles, devdoc, userdoc)
        content += '\n'

    return content


def add_param(param, titles, devdoc=None, userdoc=None):
    content = '\n|'
    for title in titles:
        if title == 'description':
            continue
        text = None
        if title in param.keys():
            text = param[title]
        if devdoc and 'params' in devdoc and title in devdoc['params'].keys():
            text = devdoc['params'][title]
        if text:
            content += '%s|' % (text)
        else:
            content += '|'
    if devdoc and 'params' in devdoc and param['name'] in devdoc['params'].keys():
        content += '%s|' % (devdoc['params'][param['name']])
    else:
        content += '|'
    return content


def params_header(names):
    content = '\n'
    content += '|%s|\n' % ('|'.join(names))
    content += '|%s|' % ('|'.join(['---'] * len(names)))
    return content

if __name__ == '__main__':
    main()

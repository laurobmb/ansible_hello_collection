# my_collection/plugins/modules/hello_plugin.py

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    name = module.params['name']
    greeting = f"Hello, {name}!"

    result = dict(
        changed=False,
        msg=greeting
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()

# Documentação do módulo
DOCUMENTATION = '''
---
module: hello_plugin
short_description: Exemplo de módulo Ansible em Python
description:
    - Este módulo exibe uma mensagem de saudação.
options:
    name:
        description:
            - O nome para o qual exibir a saudação.
        required: true
notes:
    - Exemplo de uso:
        - name: Use Hello Plugin
          my_collection.hello_plugin:
            name: "John Doe"
          register: hello_result

        - name: Display Greeting
          debug:
            var: hello_result.msg
'''

EXAMPLES = '''
- name: Exemplo de uso do Hello Plugin
  my_collection.hello_plugin:
    name: "Jane Doe"
  register: hello_result

- name: Exibir saudação
  debug:
    var: hello_result.msg
'''


# Ansible Collection - laurobmb.hello

Documentation for the collection.

### Galaxy collection build
> ansible-galaxy collection build
### Galaxy collection install from file
> ansible-galaxy collection install laurobmb-hello-1.0.0.tar.gz
### Galaxy collection install from git
> ansible-galaxy collection install git+https://github.com/laurobmb/ansible_hello_collection.git,main

> ansible-galaxy collection install laurobmb-hello-1.0.4.tar.gz -p collections/

### Playbook sample
    ---
    - name: Utilizando o módulo personalizado
      hosts: localhost
      tasks:
        - name: Usar o módulo Hello Plugin
          laurobmb.hello.hello_plugin:
            name: "Lauro Gomes"
          register: hello_result

        - name: Exibir saudação
          ansible.builtin.debug:
            var: hello_result.msg

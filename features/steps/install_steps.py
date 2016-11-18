from behave import given

from captainhook.checkers.utils import bash_no_errors


@given('I have installed captainhook')
def step_impl(context):
    bash_no_errors('captainhook install')


@given('I have a tox.ini file with {settings}')
def step_configure_tox(context, settings):
    with open('tox.ini', 'w') as f:
        f.write('[captainhook]\n')
        for setting in settings.split(','):
            if setting:
                f.write("{0}\n".format(setting.strip()))

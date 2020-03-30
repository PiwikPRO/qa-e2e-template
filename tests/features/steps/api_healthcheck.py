from behave import step
from features.lib.pages import *


@step('I get list all apps')
def step_impl(context):
    api = Api(context)
    api.get_apps()

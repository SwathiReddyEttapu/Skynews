
from behave import *
from skynews_code import SkyNewsMain

@given('I launch Sky News website')
def step_impl(context):
    context.skynewsobj = SkyNewsMain()
    context.skynewsobj.launch_browser()

@when('I check for the browser tab\'s title')
def step_impl(context):
    context.skynewsobj.check_browser_title()

@then('it should return the title "The Latest News from the UK and Around the World | Sky News"')
def step_impl(context):
    assert context.skynewsobj.verify_returned_title()

@then('I should see all categories')
def step_impl(context):
    assert context.skynewsobj.check_categories()

@then('Home category should be active')
def step_impl(context):
    assert context.skynewsobj.check_home_categories()

@when('I click on Ocean Rescue')
def step_impl(context):
    context.skynewsobj.click_ocean_rescue()

@then('I should see the correct header text')
def step_impl(context):
    assert context.skynewsobj.check_header_text()

from behave import *

@given('Open Maestro QA Test Page')
def step_impl(context):
    context.app.ROICalculator.open_roicalculator()

@then('Click on cookies banner')
def step_impl(context):
    context.app.ROICalculator.cookiesbanner()

@then('Click Goto calculator')
def step_impl(context):
    context.app.ROICalculator.goto_calculator()

@then('Check if title exists {title}')
def step_impl(context, title):
    context.app.ROICalculator.find(title)

@then('Fillout the number of graders field with {num}')
def step_impl(context, num):
    context.app.ROICalculator.fillout_numofgraders_field(num)

@then('Fillout the number of agents field with {num}')
def step_impl(context, num):
    context.app.ROICalculator.fillout_numofagents_field(num)

@then('Fillout the number of percentage field with {num}')
def step_impl(context, num):
    context.app.ROICalculator.fillout_percents_field(num)

@then('Fillout the first name field with {firstName}')
def step_impl(context, firstName):
    context.app.ROICalculator.fillout_firstName(firstName)

@then('Fillout the last name field with {lastName}')
def step_impl(context, lastName):
    context.app.ROICalculator.fillout_lastName(lastName)

@then('Click next')
def step_impl(context):
    context.app.ROICalculator.click_next_button()

@then('Select the number of agents')
def step_impl(context):
    context.app.ROICalculator.selectNumOfAgents()

@then('Fillout the number of minutes of AHT with {num}')
def step_impl(context, num):
    context.app.ROICalculator.filloutNumOfMinutesOfAHT(num)

@then('Fillout the email field with {email}')
def step_impl(context, email):
    context.app.ROICalculator.filloutEmail(email)

@then('Select Number of tickets per year {num}')
def step_impl(context, num):
    context.app.ROICalculator.filloutNumOfTickets(num)


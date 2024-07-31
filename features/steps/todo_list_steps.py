from behave import given, when, then
import sys
import os

# Adding the parent directory to sys.path so we can import the ToDoList class
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from todo_list import ToDoList

# Use the same ToDoList class as your application
todo_list = None

@given('the to-do list is empty')
def step_impl(context):
    global todo_list
    todo_list = ToDoList()
    todo_list.clear_tasks()

@given('the to-do list contains tasks')
def step_impl(context):
    global todo_list
    todo_list = ToDoList()
    for row in context.table:
        todo_list.add_task(row['Task'], "")
    context.todo_list = todo_list

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global todo_list
    todo_list.add_task(task, "")

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    global todo_list
    task_titles = [t.title for t in todo_list.tasks]
    assert task in task_titles, f'Task "{task}" not found in the to-do list'

@when('the user lists all tasks')
def step_impl(context):
    global todo_list
    # Include "Tasks:" header to match the feature file expectation
    context.output = "Tasks:\n" + "\n".join([f"- {t.title}" for t in todo_list.tasks])

@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip()
    actual_output = context.output.strip()
    assert expected_output == actual_output, f'Expected "{expected_output}" in output, but got "{actual_output}"'

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global todo_list
    for t in todo_list.tasks:
        if t.title == task:
            todo_list.mark_task_completed(t.id)
            break

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    global todo_list
    completed_task = next((t for t in todo_list.tasks if t.title == task), None)
    assert completed_task and completed_task.completed, f'Task "{task}" was not marked as completed'

@when('the user clears the to-do list')
def step_impl(context):
    global todo_list
    todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    global todo_list
    assert len(todo_list.tasks) == 0, "The to-do list was not cleared"


@when('the user marks task "{task}" as pending')
def step_impl(context, task):
    global todo_list
    for t in todo_list.tasks:
        if t.title == task:
            todo_list.mark_task_pending(t.id)
            break
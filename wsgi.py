import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)


import click
from App import create_app
from App.controllers import student_controller, staff_controller

from App.controllers.student_controller import request_hours
from App.controllers.staff_controller import approve_hours, log_hours
app.cli.add_command(request_hours)
app.cli.add_command(approve_hours)
app.cli.add_command(log_hours)
app = create_app()

# STUDENT COMMANDS
@app.cli.command("request-hours")
@click.argument("student_id", type=int)
@click.argument("activity")
@click.argument("hours", type=float)
def request_hours(student_id, activity, hours):
    entry = student_controller.request_hours(student_id, activity, hours)
    click.echo(f"Requested {hours}h for {activity} (id={entry.id})")

@app.cli.command("leaderboard")
def leaderboard():
    board = student_controller.view_leaderboard()
    for name, total in board:
        click.echo(f"{name}: {total}h")

@app.cli.command("accolades")
@click.argument("student_id", type=int)
def accolades(student_id):
    accs = student_controller.view_accolades(student_id)
    for a in accs:
        click.echo(a)

# STAFF COMMANDS
@app.cli.command("log-hours")
@click.argument("student_id", type=int)
@click.argument("activity")
@click.argument("hours", type=float)
@click.argument("staff_name")
def log_hours(student_id, activity, hours, staff_name):
    entry = staff_controller.log_hours(student_id, activity, hours, staff_name)
    click.echo(f"Staff {staff_name} logged {hours}h for {activity}")

@app.cli.command("approve-hours")
@click.argument("entry_id", type=int)
@click.option("--status", default="approved")
def approve_hours(entry_id, status):
    entry = staff_controller.approve_hours(entry_id, status)
    if entry:
        click.echo(f"Updated entry {entry.id} → {status}")
    else:
        click.echo("Entry not found")

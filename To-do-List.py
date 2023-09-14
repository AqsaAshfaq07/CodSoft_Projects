# This is a Python To-do-List
import self as self

# Things to do
# Create
# Update
# View

# Flow Chart
# create a class
# Inside the constructor Function
# print -> My To-Do List
# Please choose a task to continue
# create, Update, View
# Define a function for create(), update(), view()


def to_do_list(self):
    print('TO-DO LIST')
    tasks = {}
    should_continue = True

    def create(id, task):
        tasks.update({id : task})
        print('Task added Successfully!')

    def update(id, updated_task):
        tasks[id] = updated_task
        print('Task updated Successfully!')

    def view():
        if tasks == {}: print('You haven\'t added any to-dos yet')
        else:
            for value in tasks.values() : print(value)

    while should_continue:
        choice = input('Please choose a task to continue: \nCreate / Update / View: ')
        if choice.lower() == 'create':
            task, id = input('Enter the task: '), input('And a unique ID: ')
            create(id, task)

        elif choice.lower() == 'update':
            updated_task, id = input('Enter the new text: '), input('Enter the ID: ')
            update(id, updated_task)

        elif choice.lower() == 'view':
            return view()

        else:
            print('Please give a valid input!')

        exit = input('Type yes to continue / no to exit! ')
        if exit == 'yes': should_continue = True
        else: should_continue = False


to_do_list(self)

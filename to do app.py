
class Task:
    def __init__(self, title, description, priority, status):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    def view_tasks(self):

        print(f'''
Title: {self.title}
Description: {self.description}
Priorty: {self.priority}
Status: {self.status}''')


      
class TaskManager:
    def __init__(self):
        self.task_list = []
        
    def add_task(self, task):
        self.task_list.append(task)

    def view_all_tasks(self):
        if len(self.task_list) > 0:
            for task in self.task_list:
                task.view_tasks()
        else:
            print('Nothing is in the list! ')

    def view_pending_tasks(self):
        for tasks in self.task_list:
            if tasks.status == 'Incomplete':
                print('Following are the pending tasks! ')
                tasks.view_tasks()  
            else:
                print('No pending tasks :)')
            
    def remove_task(self, title):
        for task in self.task_list:
            if task.title.lower() == title.lower():
                self.task_list.remove(task)

    def mark_task_completed(self, completed_tasks):
        for task in self.task_list:
                if task.title.lower() == completed_tasks.lower():
                    task.status = 'Completed'
                    print(f'Task {task.title} is marked as completed')  
                else:
                    print(f'No task found named "{completed_tasks}". ')
                    
                    



taskManger = TaskManager()

def main():
    while True:
        print('''
1. Add task
2. Remove task
3. View all tasks
4. View pending tasks
5. Mark tasks as completed 
6. Exit
''')
        user_input = input('> ')
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:

                title = input('Enter the title of the task: ')
                description = input('Enter the description of the task: ')
                priority = input('Choose the priority of the task (High, Med, Low): ')
                priorities = ['high', 'med', 'low']



                while True:
                    if priority.lower() not in priorities:
                        priority = input('Enter the valid prioirty from (High, Med, Low): ')
                    else:
                        # status = 'Incomplete'
                        task = Task(title, description, priority, status= 'Incomplete')
                        taskManger.add_task(task)
                        break

            elif user_input == 2:
                user_input = input('Enter the title of the task, you wanna remove: ')
                taskManger.remove_task(user_input)
        
            elif user_input == 3:
                taskManger.view_all_tasks()

            elif user_input == 4:
                taskManger.view_pending_tasks()

            elif user_input == 5:
                taskManger.view_pending_tasks()

                user_input = input('Enter the title of the task, you have completed: ')
                taskManger.mark_task_completed(user_input)

            elif user_input == 6:
                print('Exiting...')
                break

            else:
                print('Choose the valid option! ')
        else:
            print('Choose from the following by their serial number! ')
main()
#!/usr/bin/python3
import cmd

class Myconsole(cmd.Cmd):
    intro = "Welcome to your to-do app Charity :-)"
    prompt = "(charity): "

    def __init__(self):
        super().__init__()
        self.list = []  #store tasks in a list

    def do_createtask(self, task):
        """creates a new task"""
        if task not in self.list:
            self.list.append(task)
            print(f"the task '{task}' has been created")
        else:
            print(f"task '{task}' already exists, try updating...")

    def do_list_tasks(self, _):
        """lists the available tasks"""
        if not self.list:
            print("no tasks found")
        else:
            for task in self.list:
                print(f"{task}")  # Access task name correctly

    def do_update_task(self, task):
        """updates an existing task"""
        if task not in self.list:
            print(f"task '{task}' doesn't exist, try creating first")
        else:
            new_task = input("Input your new task here: ")
            indx = self.list.index(task)
            self.list[indx] = new_task
            print(f"task '{task}' updated successfully")

    def do_delete_task(self, task):
        """deletes a specified task"""
        if task in self.list:
            self.list.remove(task)
            print(f"deleted '{task}'")
        else:
            print(f"task '{task}' not found")

    def do_exit(self, _):
        """exits the command-line interface"""
        return True

if __name__ == "__main__":
    Myconsole().cmdloop()

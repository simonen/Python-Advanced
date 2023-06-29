from project.task import Task
from project.section import Section

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
section_new = Section('New section')
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.complete_task(second_task.name))
print(section.complete_task(task.name))
print(section.clean_section())
print(section.view_section())

section_new.add_task(second_task)
print(section_new.view_section())
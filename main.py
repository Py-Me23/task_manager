# use loop to calculate the sum of the numbers below
#numbers = [10, 5, 8, 15]
#total_sum= 0

#for num in numbers:
    #total_sum += num
#print(total_sum)
# define a function add task

import add
import show
import update
import delete

add_task_response= add.add_task("sleep")
print(add_task_response)

show_task_response= show.show_task()
print(show_task_response)

update_task_response= update.update_task("sleep", "wake up")
print(update_task_response)

delete_task_response= delete.delete_task("wake up")
print(delete_task_response)

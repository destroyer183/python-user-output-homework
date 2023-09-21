from cProfile import label
import tkinter as tk
import math
import statistics

root = tk.Tk()

root.title("HW stuff")

root.geometry('500x260')

task1 = tk.Label(root, text = "Task 1: Python Rocks!")

task1.place(x = 50, y = 25)

task2 = tk.Label(root, text = " Task 2: Welcome to Richmond Green")

task2.place(x = 200, y =25)

task21 = tk.Label(root, text = "Computer Science")

task21.place(x = 240, y = 50)

task3 = 12345 + 58273 - 38200 / 2 + 510 * 342

task31 = tk.Label(root, text = "Task 3: " + str(task3))

task31.place(x = 50, y = 60)

task4 = 8.99 * 0.13
task41 = 8.99 * 1.13

task42 = tk.Label(root, text = "Task 4: Tax on $8.99 lunch: $" + str(task4))
task42.place(x = 200, y = 90)

task43 = tk.Label(root, text = "Total cost: $" + str(task41))
task43.place(x = 220, y = 115)

task5 = 375 / 60
task5 = math.floor(task5)

task51 = tk.Label(root, text = "Task 5: There are " + str(task5) + " hours")
task511 = tk.Label(root, text = "in 375 minutes.")
task51.place(x = 25, y = 100)
task511.place(x = 25, y = 125)

task6 = 6 * 3.14159
task6 = round(task6, 2)

task61 = tk.Label(root, text = "Task 6: The circumfrence of a circle ")
task611 = tk.Label(root, text = "with a diameter of 6m is " + str(task6) + "m")

task61.place(x = 25, y = 160)
task611.place(x = 25, y = 185)

data1 = [17, 24, 30]
task7 = statistics.mean(data1)
task7 = round(task7, 2)

task71 = tk.Label(root, text = "Task 7: The average of 17, 24, and 30 " + "is " + str(task7))

task71.place(x = 240, y = 160)

task8 = tk.Label(root, text = "Task 8: FIFA World Cup in Canada 2026")
task8.place(x = 15, y = 220)

task9 = tk.Label(root, text = "Task 9: the result of the following expression:")
task9.place(x = 240, y = 220)

root.mainloop()
import webbrowser
import time

#problem 1
def make_some_entries():
    entries=[]
    while True:
    	print()
        add_entry= input("Add some data here: ")
        if add_entry not in entries:
            entries.append(add_entry)
            print("Added")
        elif add_entry in entries:
            print("This already exists")

        if len(entries) == 5:
        	print("Database full")
        	return False
make_some_entries()

# problem 2
class make_triangles():
	def triangle(number):
		for item in range(1, number + 1):
			print("." * item)
	def triangle_backwards(number):
		for item in range(1, number + 1):
			back_triangle = ("." * item)
			print(back_triangle.rjust(4, " "))
	def triangle_upside_down(number):
	    for item in range(number, 0, - 1):
	        print("." * item)
	triangle(4)
	print()
	triangle_backwards(4)
	print()
	triangle_upside_down(4)
	print()

make_triangles()

#problem 3
class Fibbonacci:
	def fib_count(number):
		firstnum = 0
		secondnum = 1
		for num in range(0, number):
			print(firstnum)
			thirdnum = firstnum
			firstnum = secondnum
			secondnum = thirdnum + secondnum
		return firstnum
	fib_count(15)
Fibbonacci()

#problem 4
class Construction():
	def open_browser():
		webbrowser.open_new_tab("https://www.youtube.com/watch?v=hl_9_q_uLF8")

	open_browser()
	time.sleep(3)
	def __del__(self):
		webbrowser.open_new_tab("https://youtu.be/JwXohnAYyuc?t=22s")

Construction()	
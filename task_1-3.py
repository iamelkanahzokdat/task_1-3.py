#task1

Favourite_Movies = ["Green Knight", "The Matrix", "Ratatoullie", "Blood of Zeus", "EEAO", "Babadook"]
List_of_numbers = [1,2,3,4,5,6,7,8,9,10]
Mixed_list = ["Dre", 22, False, "male", 5.11, "Black or Blue"]
List_of_provision = ["Noodles", "Rice", "Milk", "Pocket Money", "Beans"] 
print(Favourite_Movies[::1])	
print(List_of_numbers[::1])
print(Mixed_list[::1])
print(List_of_provision[::1])

#task2

code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-    ", "n", " ", "W", "@", "r", "d", "o", "#"]
print(code[1] + code[2] + code[4] + code[4] + code[8])
print(code[-6] + code[-2] + code[-4] + code[5] + code[-3])
print(code[::-1])

#task3

grid = [
["The", "sky", "is"],
["full", "of", "stars"],
["shinning", "bright", "tonight"]
]

print(grid[0][0], grid[0][1])
print(grid[0][0], grid[1][2], "are", grid[2][0])
print(grid[1][::-1])


#task4

playlist = ["Song A", "Song B", "Song C"]
print("Before Update>>>>>>>")
print(playlist)
playlist[1] = "Song D"
print("After Update>>>>>>>>")
print(playlist)
print("new update")
playlist.append("Song E")
print(playlist)
print("new update")
playlist.insert(0, "Intro")
print(playlist)


#task5

desks = []
student1 = input("Enter Student name: ")
student2 = input("Enter Student name: ")
student3 = input("Enter Student name: ")
desks = [student1, student2, student3]
print("Second student's name change>>>>")
desks[1] = input("Enter new student's name: ")
print('''Second student's name changing....

Second student's name changed!''')
desks.insert(1, input("Enter new student name: "))
print(desks)



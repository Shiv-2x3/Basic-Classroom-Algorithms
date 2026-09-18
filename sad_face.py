counter = 0
where = input("Go left or right: ")
while where == "right":
    where = input("Go Left or Right? ")
    counter += 1
    if counter > 2:
        print(":(")
print("you got out")
print(counter)
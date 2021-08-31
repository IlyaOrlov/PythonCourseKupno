with open("1.txt", "r") as f1:
    with open("2.txt", "w") as f2:
        f2.write(f1.read())

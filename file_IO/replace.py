with open("practice.txt","w") as f:
          f.write("Hi everyone\nwe are learning File I/O")
          f.write("nusing Java\nI like programming in Java")


with open("practice.txt","r")as f:
        data=f.read()
        new_data=data.replace("Java","Python")
with open("practice.txt","w") as f:
        f.write(new_data)

print(new_data)




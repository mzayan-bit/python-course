def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")

check_for_word()

def check_for_line():
    word="learning"
    with open("practice.txt","r") as f :
        data=f.read()
        line_count=1
        if(word in data):
            print(line_count)
            return
        line_count+=1
    
    return -1

check_for_line()
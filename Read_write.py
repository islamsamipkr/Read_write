with open("data.txt","r") as datafile:
    f=datafile.read()
    print(f)
with open("data.txt", "a") as datafile:
    datafile.write("Arekta Hagu Pacha")
with open("data.txt", "r") as datafile:
    f = datafile.read()
    print(f)
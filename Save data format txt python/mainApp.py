def Print():
    load_data = open("savedat.txt", "r")
    load = load_data.readlines()
    print(load)


def Load():
    load_data = open("savedat.txt", "r")
    load = load_data.readlines()
    return load


def Save(input_data):
    save_data = open("savedat.txt", "w")
    save_data.writelines(f"{input_data}, ")


data_pre_save = []
run = True
while run:
    load = Load()
    Save(load)

    input_data = input("input: ")
    Save(input_data)
    if input_data == "exit":
        run = False

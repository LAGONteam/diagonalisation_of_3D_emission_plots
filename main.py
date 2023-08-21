from pathlib import Path
def run():
    print("Please give the path of the files")
    file = input()
    data=read_file(file)
    new_data= remove_artifacts(data)
    # new_data = remove_duplicates(data)
    state = write_file(file, new_data)
    if state:
        print("Successful")
    else:
        print("Fail")

def read_file(file):
    raw_data = open(file).readlines()
    return raw_data
def remove_duplicates(raw_data):
    data_to_search = None
    new_data = []
    for n in range(len(raw_data)):
        first_index = raw_data[n].find("\t")
        first_data = raw_data[n][0:first_index]
        second_index = raw_data[n][first_index+1:-1].find("\t")
        second_data = raw_data[n][first_index+1:first_index+second_index+1]
        third_index = raw_data[n].find("\n")
        if third_index == -1:
            third_data = raw_data[n][first_index + second_index+2:]
        else:
            third_data = raw_data[n][first_index+second_index+2: third_index]
            real_third_data=third_data
        if third_data == data_to_search:
            third_data = "1"
        if n == len(raw_data)-1:
            concatenated_data = first_data + "\t"+second_data+"\t"+third_data
        else:
            concatenated_data = first_data + "\t" + second_data + "\t" + third_data + "\n"
        new_data.append(concatenated_data)
        data_to_search = real_third_data
    print(new_data)
    return new_data

def remove_artifacts(raw_data):
    data_to_search = None
    new_data = []
    for n in range(len(raw_data)):
        first_index = raw_data[n].find("\t")
        first_data = raw_data[n][0:first_index]
        second_index = raw_data[n][first_index+1:-1].find("\t")
        second_data = raw_data[n][first_index+1:first_index+second_index+1]
        third_index = raw_data[n].find("\n")
        if third_index == -1:
            third_data = raw_data[n][first_index + second_index+2:]
        else:
            third_data = raw_data[n][first_index+second_index+2: third_index]
            real_third_data=third_data
        if float(first_data) <=  float(second_data) or third_data == data_to_search:
            third_data = "1"
        if n == len(raw_data)-1:
            concatenated_data = first_data + "\t"+second_data+"\t"+third_data
        else:
            concatenated_data = first_data + "\t" + second_data + "\t" + third_data + "\n"
        new_data.append(concatenated_data)
        data_to_search = real_third_data
    return new_data
def write_file(file, new_data):
    new_data = "".join(new_data)
    new_file = Path(file.replace(".txt", "_corr.txt"))
    new_file.touch()
    temp_file = open(new_file, "w")
    temp_file.write(new_data)
    temp_file.close()

    return True

if __name__ == "__main__":
    a = run()

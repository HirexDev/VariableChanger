import os

print("""
________________________________________________________________________________________
|                   _        _     _                 _                 __ _            |
|  __ __ __ _  _ _ (_) __ _ | |__ | | ___        __ | |_   __ _  _ _  / _` | ___  _ _  |
|  \ V // _` || '_|| |/ _` ||  _ \| |/ -_)      / _||   \ / _` || ' \ \__. |/ -_)| '_| |
|   \_/ \__/_||_|  |_|\__/_||____/|_|\___|      \__||_||_|\__/_||_||_||___/ \___||_|   |
|______________________________________________________________________________________|
""")

User_path = input("Enter the url of the directory as in (example/example/example): ")
User_target = input("Enter the target variable: ")
User_amount = input("Enter the amount you want to change: ")

def change_var(correct_path):
    print("|           There is a .txt file!          |")
    with open(correct_path) as file:
        file_contents = file.read()
        if (User_target + "=") in file_contents or (User_target + " =") in file_contents:
            print('|        Target is in the .txt file!       |')
            lines_list = file_contents.split('\n')
            Target_index = 0
            for j in lines_list:
                Target_index += 1
                if User_target in j:
                    Target_index -= 1
                    break
            lines_list.remove(lines_list[Target_index])
            line_to_write = User_target + "=" + User_amount
            lines_list.insert(Target_index, line_to_write)
            lines_list = '\n'.join(lines_list)
            with open(correct_path, 'w') as file_Write:
                file_Write.write(lines_list)
                print("|------------------------------------------|\n|           successfully saved!            |\n|------------------------------------------|")
        else:
            print('|the .txt file does not content your target|')


def process_files(path):
    try:
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isfile(entry_path):
                change_var(entry_path)
            elif os.path.isdir(entry_path):
                process_files(entry_path)
    except FileNotFoundError:
        print("The url u entered doesn't exist")
def directory_changing(path):
    process_files(path)


directory_changing(User_path)

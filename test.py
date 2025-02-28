user_command =  "mark-in-progress 1"
splited_user_command = user_command.split()

if "mark" == splited_user_command[0].split("-")[0]:
    print(splited_user_command[0][5:])
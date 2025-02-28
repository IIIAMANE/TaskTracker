import json
from datetime import datetime

# Это каждый раз переписывает файл в []
with open("sample.json", "w") as f:
    f.write("[\n]")

def create_task(desc):

    with open("sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    current_time = datetime.now().isoformat()

    try:
        current_last_id = data[-1]["id"]
        id_for_create_task = current_last_id + 1
    except:
        id_for_create_task = 0


    new_entry = {
        "id": id_for_create_task,
        "desc": desc,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": None
    }

    data.append(new_entry)

    with open("sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        print(data)

def update_task(id, desc):
    # Ищется словарь, где id == введенному айди, изменяется описание,
    # изменяется/добавляется updatedAt 
    with open("sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for task in data:
            if task["id"] == id:
                task["desc"] = desc
                task["updatedAt"] = datetime.now().isoformat()

    with open("sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        print(data)

def delete_task(id):
    # Если введенное айди = id таски, то удалить таску(а как?, по индексу чтоли?)
    with open("sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        # До этого юзал del в цикле и он ломался
        index_for_delete = None
        for i in range(len(data)):
            if data[i]["id"] == id:
                index_for_delete = i
        del data[index_for_delete]

    with open("sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        print(data)

def mark(id, status):
    # Надо по айдишнику найти таску и изменить в ней статус на переданный
    with open("sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for task in data:
            if task["id"] == id:
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()

    with open("sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        print(data)

def list_tasks(status_filter=None):
    # list done -> я должен вывести все таски, где status == done
    # Если просто list, то я вывожу все таски
    with open("sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
        if status_filter is None:
            for task in data:
                print(task)

        else:
            for task in data:
                if task["status"] == status_filter:
                    print(task)
        

while True:
    # add/update/delete/mark-(in-progress/done/todo)/list/list done/todo/in-progress
    # Надо будет сделать функцию для вывода комманд, а то это пиздец
    user_command = input("task-cli: ")
    splited_user_command = user_command.split()
    if splited_user_command[0] == "add":
        desc = splited_user_command[1:]
        create_task(' '.join(desc))
        # ['хихихи', 'поиграть', 'в', 'валорантик'] ->
        # хихихи поиграть в валорантик
    elif splited_user_command[0] == "update":
        id = int(splited_user_command[1])
        desc = splited_user_command[2:]
        desc = ' '.join(desc)
        update_task(id, desc)
    elif splited_user_command[0] == "delete":
        id = int(splited_user_command[1])
        delete_task(id)
    elif splited_user_command[0].split("-")[0] == "mark":
        id = int(splited_user_command[1])
        status = splited_user_command[0][5:]
        mark(id, status)
    elif splited_user_command[0] == "list":
        if len(splited_user_command) > 1:
            list_tasks(splited_user_command[1])
        else:
            list_tasks()
    else:
        print("Такой команды нет. Введи help, чтобы посмотреть список команд.")

# Я бы мб этот код доработал исключениями, а то он вроде откисает пиздец от всего 
# И начал бы двигаться к todo list api, ну короче, хочу личные заметки через сервак с впном,
# Которые я бы юзал(ток траблы с apk, мб придется через тг бота делать)
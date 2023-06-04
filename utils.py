import json

from datetime import datetime


def get_data():
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filter_empty_from=False):
    data = [i for i in data if "state" in i and i["state"] == "EXECUTED"]
    if filter_empty_from:
        data = [i for i in data if "from" in i]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda i: i["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        recipient = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operations_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if "from" in i:
            sender = i["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        else:
            from_info, from_bill = "", ""
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient}
{operations_amount}""")
    return formatted_data

import csv
from collections import Counter


def most_common_food(data, name):
    foods = [row[1] for row in data if row[0] == name]
    common_food = Counter(foods).most_common(1)[0][0]
    return common_food


def number_hamburguers(data, name):
    result = 0
    for item in data:
        if item[0] == name and item[1] == 'hamburguer':
            result += 1
    return result


def never_ask(data, name):
    foods = set(line[1] for line in data if line[0] != name)
    all = set(line[1] for line in data if line[0] == name)
    return foods - all


def never_went(data, name):
    days = set(line[2] for line in data if line[0] != name)
    all = set(line[2] for line in data if line[0] == name)
    return days - all


def analyze_log(path_to_file):
    result = []
    if not path_to_file.endswith('csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, 'r') as file:
            files = csv.reader(file)

            for line in files:
                result.append(line)

        with open('data/mkt_campaign.txt', 'w') as new_file:
            new_file.write(f"{most_common_food(result, 'maria')}\n")
            new_file.write(f"{number_hamburguers(result, 'arnaldo')}\n")
            new_file.write(f"{never_ask(result, 'joao')}\n")
            new_file.write(f"{never_went(result, 'joao')}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')

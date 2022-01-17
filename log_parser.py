import argparse
import re
import json
from collections import defaultdict
import os


def parse_dir(args):
    '''
    Поверка на файл или дирректорию и поиск файлов формата *.logs в перереданном пути.
    :param args: path of log file or path dir.
    :return: path for logs files
    '''
    _path_to_logfiles = []
    if os.path.isfile(args.file):
        return args.file  # Путь до конкретного лог файла

    elif os.path.isdir(args.file):
        for file in os.listdir(args.file):
            if file.endswith(".log"):
                _path_to_logfile = os.path.join(args.file, file)
                _path_to_logfiles.append(_path_to_logfile)
        return _path_to_logfiles  # Путь до перечня лог файлов

    else:
        print("ERROR: Incorrect path to log file or directory")


def parse_log_file(log_file):
    '''
    На вход данной процедуре передается путь до файла логов.
    :param log_file:
    :return:
    '''
    dict_method = {"COUNT_REQUEST": 0, "METHOD": {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0, "OPTIONS": 0}}
    dict_ip_requests = defaultdict(int)
    list_ip_duration = []

    with open(log_file) as logfile:
        for line in logfile:
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|OPTIONS)", line)
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
            duration = int(line.split()[-1])
            date = re.search(r"\[\d.*?\]", line)
            url = re.search(r"\"http.*?\"", line)

            dict_method["COUNT_REQUEST"] += 1
            if method:
                dict_method["METHOD"][method.group(1)] += 1
                dict_ip_requests[ip] += 1
                dict_data_request = {"METHOD": method.group(1), "URL": "None", "IP": ip, "DURATION": duration,
                                     "DATE": date.group(0).split(" ")[0].lstrip("[")}
                if url:
                    dict_data_request["URL"] = url.group(0).strip("\"")

                list_ip_duration.append(dict_data_request)

        top3_req = dict(sorted(dict_ip_requests.items(), key=lambda x: x[1], reverse=True)[0:3])
        top3_duration_requests = sorted(list_ip_duration, key=lambda x: x["DURATION"], reverse=True)[0:3]

        result = {"count_request": dict_method["COUNT_REQUEST"],
                  "count_stat_method": dict_method["METHOD"],
                  "top3_ip_requests": top3_req,
                  "top3_duration_requests": top3_duration_requests
                  }
    return write_json_file(log_file, result)


def write_json_file(name_file, data):
    # запись результате в итоговый файл.
    with open(f"{name_file}.json", "w", encoding="utf-8") as file:
        result = json.dumps(data, indent=4)
        file.write(result)
        print(f" Result file: {name_file}.json \n {result}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', dest='file', action='store', help='log file or Path to logfile')
    args = parser.parse_args()
    # Получаем перечень лог файлов.
    path_logs_files = parse_dir(args)
    if isinstance(path_logs_files,
                  list):  # Если вернулся лист, значит в дирректории более 1 файла. Обрабатываем в цикле
        for path_f in path_logs_files:
            parse_log_file(path_f)
    else:
        parse_log_file(path_logs_files)

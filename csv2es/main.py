import os
import asyncio
import click
import csv

from utils import log
from es_mng import EsMng


def check_path(file_path):
    return os.path.exists(file_path)


def get_csv_path(file_path):
    return os.path.dirname(file_path), os.path.basename(file_path)


def parse_head(head):
    head = head.strip()
    return head.split(',')


def parse_line(line, head):
    return { h: line[i] for i, h in enumerate(head) if h }


async def do_upload(file_path):
    _, file_name = get_csv_path(file_path)
    file_name = file_name[:file_name.rfind('.')]
    es = EsMng()

    with open(file_path, mode='r', encoding='utf8') as f:
        head = parse_head(f.readline())
        log(head)
        csv_reader = csv.reader(f)
        data = []
        total = 0
        count = 0
        log('开始上传')

        for l in csv_reader:
            data.append(parse_line(l, head))

            if len(data) >= 1000:
                total += len(data)
                count += 1
                log('.' * count)
                await es.bulk_add_document(file_name, data)
                data = []

        if len(data) > 0:
            total += len(data)
            await es.bulk_add_document(file_name, data)
            data = []

        log('上传结束')
        log(f'总数：{total}')



@click.command()
@click.option('--file_path', help='csv文件路径')
def main(file_path):
    
    if not check_path(file_path):
        raise Exception('file_path错误')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_upload(file_path))


if __name__ == "__main__":
    main()

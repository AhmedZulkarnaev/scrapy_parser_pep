import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PepParsePipeline:

    def __init__(self):
        self.status_count = {}
        self.total_peps = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        if status in self.status_count:
            self.status_count[status] += 1
        else:
            self.status_count[status] = 1
        self.total_peps += 1
        return item

    def close_spider(self, spider):
        results_dir = os.path.join(BASE_DIR, 'results')

        os.makedirs(results_dir, exist_ok=True)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{current_time}.csv'
        file_path = os.path.join(results_dir, filename)

        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
            writer.writerow(['Total', self.total_peps])

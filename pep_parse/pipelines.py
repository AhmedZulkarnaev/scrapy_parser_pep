import csv
import os
from datetime import datetime

from .constants import RESULT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = os.path.join(BASE_DIR, RESULT)
        os.makedirs(results_dir, exist_ok=True)
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{current_time}.csv'
        file_path = os.path.join(results_dir, filename)

        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Status', 'Quantity'])
            writer.writerows(self.status_count.items())

            total = sum(self.status_count.values())
            writer.writerow(['Total', total])

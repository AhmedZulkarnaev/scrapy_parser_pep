import csv
import os
from datetime import datetime

from .constants import RESULT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PepParsePipeline:

    def __init__(self):
        self.status_count = {}
        self.total_peps = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item.get('status')
        self.status_count.setdefault(status, 0)
        self.status_count[status] += 1
        self.total_peps += 1
        return item

    def close_spider(self, spider):
        results_dir = os.path.join(BASE_DIR, RESULT)

        os.makedirs(results_dir, exist_ok=True)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{current_time}.csv'
        file_path = os.path.join(results_dir, filename)

        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['Status', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            total_docs = sum(self.status_count.values())
            for status, count in self.status_count.items():
                status_label = status if status else 'None'
                writer.writerow({'Status': status_label, 'Quantity': count})
            writer.writerow({'Status': 'Total', 'Quantity': total_docs})

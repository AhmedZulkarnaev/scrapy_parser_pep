# Python Documentation Parser

Этот проект представляет собой асинхронный парсер документации Python.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:AhmedZulkarnaev/scrapy_parser_pep.git
    cd scrapy_parser_pep
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Использование

### Аргументы командной строки

- `scrapy crawl pep` (обязательный): Запуск парсера.

## Структура проекта
python-pep-parser/
│
├── pep_parse/
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── pep_spider.py
│
├── results
├── tests
├── requirements.txt
└── README.md


### CSV Output
Файл `pep_2029-01-31T23-55-00.csv`:
number,name,status
1,PEP 1 – PEP Purpose and Guidelines,

Файл `status_summary_2029-01-31_23-55-00.csv`:
Статус,Количество
None,648

## Требования

- Python 3.7+
- Модули, перечисленные в `requirements.txt`


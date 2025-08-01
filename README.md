# wallet_info_by_address

### склонируйте репозиторий
```bazaar
git clone git@github.com:vawy/wallet_info_by_address.git
```

### создайте виртуальное окружение и активируйте его
```bazaar
python -m venv venv
source venv/bin/activate # Linux
source venv/Script/activate # Windows
```

### установите зависимости
```bazaar
pip install -r req.txt
```

### добавьте в app/settings файл .env
```bazaar
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=test_db
```

### поднимите докер контейнер с postgresql
```bazaar
sudo docker run --name my_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=test_db -p 5432:5432 -d postgres
```

### из /wallet_info_by_address запустите тесты
```bazaar
pytest -v
```

### запустить приложение
```bazaar
python app/main.py
```

### swagger
```bazaar
/api/wallet_info/swagger
```

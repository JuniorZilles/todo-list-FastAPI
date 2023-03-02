# todo-list-flask
TODO list to practice python

## run locally
### install dependencies

```bash
pip install -r requirements.txt
```

### set environment variables on .env file
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todo
KEY=xEYR6SNfGzBvqgiTyg-V1Hbr_f0WmNuwZEpqhVu7JgA=
PORT=3000
```

### run command

```bash
python3 main.py
```

## deploy using docker-compose
```bash
docker-compose up -d
```
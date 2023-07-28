#  This is a Docker environment for development purposes with Scripts Python 
## 1. Build and run Docker Compose
```bash
docker-compose build
docker-compose up -d
docker-compose exec app bash
```
## 2. Inside the container

```bash
python main.py
```
# # 3.  Stop container
```bash
docker-compose down
```
# Docker Deployment

## Build Docker Image

```bash
docker build -t avatar-system:latest .
```

## Run Container

```bash
docker run -p 8000:8000 --gpus all avatar-system:latest
```

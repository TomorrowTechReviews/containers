# Containers & Lambdas

Build container

If you CPU architecture the same as the server

```bash
docker build -t chat .
```

If you build on Apple M1 for x86

```bash
docker buildx build --platform linux/amd64 -t chat .
```

If you build for ARM

```bash
docker buildx build --platform linux/arm64 -t chat .
```

## loadtest-py

Container to seed and read chats from Postgres database.

Environment variables

- `DB_URL` - Postgres database URL
- `DB_HOST` -
- `DB_NAME` -
- `DB_PORT` - 5432
- `DB_USER` -
- `DB_PASSWORD` -
- `DB_SECRET` - JSON from Secret Manager with username and password
- `POOL_SIZE` - sqlalchemy pool size (Default: 500)
- `HOST` - FastAPI Server host (Default: 0.0.0.0)
- `PORT` - FastAPI Server post (Default: 80)

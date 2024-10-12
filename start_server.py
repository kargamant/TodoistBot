from src import HOST, PORT, DEBUG
import uvicorn

if __name__ == '__main__':
    uvicorn.run('src.backend:app', host=HOST, port=PORT, reload=DEBUG)

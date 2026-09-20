from fastapi import FastAPI

app = FastAPI(title='Kashmakr Healed Microservice')

@app.get('/health')
def health():
    return {'status': 'healthy', 'service': 'kashmakr_service'}

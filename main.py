from fastapi import FastAPI

app = FastAPI(
    title="VIRTUALIZACIÓN E INTEGRACION DE CONTENIDOS, TRAZABILIDAD Y ORGANIZACION DE REPOSITORIOS DE INTRUCTORE Y APRENDIZES  ",
    description=" aplicativo informático Lque permita administrar, publicar y calificar guías y materiales del SENA en un solo lugar, asegurando que tanto instructores como aprendices gestionen sus portafolios de forma organizada y bajo las mismas reglas.A_martinez,A_castañeda,K_perez,M_barraza" ,
    version="1.0.0"
)

@app.get("/")
async def root():
    """Endpoint raíz que retorna un saludo"""
    return {"message": "¡Hola, Aprendicces e instructores bienvenidos a VICTORIA "}
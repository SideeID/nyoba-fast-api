from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InformasiTambahan(BaseModel):
    hobi: str = "Membaca Buku"
    cita_cita: str = "Menjadi Software Engineer"
    makanan_favorit: str = "Nasi Goreng"

class DataDiri(BaseModel):
    nama: str = "Dimas"
    kuliah: str = "Politeknik Negeri Jember"
    informasi_lain: InformasiTambahan

@app.get("/data-diri")
async def get_data_diri():
    data = DataDiri(
        nama="Dimas",
        kuliah="Politeknik Negeri Jember",
        informasi_lain=InformasiTambahan()
    )
    return data

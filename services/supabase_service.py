from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime
import os
import uuid


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase não configurado corretamente")

supabase = create_client(url, key)

def upload_image(file_bytes, ext, bucket):
    SUPABASE_BUCKET = bucket

    date = datetime.now().strftime("%d%m%Y_%H%M%S")
    name_image = f"{date}_{uuid.uuid4().hex[:8]}.{ext}"
    path_storage = f"public/{name_image}"

    # bytes diretos (sem BytesIO)
    try:
        supabase.storage.from_(SUPABASE_BUCKET).upload(
            path_storage,
            file_bytes,  # <-- aqui vão os bytes crus
            file_options={"content-type": f"image/{ext}"}
        )
    except Exception:
        raise Exception("Erro ao fazer o upload")


    # Gera URL pública
    url_publica = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path_storage)
    
    return url_publica
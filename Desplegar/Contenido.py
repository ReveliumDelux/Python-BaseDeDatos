[Unit]
Description=Gunicorn instance to serve miapp
After=network.target

[Service]
User=tu_usuario
Group=www-data
WorkingDirectory=/ruta/a/tu/proyecto
Environment="PATH=/ruta/a/tu/proyecto/venv/bin"
ExecStart=/ruta/a/tu/proyecto/venv/bin/gunicorn --workers 3 --bind unix:miapp.sock app:app

[Install]
WantedBy=multi-user.target

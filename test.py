import os

# Путь к server.exe
server_path = r'C:\Users\79004\autopusk\autouse\dist\server.exe'  # Укажите правильный путь к вашему server.exe

# Папка автозагрузки
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# Путь к файлу .bat
bat_file_path = os.path.join(startup_folder, r'C:\Users\79004\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start_server.bat')

# Содержимое файла .bat
bat_content = f'@echo off\nstart "" "{server_path}"\n'

# Запись в файл
with open(bat_file_path, 'w') as bat_file:
    bat_file.write(bat_content)

print(f'Файл {bat_file_path} успешно создан!')
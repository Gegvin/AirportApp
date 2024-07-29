
import os
import subprocess
import sys

def create_virtual_env():
    print("Создается виртуальное окружение...")
    subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)

def install_requirements():
    print("Устанавливаются зависимости...")
    pip_executable = os.path.join('venv', 'Scripts', 'pip') if os.name == 'nt' else os.path.join('venv', 'bin', 'pip')
    subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'], check=True)

def run_application():
    print("Запускается приложение...")
    python_executable = os.path.join('venv', 'Scripts', 'python') if os.name == 'nt' else os.path.join('venv', 'bin', 'python')
    subprocess.run([python_executable, 'controller.py'], check=True)

def main():
    try:
        if not os.path.exists('venv'):
            create_virtual_env()
            install_requirements()
        run_application()
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

if __name__ == '__main__':
    main()

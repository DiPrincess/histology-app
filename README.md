# Histology System

Программная система распознавания гистологических изображений с использованием MLP-модели.


## ⚙️ Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/your-username/histology-system.git
   cd histology-system

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate       # Windows: venv\Scripts\activate

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt

4. Убедитесь, что файл `mlp_model.pkl` находится в каталоге src/

5. Запустите классификацию:
    ```bash
    python src/main.py data/sample_slide.jpg


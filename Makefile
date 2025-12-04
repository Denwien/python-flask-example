VENV = venv
PYTHON = $(VENV)/Scripts/python.exe
PIP = $(VENV)/Scripts/pip.exe
UVICORN = $(VENV)/Scripts/uvicorn.exe

start:
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install flask uvicorn asgiref
	$(UVICORN) example_asgi:asgi_app --reload --host 127.0.0.1 --port 8000

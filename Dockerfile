FROM python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /main
COPY . /main

CMD ["python3","main.py"]
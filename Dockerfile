FROM python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ=Australia/Melbourne

WORKDIR /main
COPY . /main

CMD ["python3","main.py"]
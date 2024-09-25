FROM python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y tzdata
ENV TZ=Australia/Melbourne

WORKDIR /main
COPY . /main

CMD ["python3","main.py"]
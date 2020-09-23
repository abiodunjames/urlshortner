FROM python:3.7
WORKDIR /app

# install requirements
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add source code
ADD . /app


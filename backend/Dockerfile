
FROM python:3.10 as builder

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code/api

# 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "3000"]
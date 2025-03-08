FROM python:3.10-slim-bullseye
 
ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8080
 
EXPOSE 8080
 
RUN apt-get update && apt-get install -y git

WORKDIR app/
 
COPY ./requirements.txt /app/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
COPY ./app.py /app/app
COPY ./.streamlit /app/.streamlit
 
CMD ["streamlit", "run", "app/app.py", "--server.port", "8080"]
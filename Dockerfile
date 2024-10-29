FROM python:3.12
RUN apt-get update && apt-get install -y openjdk-17-jdk
EXPOSE 5050
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Run app.py when the container launches
CMD  ["flask", "run", "--host", "0.0.0.0"]
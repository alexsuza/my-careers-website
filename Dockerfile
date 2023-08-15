FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

WORKDIR /app

COPY . .

# Print directory contents for debugging
RUN ls -la

RUN pip install -r requirements.txt
RUN pip3 install -U python-dotenv

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

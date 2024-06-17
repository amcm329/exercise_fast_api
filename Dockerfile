FROM python:3.9

EXPOSE 5000

# ***** Creating sources folders (for counter). *****

RUN mkdir /home/sources

# ***** Instruction related to the installation and configuration of both Python libraries and Fast API. *****

WORKDIR /app

#Left is your host (the path where the docker is) and right is the container's path.

COPY app/requirements.txt /app

RUN apt -qq -y update && apt -qq -y upgrade
	
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY app/main.py /app

#Executing Fast API service. 
CMD ["fastapi", "run", "main.py", "--port", "80"]
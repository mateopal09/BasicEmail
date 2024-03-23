#Based in python 3.8 version.
FROM python:3.10-slim-buster

#Django server showed on the cmd
ENV PYTHONUNBUFFERED 1

#Set the workdir as /backend_code
WORKDIR /backend_code

# Add the libraries for mysqlclient / MariaDB / pakg-config / gcc
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    gcc

#copy dependencies into /backend_code directory
COPY requirements.txt /backend_code/

#install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

#Copy the rest of the files
COPY . /backend_code/

# Give permissions to the start.sh file
RUN chmod +x start.sh

#Expose the port 2000 to use it
EXPOSE 2000

#Command to start the backend
CMD ["./start.sh"]


FROM ubuntu:latest
MAINTAINER Mohd Danish Yusuf "mddanishyusuf@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-bs4
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install requests pillow beautifulsoup4
ENTRYPOINT ["python"]
CMD ["__init__.py"]
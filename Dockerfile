FROM python:latest
LABEL maintainer = "aha392@nyu.edu"

LABEL build_date = "2019-11-14"
RUN apt-get update -y && \
    apt-get upgrade -y

RUN git clone https://github.com/Kurlee/SpellCheckerWebapp.git

WORKDIR /SpellCheckerWebapp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD [ 'gunicorn', 'SpellCheckApp:this_app', '--bind', '0.0.0.0:8080', '--workers', '5' ]


# Commands for testing and building:
# docker build -t spelling-docker:latest .
# docker run -d -p 8080:8080 spelling-docker
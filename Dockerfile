FROM python:3.6-alpine

ENV app_dir_name OpenClass
ENV app_path /opt/$app_dir_name
#installing postgres requirements
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
#Pillow requirements
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
#installing django
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt
#adding the django project
EXPOSE 8000
RUN mkdir -p $app_path
COPY $app_dir_name $app_path
WORKDIR $app_path
VOLUME $app_path

#replace it with something that check when the db start
CMD sleep 10; python manage.py runserver 0.0.0.0:8000

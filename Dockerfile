FROM node:13.12.0-alpine

ENV MONGO_DB_USERNAMES=codewarsfx \
    MONGO_DB-PASSWORD=1234

RUN mkdir -p /home/app

COPY . /home/app


CMD ["node","/home/app/server.js"]



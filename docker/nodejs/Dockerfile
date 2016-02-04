FROM node:argon
MAINTAINER reachlin@gmail.com

ARG APP_ROOT=/var/data/app

RUN apt-get update && apt-get install -y openssh-client
RUN mkdir -p /root/.ssh
COPY id_rsa /root/.ssh
COPY id_rsa.pub /root/.ssh

# Create app directory
RUN mkdir -p $APP_ROOT
WORKDIR $APP_ROOT

# Install app dependencies
COPY package.json $APP_ROOT
RUN npm install

# Bundle app source
COPY . $APP_ROOT

ADD documentation-pages/docs $APP_ROOT

EXPOSE 8080
#CMD [ "npm", "start" ]
ENTRYPOINT tail -f /dev/null

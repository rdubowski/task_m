# pull official base image
FROM node:20-alpine

# set working directory
WORKDIR /usr/src/app

# install app dependencies
COPY package.json .
COPY yarn.lock .
RUN yarn install --production

# copy project
COPY . .
#syntax=docker/dockerfile:1

ARG NODE_VERSION=${NODE_VERSION:-19.0-alpine3.16}
ARG PYTHON_VERSION=${PYTHON_VERSION:-3.10-alpine3.16}

FROM node:${NODE_VERSION} as node
FROM python:${PYTHON_VERSION} as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#
RUN apk update
RUN apk add --no-cache git
RUN pip3 install --upgrade pip
RUN pip3 install wheel

#
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt

#
COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

#
COPY app app
COPY assets assets
COPY migrations migrations
COPY package.json package.json
COPY webpack.config.js webpack.config.js

#
RUN npm install
RUN npm run build

#
#   development
#
FROM builder AS development
CMD ["npm", "start"]

#
#   production
#
FROM python:${PYTHON_VERSION} as production

WORKDIR /usr/src/app

#
RUN adduser -m www
RUN chown -R "www:www" /usr/src/app
ENV PATH="/home/www/.local/bin:${PATH}"

USER www

#
RUN apk update
RUN apk add --no-cache git
RUN pip3 install --upgrade pip
RUN pip3 install wheel

#
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt

#
COPY app app
COPY migrations migrations
COPY --from=builder --chown=www:www /usr/src/app/app/static /usr/src/app/app/static

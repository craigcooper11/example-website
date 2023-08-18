FROM --platform=$BUILDPLATFORM node:20-bullseye-slim as builder

RUN mkdir /project
WORKDIR /project

RUN npm install -g @angular/cli


COPY package.json package-lock.json ./
RUN npm ci
COPY . ./
RUN ng build


# Stage 2: Serve app with nginx server

# Use official nginx image as the base image
FROM nginx as server
COPY --from=builder /project/dist/frontend /usr/share/nginx/html

# Expose port 80
EXPOSE 80

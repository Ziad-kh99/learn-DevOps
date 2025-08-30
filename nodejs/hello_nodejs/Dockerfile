# Build Stage:
FROM node:20-alpine

WORKDIR /app

COPY package*.json .

RUN npm ci --omit=dev

COPY . .

# Runtime Stage:
# node is a non-root user exists in this base-image
USER node           

EXPOSE 3000

CMD ["npm", "start"]
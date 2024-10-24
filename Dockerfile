# Use the official Node.js image as the base
FROM node:20

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json from the frontend folder
COPY frontend/package*.json ./

# Remove any existing package-lock.json and node_modules
RUN rm -rf node_modules package-lock.json

# Install dependencies with a clean npm cache
RUN npm cache clean --force && npm install

# Copy the rest of the frontend folder into the container
COPY frontend/ .

# Expose the port your Nuxt.js app runs on (default is 3000)
EXPOSE 3000

# Command to run your application
CMD ["npm", "run", "dev"]

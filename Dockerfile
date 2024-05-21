# Use a base image with JDK installed
FROM openjdk:11

# Set the working directory in the container
WORKDIR /app

# Copy the compiled Java class file into the container
COPY HelloWorld.class /app

# Command to run the Java program
CMD ["java", "HelloWorld"]

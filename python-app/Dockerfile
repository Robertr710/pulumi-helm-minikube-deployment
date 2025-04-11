# Step 1: Use an official Node.js runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app


COPY app.py /app
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose the port the app will run on
EXPOSE 3000

# Step 7: Define the command to run the app
CMD ["python", "app.py"]


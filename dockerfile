# Use the official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the current directory content into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]

FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy your application code to the container's /app directory
COPY . /app/

# Install dependencies (ensure you have a requirements.txt in your project)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your FastAPI app will run on
EXPOSE 8000

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "src.main:app", "--reload"]

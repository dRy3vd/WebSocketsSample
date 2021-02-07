FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Copy the install script and the requirements.txt  to the /app dir
COPY ./app/scripts/install /app
# Make sure the install script is executable
RUN chmod 755 /app/install
COPY ./app/requirements.txt /app

# Run the install script
RUN ./install

# Copy the app directory to the container app dir
# uvicorn will launch the app (i.e. uvicorn main:app)
COPY ./app /app


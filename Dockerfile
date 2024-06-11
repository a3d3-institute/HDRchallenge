FROM nvidia/cuda:12.3.1-devel-ubuntu22.04
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y hdf5-tools

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install numpy pandas pyarrow matplotlib xgboost scikit-learn nflows lightgbm seaborn iminuit

# Create environment from provided yaml file and activate it
FROM continuumio/miniconda3
COPY /ingested_program/hdr_env.yml /app/ingested_program/hdr_env.yml
RUN conda env create -f /app/ingested_program/hdr_env.yml

# Set the default command to Python3
CMD ["python3"]
FROM continuumio/anaconda3:latest

# Update Anaconda
RUN conda update -n base -c defaults conda

# # Install any other dependenscies
RUN conda install -c conda-forge nano

# Set working directory
WORKDIR /app

# # Expose port (if required)
# EXPOSE 80
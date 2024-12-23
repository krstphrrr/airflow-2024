# airflow ingester 

This project adapts a manually triggered data ingestion pipeline into a more automated one using Apache Airflow.

## Overview

The goal is to automate the data ingestion process, which was previously triggered manually, by leveraging the capabilities of Apache Airflow. 

## Features

- Automated scheduling of data ingestion tasks
- Monitoring and logging of pipeline execution
- Error handling and retry mechanisms

## Getting Started

### Prerequisites

- Python 3.7+
- Apache Airflow 2.10.4

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/airflow-2024.git
    cd airflow-2024
    ```
2. Build the Docker image if using custom Python libraries:
    ```bash
    docker build -t airflow-custom:latest .
    ```

3. Spin up the Airflow Docker stack using Docker Compose:
    ```bash
    docker-compose up -d
    ```

4. Add files into the `plugins/data` directory as the scheduler will automatically detect them.

## Usage

1. Access the Airflow web interface at `http://localhost:8080`.
2. Trigger the data ingestion pipeline manually or wait for the scheduled run.
3. Dockerfile, requirements.txt and ingestion scripts can be found in the plugins dir.

## License

This project is licensed under the MIT License.
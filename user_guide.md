# ETL-Query Script User Guide

## Overview

The ETL-Query script is a command-line interface (CLI) tool that performs Extract, Transform, Load (ETL) operations and executes general queries. This guide provides instructions on how to use the script effectively.

## Startup 
To access the cli command tool you would need to run setup.py by typing:

```bash
python setup.py develop
```
By doing so, we can now run the project as an executable via `etl_query`

## Usage

### Running the Script

To run the ETL-Query script, use the following command:

```bash
etl_query <action> 
```

### Available Actions

The script supports the following actions:

- `extract`: Extract data
- `transform_load`: Transform and load data
- `general_query`: Execute a general query

## Examples

### Extract Data

```bash
etl_query extract
```

This command will extract data.

### Transform and Load Data

```bash
etl_query transform_load
```

This command will transform and load data.

### Execute General Query

```bash
etl_query general_query <query>
```

Replace `<query>` with the specific query you want to execute.

## Notes

- Ensure that you have the required dependencies installed before running the script.
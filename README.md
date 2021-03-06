# ConnectorX: A Unified API Wrapper to Simplify Web DataCollection

## Library Demo

A unified way to get data into a DataFrame from different website.
![](connector_main.gif)

Concurrently fetching multiple pages.
![](connector_concurrency.gif)

Automatic pagination.
![](connector_pagination.gif)

## Reproduce Figure 6 and 7

Start [`notebooks/ConnectorSIGMOD.ipynb`](https://nbviewer.jupyter.org/github/connectorxtechreport/connectorx/blob/master/notebooks/ConnectorSIGMOD.ipynb) to run the experiment
and generate the figures. You might need to register API keys for each website.

## Demonstration of Generator (Sec 4.1)

The following demo is 1m30s long.

![Demo](ConnectorX%20SIGMOD.gif)

# Repo Structure

- connectorx: the connectorx library
- notebooks: containing notebooks for the experments.

# Configuration Files

[https://github.com/connectorxtechreport/Configs](https://github.com/connectorxtechreport/Configs)
stores the configuration files for different websites.

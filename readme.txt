required files to run backtesting

live_runs.csv (copy and paste)
box_mapping.csv (one for each server, only when they change)

liveruns has date and name (for faster results sort by date)
box_mapping has the box_name, folder, and box number

run all the backtests python p.py
throttle the speed, add only 1 test per second

liveruns are then imported into sql
backtest runs are also imported into sql

sql database is accessible via webserver
asp.net application provides dropdowns to construct a query

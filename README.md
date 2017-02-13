Fetch Based Web Communication
==========================

A server-side script to receive pings from clients and forward each ping to anyone who fetches them.

Description
-----------
A client can ping a specific target and another client can fetch that number of pings from the server.

Files
-----
* ping.py - Script to register a ping
* tmpLogger.py - Python program to record the temperature and humidity to the log
* tmpChart.html - Web page with that plot the last 48hrs of temperature and humidity

Usage
-----
Register a ping by visiting `/ping.py?target=*name*` replace *name* with a variable to store the pings
Fetch a ping by visting `/fetch.py?target=*name*` replace *name* with a variable to see pings for that variable.
Currently all pings are storaged/replied with `B` and no pings will be replied with `N`
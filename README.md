# Garmin R10 Data Converter
Small, simple script to convert Garmin R10 data extracts from json files to Excel compatible *.csv files.

## Why
As of now, Garmin does not provide any meaningful way of exporting the data from your Golf (simulator) sessions performed with the R10 launch monitor device. Yet, sometimes it might be beneficial to gain deeper insights by slicing & dicing your data according to your own needs. I therefore searched for a way to obtain my session data and export it into an easy-to-use format (here, .csv which could also be used with Excel etc.). 
Please note, that I show you a way to work around Garmin's limitations when it comes to analyzing your own session data. This is in no way any official or to Garmin related procedure. The script is provided as-is and without any support. Adapt it to your needs if required. 

## Requirements
This script is based on Python 3.8 and requires Pandas. Please refer to the official documentation on how to install the pandas packages on your device.

## How to use the script
1) Go to www.garmin.com -> log into your account -> go to "Account" -> click on "Export Your Data" -> click on "REQUEST DATA EXPORT". The web page responds with a green highlighted "Your request has successfully been submitted.". 
2) Wait for an email to arrive at your email address registered with Garmin (delivery of the mail might vary from a few minutes to - according to garmin - up to 30 days).
3) Follow the instructions from the email to download your compiled data history from Garmin.
4) In the downloaded package Golf related *.json files at the path "$DOWNLOADED_EXTRACTED_ZIPFILE/DI_CONNECT/DI-GOLF/", drop the python script there, switch over to the console and execute the script without any additional parameters. Result is a new *.csv file containing all data from your Golf simulator session (including driving range).
8) Have fun analyzing your data. 

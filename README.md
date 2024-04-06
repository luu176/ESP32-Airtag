# ESP32-Airtag
Clone an existing airtag onto an ESP32

Based on openhaystack

All these scripts werw made by luu176

How to use:
1. First you need to get the airtag data. 

To do this, put your airtag into "lost mode" on your iPhone and then power off your phone 
**OR** 
Have your phone far from your airtag.

Next, compile and write the **airtag_sniffer.ino** script onto your ESP32 (preferably using Arduino IDE).

Open the serial monitor and click the reset button located on your ESP32.

You should be receiving airtag data around you, locate the one with the strongest RSSI

2. Now you need to retreive the advetisement key from the payload data.

Run the **payload-to-key.py** python script.

Enter the values that you found when sniffing the airtag, the mac address and payload.

The script will generate an advertisement key, you will need this later, save it somewhere.


# ESP32-Airtag
Clone an existing airtag onto an ESP32

All the code was written by luu176

Disclaimer: DO NOT TRACK SOMEONE WITHOUT EXPLICIT PERMISSION. DO NOT USE THIS FOR ILLEGAL PURPOSES.

Models supported: ESP32-S3, ESP32-WROOM, ESP32 Dev Kit, ESP32-WROVER, and any other ESP32 that can transceive in BTLE.

How to use:
1. First you need to get the airtag data. 

To do this, put your airtag into "lost mode" on your iPhone and then power off your phone 
**OR** 
Have your phone far from your airtag.

Next, compile and write the **airtag_sniffer.ino** script onto your ESP32 (preferably using Arduino IDE).

Open the serial monitor, then click the reset button located on your ESP32.

You should be receiving airtag data around you, locate the one with the strongest RSSI (the one closest to you) and copy the info

2. Run the **flash_esp32.py** python script.

Enter the values that you found when sniffing the airtag, the mac address and payload.

The script will generate an advertisement key, save it in a file temporarely, then write the firmware with the key on the ESP32.

Open the Find My app on your iPhone and you should now start seing the live location of the ESP32.


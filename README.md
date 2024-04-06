# ESP32-Airtag

**Clone an existing Airtag onto an ESP32**

*All the code was written by luu176*

## DISCLAIMER: DO NOT TRACK SOMEONE WITHOUT EXPLICIT PERMISSION AND DO NOT USE THIS FOR ILLEGAL PURPOSES.

#### **Models supported:** ESP32-S3, ESP32-WROOM, ESP32 Dev Kit, ESP32-WROVER, and any other ESP32 that can transceive in BTLE.


### How to use it
<details>
<summary><b>Step 1. Gathering Airtag data</b></summary>
#### 1. To do this, put your airtag into "lost mode" on your iPhone and then power off your phone **OR** Have your phone far from your airtag.
#### 2. Next, compile and write the **airtag_sniffer.ino** script onto your ESP32 (preferably using Arduino IDE).
#### 3. Open the serial monitor, then click the reset button located on your ESP32.
#### 4. You should be receiving airtag data around you, locate the one with the strongest RSSI (the one closest to you) and copy the info
</details>


<details>
    <summary><b>Step 2. Flashing</b></summary>

#### 1. Run the **flash_esp32.py** python script.
#### 2. Enter the values that you found when sniffing the airtag, the mac address and payload.
#### 3. The script will generate an advertisement key, save it in a file temporarily, then it will write the code using the advertisement key on the ESP32.
#### 4. Open the Find My app on your iPhone and you should now start seing the live location of the ESP32.
</details>




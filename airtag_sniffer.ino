#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>

const char* targetPayloadStart = "1E FF 4C";

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
    void onResult(BLEAdvertisedDevice advertisedDevice) {
      const uint8_t* payload = advertisedDevice.getPayload();
      int payloadLength = advertisedDevice.getPayloadLength();
      if (payloadLength > 2 && payload[0] == 0x1E && payload[1] == 0xFF && payload[2] == 0x4C) {
          Serial.println("airtag found!");
          Serial.printf("RSSI: %d dBm\n", advertisedDevice.getRSSI());
          Serial.print("Payload Data: ");
          for (int i = 0; i < payloadLength; i++) {
            Serial.printf("%02X ", payload[i]);
          }
          Serial.println();
          Serial.printf("MAC Address: %s\n", advertisedDevice.getAddress().toString().c_str());
          Serial.println();
      }
    }
};

void setup() {
  Serial.begin(115200);
  Serial.println("Loading...");
  BLEDevice::init("");
  BLEScan* pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->start(0);
}

void loop() {
  
}

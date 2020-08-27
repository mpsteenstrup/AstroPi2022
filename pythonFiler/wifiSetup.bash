country=DK
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
  ssid="network name"
  psk="password"
  key_mgmt=WPA-PSK
  priority = 10
}

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DK
network={
        ssid="AstroPiHotspot"
        psk="majorTom"
        key_mgmt=WPA-PSK
        priority=10
}

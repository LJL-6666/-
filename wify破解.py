import pywifi
def Check_state():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    print(ifaces.status())
    if ifaces.status() == 4:
        print('电脑已连接无线')
    else:
        def TestConnected(self,findStr):
            profile = pywifi.Profile()
            profile.ssid = self.wifiname
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.ciper = const.CIPHER_TYPE_CCMP
            profile.key = findStr

        self.iface.remove_all_network_profiles()
        tmp_profile = self.iface.add_network_profile(profile)
        self.iface.connect(tmp_profile)
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:
            ifconnect = True
        else:
            ifconnect = False
        self.iface.disconnect()
        time.sleep(1)
        assert self.iface.ststus() in \
               [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
        return ifconnect

        

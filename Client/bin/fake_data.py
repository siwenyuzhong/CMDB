"""
测试数据
    :如果想添加多个测试假数据，可以复制以下多个或修改sn号码，之后执行本脚本
"""

import json
import urllib.request
import urllib.parse
import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from conf import settings


def update_test(data):
    data = {"asset_data": json.dumps(data)}
    # 根据settings中的配置，构造url
    url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
    print('正在将数据发送至： [%s]  ......' % url)

    try:
        data_encode = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
        print("\033[31;1m发送完毕！\033[0m ")
        message = response.read().decode()
        print("返回结果：%s" % message)

    except Exception as e:
        message = "发送失败"
        print("\033[31;1m发送失败，%s\033[0m" % e)


if __name__ == '__main__':
    windows_data1 = {
        "os_type": "Windows",
        "os_release": "7 64bit  6.1.7601 ",
        "os_distribution": "Microsoft",
        "asset_type": "server",
        "cpu_count": 2,
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "cpu_core_count": 8,
        "ram": [
            {
                "slot": "A1",
                "capacity": 8,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "456"
            },

        ],
        "manufacturer": "Intel",
        "model": "P67X-UD3R-B3",
        "wake_up_type": 6,
        "sn": "00426-OEM-8992662-222222",
        "physical_disk_driver": [
            {
                "iface_type": "unknown",
                "slot": 0,
                "sn": "3830414130423230343234362020202020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 128
            },
            {
                "iface_type": "SATA",
                "slot": 1,
                "sn": "383041413042323023234362020102020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 2048
            },

        ],
        "nic": [
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000011] Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter",
                "name": 11,
                "ip_address": "192.168.1.100",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "0A:01:27:00:00:00",
                "model": "[00000013] VirtualBox Host-Only Ethernet Adapter",
                "name": 13,
                "ip_address": "192.168.56.100",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000017] Microsoft Virtual WiFi Miniport Adapter",
                "name": 17,
                "ip_address": "",
                "net_mask": ""
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "Intel Adapter",
                "name": 17,
                "ip_address": "192.1.1.1",
                "net_mask": ""
            },

        ]
    }

    windows_data2 = {
        "os_type": "Windows",
        "os_release": "7 64bit  10.0.0.1 ",
        "os_distribution": "Microsoft",
        "asset_type": "server",
        "cpu_count": 16,
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "cpu_core_count": 8,
        "ram": [
            {
                "slot": "A1",
                "capacity": 8,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "456"
            },

        ],
        "manufacturer": "Intel",
        "model": "P67X-UD3R-B3",
        "wake_up_type": 6,
        "sn": "00426-OEM-8992662-333333",
        "physical_disk_driver": [
            {
                "iface_type": "unknown",
                "slot": 0,
                "sn": "3830414130423230343234362020202020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 128
            },
            {
                "iface_type": "SATA",
                "slot": 1,
                "sn": "383041413042323023234362020102020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 4069
            },

        ],
        "nic": [
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000011] Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter",
                "name": 11,
                "ip_address": "192.168.1.110",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "0A:01:27:00:00:00",
                "model": "[00000013] VirtualBox Host-Only Ethernet Adapter",
                "name": 13,
                "ip_address": "192.168.56.110",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000017] Microsoft Virtual WiFi Miniport Adapter",
                "name": 17,
                "ip_address": "",
                "net_mask": ""
            },
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "Intel Adapter",
                "name": 17,
                "ip_address": "192.1.1.1",
                "net_mask": ""
            },

        ]
    }

    linux_data1 = {
        "asset_type": "server",
        "manufacturer": "innotek GmbH",
        "sn": "00005",
        "model": "VirtualBox",
        "uuid": "E8DE611C-4279-495C-9B58-502B6FCED076",
        "wake_up_type": "Power Switch",
        "os_distribution": "Ubuntu",
        "os_release": "Ubuntu 16.04.3 LTS",
        "os_type": "Linux",
        "cpu_count": "2",
        "cpu_core_count": "4",
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "ram": [
            {
                "slot": "A1",
                "capacity": 4,
            }
        ],
        "ram_size": 3.858997344970703,
        "nic": [],
        "physical_disk_driver": [
            {
                "model": "VBOX HARDDISK",
                "size": "50",
                "sn": "VBeee1ba73-09085302"
            }
        ]
    }

    linux_data2 = {
        "asset_type": "server",
        "manufacturer": "innotek GmbH",
        "sn": "00006",
        "model": "VirtualBox",
        "uuid": "E8DE611C-4279-495C-9B58-502B6FCED076",
        "wake_up_type": "Power Switch",
        "os_distribution": "Centos",
        "os_release": "Centos 16.04.3 LTS",
        "os_type": "Linux",
        "cpu_count": "8",
        "cpu_core_count": "4",
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "ram": [
            {
                "slot": "A1",
                "capacity": 8,
            }
        ],
        "ram_size": 3.858997344970703,
        "nic": [],
        "physical_disk_driver": [
            {
                "model": "VBOX HARDDISK",
                "size": "50",
                "sn": "VBeee1ba73-09085302"
            }
        ]
    }

    linux_data3 = {
        "asset_type": "server",
        "manufacturer": "innotek GmbH",
        "sn": "00007",
        "model": "VirtualBox",
        "uuid": "E8DE611C-4279-495C-9B58-502B6FCED076",
        "wake_up_type": "Power Switch",
        "os_distribution": "Debian",
        "os_release": "Debian 16.04.3 LTS",
        "os_type": "Linux",
        "cpu_count": "6",
        "cpu_core_count": "10",
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "ram": [
            {
                "slot": "A1",
                "capacity": 10,
            }
        ],
        "ram_size": 3.858997344970703,
        "nic": [],
        "physical_disk_driver": [
            {
                "model": "VBOX HARDDISK",
                "size": "50",
                "sn": "VBeee1ba73-09085302"
            }
        ]
    }

    update_test(linux_data1)
    update_test(linux_data2)
    update_test(linux_data3)
    update_test(windows_data1)
    update_test(windows_data2)

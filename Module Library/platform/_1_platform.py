#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Module - platform
#
# Access to underlying platform’s identifying data
# ----------------------------------------------------------------------------------------------------------------

import platform

if __name__ == "__main__":
    print(platform.architecture())  # ('64bit', 'ELF')
    print(platform.machine())       # aarch64
    print(platform.node())          # mindprobe-h96
    print(platform.platform())      # Linux-5.9.0-arm-64-aarch64-with-glibc2.29
    print(platform.processor())     # aarch64
    print(platform.system())        # Linux
    
    print(platform.uname())         
    # uname_result(system='Linux', node='mindprobe-h96', release='5.9.0-arm-64', version='#20.10 SMP PREEMPT Wed Oct 14 12:04:42 MSK 2020', machine='aarch64', processor='aarch64')
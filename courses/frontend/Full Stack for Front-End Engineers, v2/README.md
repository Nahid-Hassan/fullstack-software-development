# Full Stack for Front-End Engineers, v2

## Table Of Contents

- [Full Stack for Front-End Engineers, v2](#full-stack-for-front-end-engineers-v2)
  - [Table Of Contents](#table-of-contents)
    - [Introduction](#introduction)
      - [Full Stack Developer](#full-stack-developer)
      - [Command Line](#command-line)
      - [Shell](#shell)
    - [Understanding the Internet](#understanding-the-internet)
      - [How Does the Internet Work](#how-does-the-internet-work)
      - [IP Addresses & Protocols](#ip-addresses--protocols)
  - [- **IP Address**: A label assigned to an internet connected device.](#--ip-address-a-label-assigned-to-an-internet-connected-device)
      - [Domain Name System](#domain-name-system)

### Introduction

#### Full Stack Developer

Now, a Full Stack Developer is a software expert who's equally proficient in frontend (client-side) development and backend (server-side) development. Full Stack Developers are familiar with each layer of tech stacks that go into the making of a software product.

#### Command Line

Command line is,

- **Fast**.
- **Consistent**.
- Easier to **automate**.

```dash
nahid@infoForest:~$ echo hi
hi
nahid@infoForest:~$ ls
Desktop  Devs  Documents  Downloads  Music  Pictures  Public  Python3Env  snap  Templates  Videos
nahid@infoForest:~$
```

| Command | Description                |
| :-----: | :------------------------- |
|  `cd`   | change directory           |
|  `ls`   | list directory contents    |
|  `pwd`  | print working directory    |
| `mkdir` | make directory             |
| `rmdir` | remove directory           |
|  `cat`  | show file contents         |
|  `man`  | command manual             |
| `less`  | show file contents by page |
|  `rm`   | remove file                |
| `echo`  | repeat input               |

#### Shell

- **Shell**: Command `interpreter` to interface with system, ot simply we can say shell is a **program** that takes `command` as input and showing output.
- **Terminal**: Runs shell application.

```dash
nahid@infoForest:~$ echo $0
bash
```

### Understanding the Internet

#### How Does the Internet Work

A bunch of computers talking to each other. `A series of publicly interconnected devices`. 

- **Private Internet**: Intranet. (Example: Company usages `VPN`)
- **WAN**: Wide Area Network.
- **LAN**: Local Area Network.

#### IP Addresses & Protocols

> Internet run on **trust**.

- **IP**: Internet Protocol
- **IP Address**: A label assigned to an internet connected device.
---
- **IPv4**: `8.8.8.8` # 4.3 billion IP addresses.
- **IPv6**: `2001:4860:4860:8888` # 340 decillion IP addresses.

**Note**: `1` Decillion = `1,000,000,000,000,000,000,000,000,000,000,000`. Total 33 zeros.

--- 

In the `internet` system when two device **talk** to each other they maintain a series of **standard** and this is called `protocol`. Two kinds of protocol:

- **TCP**: Transmission Control Protocol.
- **UDP**: User Datagram Protocol.

**Ping**: Ping is a computer network administration software utility used to `test the reachability of a host on an Internet Protocol (IP) network`.

Ping is useful for **debugging** your site. Ping measures the `round-trip time` for messages sent from the originating host to a destination computer that are echoed back to the source.

Ping operates by sending Internet Control Message Protocol (ICMP) echo request packets to the target host and waiting for an ICMP echo reply. The program reports errors, packet loss, and a statistical summary of the results, typically including the minimum, maximum, the mean round-trip times, and standard deviation of the mean.

```bash
nahid@infoForest:~$ ping twitter.com
PING twitter.com (104.244.42.129) 56(84) bytes of data.
64 bytes from 104.244.42.129: icmp_seq=1 ttl=1 time=82.9 ms
64 bytes from 104.244.42.129: icmp_seq=2 ttl=1 time=82.5 ms
..........................................................
64 bytes from 104.244.42.129: icmp_seq=7 ttl=1 time=129 ms
64 bytes from 104.244.42.129: icmp_seq=8 ttl=1 time=177 ms

--- twitter.com ping statistics ---
8 packets transmitted, 8 received, 0% packet loss, time 7040ms
rtt min/avg/max/mdev = 81.955/100.061/177.063/32.870 ms
```

#### Domain Name System
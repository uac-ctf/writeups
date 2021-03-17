
# NahamCon2021 IoT Itchy & Scratchy SecureIoT Co Writeup

477 points - IoT - 107 Solves - hard

```
See if you have the patience to scratch the itch; patience is key. Mosquitto bites are so annoying! Except, in this case.. you can become an admin.

Connect here: 35.225.10.98:1883 with iot:iot
and here: http://35.225.10.98

```


## Solve

This one was supposed to be a difficult exercise, but in reality it was very simple to solve. Fortunately that's what dynamic score was implemented for.

The text provides too much information pointing towards the solution.

The ```Mosquitto``` word points towards the ```mosquitto``` ```MQTT``` broker, and the port ```1883``` to which we are supposed to connect, also corroborates that information.

The URL pointed towards a webpage asking for a login, password and One Time Password as a 2FA.

To check what was going on on the ```MQTT``` broker we connected using ```mosquitto_sub``` and subscribed to all topics (```#```)

```$ mosquitto_sub -h 35.225.10.98 -u iot -p iot -t "#"" -d ```

The result was a series of messages as present in the ```mqtt.log``` file.

From the dump we see several interesting topics:
```
Office/SecureCo/device/admin/login/u
Office/SecureCo/device/admin/login/p
Office/SecureCo/webcam/feed/part1
Office/SecureCo/webcam/feed/part2
```

The ```login/u``` is: ```YWRtaW5pc3RyYXRvcg==``` and seems to be the login.

```
$ echo YWRtaW5pc3RyYXRvcg== |base64 -d
administrator
```

The ```login/p``` is: ```U2VDVVJlUEA1NVcwckQx``` and seems to be the password.

```
$ echo U2VDVVJlUEA1NVcwckQx |base64 -d
SeCUReP@55W0rD1
```

The ```part1``` and ```part2``` contain large base64 blobs and vary along time, pointing to a two part blob related to the OTP. After reconstructing the messages we get an image with the OTP.
Input all information to the webpage and the flag is presented.

![otp](https://github.com/uac-ctf/nahamcon2021/raw/main/IoT%20Itchy%20%26%20Scratchy%20SecureIoT%20Co/otp.jpg)

The ```solve.py``` script automates this process.


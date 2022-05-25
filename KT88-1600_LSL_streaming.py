"""
Created on Dec 02, 2021

@author: Aleksandar Miladinovic email: alex.miladinovich@gmail.com

Python script used to decode serial data stream of Contec KT88-1800/1600 EEG amplifier and stream it to the local network via LSL

"""
import time
import serial
from pylsl import StreamInfo, StreamOutlet
import sys
import serial.tools.list_ports

ser=serial.Serial()
if len(sys.argv) > 1:
    COM_PORT=sys.argv[1:]
else:
    # port not given, using default
    if sys.platform == 'win32':
        COM_PORT='COM20'
    else:
        COM_PORT='/dev/cu.usbserial-1420'

ser = serial.Serial(port=COM_PORT,
                    baudrate=921600, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,xonxoff=False,rtscts=False,dsrdtr=False)




def start_acquisition():
    packet = bytearray()
    packet.append(0x90)
    packet.append(0x01)
    return ser.write(packet)


def stop_acquisition():
    packet = bytearray()
    packet.append(0x90)
    packet.append(0x02)
    return ser.write(packet)


def send_default_configuration_to_EEG():
    # stop acquisition
    packet = bytearray()
    packet.append(0x90)
    packet.append(0x02)
    ser.write(packet)
    time.sleep(0.3)

    packet = bytearray()
    packet.append(0x80)
    packet.append(0x00)
    ser.write(packet)
    time.sleep(0.3)

    packet = bytearray()
    packet.append(0x81)
    packet.append(0x00)
    ser.write(packet)
    time.sleep(0.3)

    # set BN as REF (91 + 01 - AA, 02 - A1, 03 - A2, 04 - AVG, 05 - Cz, 06 - BN)
    packet = bytearray()
    packet.append(0x91)
    packet.append(0x01)
    ser.write(packet)
    time.sleep(0.3)

    # Enable HW filter 0.03Hz to 40Hz see https://patents.google.com/patent/CN103505200A/en
    packet = bytearray()
    packet.append(0x90)
    packet.append(0x03) #04 to disable it
    ser.write(packet)
    time.sleep(0.3)

    # Disable impedance measurement
    packet = bytearray()
    packet.append(0x90)
    packet.append(0x06)
    ser.write(packet)
    time.sleep(0.3)

    ser.flushInput()
    ser.flushOutput()

    return 1


def main():
    print("Send default")
    send_default_configuration_to_EEG();

    print("Start acquisition")
    start_acquisition()

    print("Setup LSL")
    stream_info_KT88 = StreamInfo('KT88', 'EEG', 18, 100, 'float32', 'kt_88_1800_EEG')

    # add channel labels
    channels = stream_info_KT88.desc().append_child("channels")
    ch_labels = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6','ECG1','ECG2']

    for c in ch_labels:
        ch=channels.append_child("channel")
        ch.append_child_value("label", c)

    # next make an outlet
    kt88_outlet = StreamOutlet(stream_info_KT88)


    ser.flushInput()
    ser.flushOutput()

    # init channels
    channel = []
    for ch in range(0, 18):
        channel.append(0)


    while 1:
        # find marker
        ser.read_until(expected=b"\xA0")

        # extract 45byte chunk
        chunk = bytearray(ser.read(31))

        ch=0
        for bt in range(4,31,3): #
            channel[ch]=(chunk[bt] & 0b01110000)<<5 | (chunk[bt+1] & 0b01111111)

            if bt==29:
                break
            channel[ch+1]=(chunk[bt] & 0b00001111)<<8 | (chunk[bt+2] & 0b01111111)
            ch=ch+2


        channel[0] = (channel[0]) | (chunk[0] & 0b00000001) << 11 | (chunk[0] & 0b00000010) << 6
        channel[1] = (channel[1]) | (chunk[0] & 0b00000100) << 5
        channel[2] = (channel[2]) | (chunk[0] & 0b00001000) << 8 | (chunk[1] & 0b00000001) << 7
        channel[3] = (channel[3]) | (chunk[1] & 0b00000010) << 6
        channel[4] = (channel[4]) | (chunk[1] & 0b00001000) << 4 | (chunk[1] & 0b00000100) << 9
        channel[5] = (channel[5]) | (chunk[1] & 0b00010000) << 3
        channel[6] = (channel[6]) | (chunk[1] & 0b00100000) << 6 | (chunk[1] & 0b01000000) << 1
        channel[7] = (channel[7]) | (chunk[2] & 0b00000001) << 7
        channel[8] = (channel[8]) | (chunk[2] & 0b00000010) << 10 | (chunk[2] & 0b00000100) << 5
        channel[9] = (channel[9]) | (chunk[2] & 0b00001000) << 4
        channel[10] = (channel[10]) | (chunk[2] & 0b00010000) << 7 | (chunk[2] & 0b00100000) << 2
        channel[11] = (channel[11]) | (chunk[2] & 0b01000000) << 1
        channel[12] = (channel[12]) | (chunk[3] & 0b00000001) << 11 | (chunk[3] & 0b00000010) << 6
        channel[13] = (channel[13]) | (chunk[3] & 0b00000100) << 5
        channel[14] = (channel[14]) | (chunk[3] & 0b00001000) << 8 | (chunk[3] & 0b00010000) << 3
        channel[15] = (channel[15]) | (chunk[3] & 0b00100000) << 2
        channel[16] = (channel[16]) | (chunk[3] & 0b01000000) << 5 | (chunk[4] & 0b00000001) << 7
        channel[17] = (channel[17]) | (chunk[4] & 0b00000010) << 6


        for ch in range(0, 18):
            channel[ch] = float(channel[ch]-2048)/10
        if kt88_outlet.have_consumers():
            #print(channel[ch])
            kt88_outlet.push_sample(channel)


if __name__ == '__main__':
    main()

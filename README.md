# Contec_KT88-2400_LSL
Script used to decode serial data stream of Contec KT88-2400 EEG amplifier and to stream it to the local network via LSL

Requirements

Python 3.(9)
pylsl
pyserial

to install depdendencies run pip3 install pylsl pyserial

Once downloaded KT88-2400_LSL_streaming.py run the script with python3 KT88-2400_LSL_streaming.py COM_PORT or edit the script to set default 


Communication protocol and commands

Acquisition and filter control (commands in hex format)
90 01 Start Acquisition
90 02 Stop acquisition
90 03 Enable HW filter 0.5-35Hz
90 04 Disable HW filter
90 05 Start impedance measurement
90 06 Disable impedance measurement

Setting physical reference electrode
91 01 AA reference (left hemisphere referenced to the left ear lobe, right to the right earlobe)
91 02 A1 reference (all electrodes referenced to the A1)
91 03 A2 reference
91 04 AVG (average reference)
91 05 Cz reference
91 06 BN (balanced noncephalic reference)

Montage setup
92 0X (9 defined montages X=1,...,9, the montage can be explored by going to System configuration -> montage ways). Changes of default montage always follow the command 91 04 (avg reference).


Uknown commands
80 00
81 00

Example of the default system settings sequence sent by the provided EEG software.

90 02 //stop acquisition
80 00 //?
81 00 //?
91 01 //set AA reference
90 09 //?
90 03 //Enable HW filter
90 06 //Disable impedance reading
90 01 //Start data acquisition
... DATA STREAM ...
90 02 //Stop acquisition

Data Stream

Baud rate 921600 (has to be that one)
Data sampling rate 200Hz
Encoding bits 12
Number of channels 26

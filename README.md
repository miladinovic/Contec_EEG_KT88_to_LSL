# Contec_KT88-2400_LSL
Script used to decode serial data stream of Contec KT88-2400 EEG amplifier and to stream it to the local network via LSL

**Requirements**\cr
\cr
Python 3.(9)\cr
pylsl\cr
pyserial\cr
\cr
to install depdendencies `run pip3 install pylsl pyserial`\cr
\cr
Once downloaded KT88-2400_LSL_streaming.py run the script with \cr
`python3 KT88-2400_LSL_streaming.py COM_PORT`or edit the script to set default 
\cr\cr

**Communication protocol and commands\cr
**
\cr
**Acquisition and filter control (commands in hex format)**\cr
90 01 Start Acquisition\cr
90 02 Stop acquisition\cr
90 03 Enable HW filter 0.5-35Hz\cr
90 04 Disable HW filter\cr
90 05 Start impedance measurement\cr
90 06 Disable impedance measurement\cr
\cr
**Setting physical reference electrode\cr
**
91 01 AA reference (left hemisphere referenced to the left ear lobe, right to the right earlobe)\cr
91 02 A1 reference (all electrodes referenced to the A1)\cr
91 03 A2 reference\cr
91 04 AVG (average reference)\cr
91 05 Cz reference\cr
91 06 BN (balanced noncephalic reference)\cr
\cr
**Montage setup\cr
**
92 0X (9 defined montages X=1,...,9, the montage can be explored by going to System configuration -> montage ways). Changes of default montage always follow the command 91 04 (avg reference).\cr
\cr\cr

**Uknown commands
**\cr
80 00\cr
81 00\cr
\cr
Example of the default system settings sequence sent by the provided EEG software.\cr
\cr
*90 02 //stop acquisition\cr
80 00 //?\cr
81 00 //?\cr
91 06 //set BN reference\cr
90 09 //?\cr
90 03 //Enable HW filter\cr
90 06 //Disable impedance reading\cr
90 01 //Start data acquisition\cr
... DATA STREAM ...\cr
90 02 //Stop acquisition*\cr
\cr
**Data 
**\cr
Baud rate 921600\cr
Data sampling rate 200Hz\cr
Encoding bits 12\cr
Number of channels 26\cr



 

# Contec_KT88-2400_LSL
Script used to decode serial data stream of Contec KT88-2400 EEG amplifier and to stream it to the local network via LSL

**Requirements**<br />
<br />
Python 3.(9)<br />
pylsl<br />
pyserial<br />
<br />
to install depdendencies `run pip3 install pylsl pyserial`<br />
<br />
Once downloaded KT88-2400_LSL_streaming.py run the script with <br />
`python3 KT88-2400_LSL_streaming.py COM_PORT`or edit the script to set default 
<br /><br />

**Communication protocol and commands**<br />

<br />
**Acquisition and filter control (commands in hex format)**<br />
90 01 Start Acquisition<br />
90 02 Stop acquisition<br />
90 03 Enable HW filter 0.5-35Hz<br />
90 04 Disable HW filter<br />
90 05 Start impedance measurement<br />
90 06 Disable impedance measurement<br />
<br />
**Setting physical reference electrode**<br />

91 01 AA reference (left hemisphere referenced to the left ear lobe, right to the right earlobe)<br />
91 02 A1 reference (all electrodes referenced to the A1)<br />
91 03 A2 reference<br />
91 04 AVG (average reference)<br />
91 05 Cz reference<br />
91 06 BN (balanced noncephalic reference)<br />
<br />
**Montage setup**<br />

92 0X (9 defined montages X=1,...,9, the montage can be explored by going to System configuration -> montage ways). Changes of default montage always follow the command 91 04 (avg reference).<br />
<br /><br />

**Uknown commands**<br />
80 00<br />
81 00<br />
<br />
Example of the default system settings sequence sent by the provided EEG software.<br />
<br />
*90 02 //stop acquisition<br />
80 00 //?<br />
81 00 //?<br />
91 06 //set BN reference<br />
90 09 //?<br />
90 03 //Enable HW filter<br />
90 06 //Disable impedance reading<br />
90 01 //Start data acquisition<br />
... DATA STREAM ...<br />
90 02 //Stop acquisition*<br />
<br />
**Data **<br />
Baud rate 921600<br />
Data sampling rate 200Hz<br />
Encoding bits 12<br />
Number of channels 26<br />



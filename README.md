 

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
Once downloaded KT88-2400_LSL_streaming.py set the desired port an run the script with <br />
`python3 KT88-2400_LSL_streaming.py COM_PORT` the script
<br /><br />

The ready binaries for Windows x64 are available https://github.com/miladinovic/Contec_KT88-2400_LSL/releases

For Windows it is not necassery to install addional libraries, just make sure that you have changed the port to COM20, then run the EEG24 program to verify if the device still works.

To change port go to Control Panel -> Device Manager -> Ports (COM&LPT) -> Right-click to the com to the UART to USB bridge and select "Properties" -> Port settings tab -> button Advance and change to port COM20 click OK and then run te EEG24.

Choose the desired settings HW filter 0.3-35Hz ON or OFF, as well as, reference electrode (AA=A1+A2, AV=Average, BN=Balanced-non cephalic).

26 channels with state of 200Hz will be streamed to the local network via LSL protocol with the following order ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Pz', 'Cz', 'Pg1', 'Pg2', 'EOGR', 'EOGL', 'EMG', 'BR', 'ECG']



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
**Data**<br />
Baud rate 921600<br />
Data sampling rate 200Hz<br />
Encoding bits 12<br />
Number of channels 26<br />

Protocol: https://github.com/miladinovic/Contec_KT88-2400_LSL/blob/main/serial_decoding_protocol.txt

**Disclamer**
The provided software is made for educational and research purposes only. It is not by any means a substitute for provided software by manufacturer.

**Support my work**
If you find this script useful for your experiments, please cite my works. Thank you!

Miladinović, Aleksandar, et al. "Effect of power feature covariance shift on BCI spatial-filtering techniques: A comparative study." Computer Methods and Programs in Biomedicine 198 (2021): 105808.

Miladinović, Aleksandar, et al. "Performance of EEG Motor-Imagery based spatial filtering methods: A BCI study on Stroke patients." Procedia Computer Science 176 (2020): 2840-2848.

Miladinović, Aleksandar, et al. "Evaluation of Motor Imagery-Based BCI methods in neurorehabilitation of Parkinson’s Disease patients." 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2020.

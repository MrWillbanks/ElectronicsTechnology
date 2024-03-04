<img src="https://github.com/MrWillbanks/ElectronicsTechnology/blob/main/StandardOperatingProcedures/Photos/NT_Logo.png" width="60"/>
Norwich Technical High School - Electronics Technology    	   Date Updated:  3/4/2024  
7 Mahan Drive  
Norwich, CT 06360  
  
  
TITLE:  Testing an Analog/Digital Trainer 
  
APPROVALS:   
	Author: Gavin Croy & Cristien Walworth | Date: March 4, 2024  	  
	Review:  	 | 	Date:    
  
1.	Revision History:

|Initials    |	REV  |	DATE |   SUMMARY OF CHANGES |
|-|-|-|--|
|Gavin Croy & Cristien Walworth | 	A  |	1/3/2024   |	Initial                                                  |
|Cristien Walworth | 	B  |	2/8/2024  |Added Expected Results, Fixed Grammar, and Fixed Image Rotation	 |
|Gavin Croy & Cristien Walworth |  C  | 3/4/2024    |Uploaded document as an .md file|                                	
  
2.	Purpose:  
2.1. To test all the basic functions of an analog/digital breadboard trainer to ensure proper functionality.  
  
3.	Safety:  
3.1. Don’t open up the trainer while power is on.                               
3.2. Don’t remove anything built on to the breadboard while power is on. 
  
5.	Materials: 
-	Analog/Digital breadboard trainer 
-	Breadboard
-	22 AWG wire
-	Digital Multimeter (DMM)
-	Digital Oscilloscope 
-	Access to “Breadboard Trainer’s List” Google Sheet

                              
5.	Procedure:                           

|Step  |	Procedure  |	Picture |
|------|-------------|----------|
|1.| Testing DC Voltage: Set DMM to DC voltage. Insert positive lead on DMM to **+5V** and insert negative lead on DMM to **GND**. DMM should read near 5V. Record results from DMM and upload them to *“Breadboard Trainer’s List.”* |<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step1.png"/> |
|2.| Testing DC Voltage: Insert positive lead on DMM to adjustable **+V** and insert negative lead on DMM to **GND**. Use the **+V Adjustment knob** to test for proper functionality. DMM should have a varying voltage as you turn the knob. Record results from DMM and upload them to *“Breadboard Trainer’s List.”* Repeat this for adjustable **-V** and use the **-V Adjustment knob.**|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step2.png"/>  |
|3.| Testing AC Voltage: Set DMM to AC voltage. Insert positive lead on DMM to **RED 12.6VAC** and insert negative lead on DMM to **BLUE 12.6VAC**. DMM should read near 12.6VAC. Record results from DMM and upload them to *“Breadboard Trainer’s List.”* Then, move the positive lead to **YELLOW CT 12.6VAC** and keep negative lead at **BLUE 12.6VAC.** DMM should read 6.3VAC. Record results from DMM and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step3.png"/>  |
|4.| Testing PushButtons: Set DMM to continuity mode. Insert 22 AWG wire into **NC**. Connect DMM positive lead on DMM to **NC** wire and insert negative lead on DMM to **GND**. Push the button and record results from DMM and upload them to “Breadboard Trainer’s List.” DMM should beep confirming continuity. Repeat this for all pushbuttons.|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step4.png"/>  |
|5.| Testing POTs (Potentiometers): Set DMM to ohmmeter. Connect a 22 AWG wire into the outside rail (left or right) and one into the wiper rail (middle). Connect DMM positive lead to outside rail wire and DMM negative lead to wiper rail wire. Turn the adjustable corresponding knob. DMM resistance number should change as you turn the knob. Record results from DMM and upload them to *“Breadboard Trainer’s List.”* Repeat this for all POTs.|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step5.png"/>  |
|6.| Testing Function Generator: Use an oscilloscope. Insert a 22 AWG wire into the generator and one 22 AWG wire into **GND**. Connect the probe to both wires. Turn all knobs and check for functionality on the oscilloscope. Make sure each output wave is properly displayed and all of its functions. Record results from oscilloscope and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step6.png"/>  |
|7.| Testing Logic Switches. Set DMM to DC Voltage. Insert 22 AWG wire into slot **1** on the logic switches breadboard. Place positive lead on wire and insert negative lead into **GND**. DMM should read near 5V. Record results from DMM and upload them to *“Breadboard Trainer’s List.”* Repeat for all switches.|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step7.png"/>  |
|8.| Testing Logic Monitor: Insert 22 AWG wire into **+5V** and insert it into any slot on the breadboard. Check if each light turns on for HIGH. Record results and upload them to *“Breadboard Trainer’s List.”* Repeat the same with **GND** and LOW.|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step8.png"/>  |
|9.| Testing Logic Probe: Insert 22 AWG wire into **+5V** and place it in VCC on the **LOGIC PROBE**. Connect a 22 AWG wire from a logic switch to the input of the Logic Probe and check that all of the LEDs light up. Record results and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step9.png"/>  |
|10.| Testing BCD 7-Segment Display: Insert 22 AWG wire into any logic switch. And connect it to any row on the breadboard of the 7-segment display. Check that each display displays the numbers 0-9. Record results and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step10.png"/>  |
|11.| Testing SPDT Switches: Set DMM to continuity. Insert 22 AWG wire into the left (or right) rail and middle rail. Check for continuity while flipping the switch. DMM should beep confirming continuity. Record results on DMM and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step11.png"/>  |
|12.| Testing Speaker: Insert 22 AWG wire into the frequency generator and one into the left side of the speaker. Insert other wire from the right side of the speaker to **GND**. Turn the frequency knob and check for a changing sound from the speaker.  Record results and upload them to *“Breadboard Trainer’s List.”*|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step12.png"/>  |
|13.| Testing BNC: Set DMM to continuity. Insert 22 AWG wire into top of the breadboard of BNC. Connect the positive lead of DMM to the center pin of the BNC input and connect the negative lead to the end of the wire.   Record results on DMM and upload them to “Breadboard Trainer’s List.” Then, move the wire to the bottom of the breadboard. Connect the positive lead of DMM to outside of the BNC input and connect the negative lead to the end of the wire. DMM should beep confirming continuity. Record results on DMM and upload them to “Breadboard Trainer’s List.”|<img src="https://raw.githubusercontent.com/Cristien-Walworth/TrainerFunctionalityPICS/main/step13.png"/> |





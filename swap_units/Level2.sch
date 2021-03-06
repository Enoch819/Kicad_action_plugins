EESchema Schematic File Version 4
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Operational:LM324 U1
U 4 1 5B2A1811
P 3900 3800
F 0 "U1" H 3900 4000 50  0000 L CNN
F 1 "LM324" H 3900 3600 50  0000 L CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 3850 3900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2902-n.pdf" H 3950 4000 50  0001 C CNN
	4    3900 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R6
U 1 1 5B2A4F5C
P 3150 3350
F 0 "R6" H 3250 3400 50  0000 C CNN
F 1 "R" H 3250 3300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 3080 3350 50  0001 C CNN
F 3 "~" H 3150 3350 50  0001 C CNN
	1    3150 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5B2A4F63
P 3150 4250
F 0 "R7" H 3250 4300 50  0000 C CNN
F 1 "R" H 3250 4200 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 3080 4250 50  0001 C CNN
F 3 "~" H 3150 4250 50  0001 C CNN
	1    3150 4250
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR09
U 1 1 5B2A4F6A
P 3150 3100
F 0 "#PWR09" H 3150 2950 50  0001 C CNN
F 1 "+5V" H 3150 3240 50  0000 C CNN
F 2 "" H 3150 3100 50  0001 C CNN
F 3 "" H 3150 3100 50  0001 C CNN
	1    3150 3100
	1    0    0    -1  
$EndComp
$Comp
L Passives:GND #PWR010
U 1 1 5B2A4F70
P 3150 4500
F 0 "#PWR010" H 3150 4350 50  0001 C CNN
F 1 "GND" H 3300 4450 50  0001 C CNN
F 2 "" H 3150 4500 50  0001 C CNN
F 3 "" H 3150 4500 50  0001 C CNN
	1    3150 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3150 4500 3150 4400
Wire Wire Line
	3150 4100 3150 3700
Wire Wire Line
	3150 3700 3600 3700
Connection ~ 3150 3700
Wire Wire Line
	3150 3100 3150 3200
Wire Wire Line
	3150 3500 3150 3700
Wire Wire Line
	3600 3900 3500 3900
Wire Wire Line
	3500 3900 3500 4150
Wire Wire Line
	3500 4150 4350 4150
Wire Wire Line
	4350 4150 4350 3800
Wire Wire Line
	4350 3800 4200 3800
Text HLabel 4350 3800 2    50   Output ~ 0
out_level_2
$EndSCHEMATC

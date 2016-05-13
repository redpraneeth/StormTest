############## Script Owned by:################################################
#  ______                          _   _                                      #
#  | ___ \                        | | | |                                     #
#  | |_/ / __ __ _ _ __   ___  ___| |_| |__                                   #
#  |  __/ '__/ _` | '_ \ / _ \/ _ \ __| '_ \                                  #
#  | |  | | | (_| | | | |  __/  __/ |_| | | |                                 #
#  \_|  |_|  \__,_|_| |_|\___|\___|\__|_| |_|                                 #
#                                                                             #
# Description : All Common functions which can be Re-Use are defined here     #              .     #
###############################################################################

import stormtest.ClientAPI as StormTest
#import xlrd
#import xlwt
#############################
#####	Global Variables
#############################
Server1 = "storm1" # StormTest server name/IP address 192.168.30.83
Server2 = "storm2" # StormTest server name/IP address 192.168.30.140
User = "Praneeth_Reddy"          # Helps other users identify who has reserved the slot
logParam1 = [115200, 8, "none", 1, "none", "TestName"]
#logParam2 = [9600, 8, "none", 1, "none", "TestName_log2"]
TotalTestCases = 0
TotalPassTestCases = 0
TotalFailTestCases = 0
TotalNonExecutedTestCases = 0

#########################################
#####	User remote control file	#####
#########################################
#####	Use default remote	#############
#########################################
RC_KeySet		=		"default"

#####################################################################################
#####	RCU Keys	######
#####	Format <DEFINE_NAME = String provided during custom remote training>
#####################################################################################
RC_Fav			=		"Fav"
RC_Power		=		"Power"
RC_Active		=		"Active"
RC_WebApps		=		"WebApps"
RC_Vod			=		"Vod"
RC_Mosaic		=		"Mosaic"
RC_Exit			=		"Exit"
RC_Guide		=		"TV_Guide"
RC_Help			=		"Help"
RC_Up			=		"Up"
RC_Left			=		"Left"
RC_Right		=		"Right"
RC_Down			=		"Down"
RC_Ok			=		"Ok"
RC_Backup		=		"Backup"
RC_Mute			=		"Mute"
RC_Menu			=		"Menu"
RC_VolPlus		=		"Vol+"
RC_VolMinus		=		"Vol-"
RC_ChnPlus		=		"Channel+"
RC_ChnMinus		=		"Channel-"
RC_Info			=		"Info"
RC_Record		=		"Record"
RC_Live			=		"Live"
RC_Rew			=		"Rew"	
RC_Play_Pause	=		"Play/Pause"
RC_Stop			=		"Stop"
RC_FFwd			=		"FFwd"
RC_Red			=		"Red"
RC_Green		=		"Green"
RC_Yellow		=		"Yellow"
RC_Blue			=		"Blue"
RC_1			=		"1"
RC_2			=		"2"
RC_3			=		"3"
RC_4			=		"4"
RC_5			=		"5"
RC_6			=		"6"
RC_7			=		"7"
RC_8			=		"8"
RC_9			=		"9"
RC_Star			=		"*"
RC_0			=		"0"
RC_Hash			=		"#"
RC_Swap			=		"Swap"
RC_Text			=		"Text"
RC_Select		=		"Select"
RC_Oem4			=		"Oem4"
RC_Oem3			=		"Oem3"
RC_Oem2			=		"Oem2"
RC_Oem1			=		"Oem1"
RC_Pause		=		"Pause"
RC_Play			=		"Play"

######################################################
#####	Function Name			:	RebootSTB
#####	Function Description	:	To reboot the STB
######################################################
def VDL_RebootSTB( ):
    StormTest.PowerOffSTB(5)
    StormTest.PowerOnSTB(10)
    StormTest.WaitSec(50)

def VDL_Cisco_Active( ):
    StormTest.PressButton(RC_Active)



#########################################
#####	Resorces	#############
#########################################
Img_Assistance_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/ASSISTANCE/Img_Assistance_Main')
Img_English_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/ENGLISH/Img_English_Main')
Img_Games_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/GAMES/Img_Games_Main')
Img_Kids_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/KIDS/Img_Kids_Main')
Img_StateActive_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/STATEACTIVE/Img_StateActive_Main')
Img_Active_Main = StormTest.FindNamedImage('/ACTIVE_SERVICES/Img_Active_Main')
Img_Loading = StormTest.FindNamedImage('/ACTIVE_SERVICES/Img_Loading')

Region_Assistance = StormTest.FindNamedRegion('/ACTIVE_SERVICES/ASSISTANCE/Region_Assistance')
Region_English = StormTest.FindNamedRegion('/ACTIVE_SERVICES/ENGLISH/Region_English')
Region_Games = StormTest.FindNamedRegion('/ACTIVE_SERVICES/GAMES/Region_Games')
Region_Kids = StormTest.FindNamedRegion('/ACTIVE_SERVICES/KIDS/Region_Kids')
Region_StateActive = StormTest.FindNamedRegion('/ACTIVE_SERVICES/STATEACTIVE/Region_StateActive')
Region_Active = StormTest.FindNamedRegion('/ACTIVE_SERVICES/Region_Active')
Region_Loading = StormTest.FindNamedRegion('/ACTIVE_SERVICES/Region_Loading')
Region_Video = StormTest.FindNamedRegion('/Region_Video')

Sdo_AV = '/SDO_AV'
#Region_English		=	1400,20,450,150
#Region_Games		=	1400,20,450,150
#Region_Kids		=	1400,20,450,150
#Region_StateActive	=	930,20,650,150
#Region_Assistance	= 	160,70,300,80
#Region_Loading		= 	700,300,500,500
#Region_Active         =   1500,10,400,200

###################################################
# Function Name                   : InvokeMenu
# Function Description            : To invoke the Menu
###################################################
def VDL_InvokeMenu( ):
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)    
    StormTest.PressButton(RC_Menu)
    StormTest.WaitSec(5)


######################################################################
# Function Name                   : InvokeWebApps
# Function Description            : To invoke WebApps
######################################################################
def VDL_InvokeWebApps( ):
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)      
    StormTest.PressButton(RC_Oem2)
    StormTest.WaitSec(5)	
    
#####################################################
# Function Name					: TuneLCN
# Function Description			: To tune any Service manually
#####################################################
def VDL_TuneLCN(LCN):
    StormTest.PressButton(RC_Exit) 
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressDigits(LCN)
    StormTest.WaitSec(7)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Info)
    StormTest.WaitSec(5)
    print"Reading OCR Slot" 
    Channel_No = StormTest.OCRSlot([220, 725, 70, 50])
    Channel_No = Channel_No[4][0][1].strip()
    print Channel_No 
    if Channel_No == LCN:
        print "Tuned to LCN: "+ Channel_No
        return Channel_No
    else:
        print "Tuned LCN not Matching with OCR"
        return StormTest.TM.FAIL
    return Channel_No
  

#############################################
# Function Name                   : SWAP
# Function Description            : Channel zap/swap to Previous channel
#############################################
def VDL_SWAP():
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Swap)
    StormTest.WaitSec(5)
    StormTest.PressButton(RC_Exit)
    StormTest.WaitSec(3)
    StormTest.PressButton(RC_Info)
    StormTest.WaitSec(3)
    Channel_No=StormTest.OCRSlot([220, 725, 70, 50]) #Channel_No is captured from "Info Banner"  
    Channel_No=Channel_No[4][0][1].strip()
    Channel_No=StormTest.OCRSlot()
    return Channel_No
   
   
######################################################################
#	CO-ORDINATES
######################################################################
Info_LCN                     =       220, 725, 70, 50
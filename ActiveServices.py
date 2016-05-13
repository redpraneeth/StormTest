######################################################################
# File Name     :     Main.py
# Author     :     Praneeth Reddy
# File Description     :     This file contains the test case related to WebApps Main Page .
######################################################################

######################################################################
#                                                       FILES INCLUDED                                                           #
######################################################################
import stormtest.ClientAPI as StormTest
import Common
import traceback
import time


#TotalExecutions = int(input("Enter No.of Iterations you would like to repat..?: "))
TotalExecutions = 10
PassExecutions = 0
FailExecutions = 0

EnglishTup =[]
GamesTup =[]
KidsTup = []
StateActiveTup = []
AssistanceTup =[]

########################################################################################
# TestCase                    : 1
# TestCase Description        : Test whether App is able to launch ENGLISH
#########################################################################################

def English():
    English_Launched = TotalExecutions
    English_PASS = PassExecutions
    English_Fail = FailExecutions
    English_NonExecuted = 0
    StormTest.BeginTestStep("ACTIVE_English")
    for i in range(English_Launched):
        k = i+1
        step_name = "ITTERATION %d:::" %k
        StormTest.BeginTestStep(step_name)
        Common.VDL_RebootSTB()
        Common.VDL_Cisco_Active()
        StormTest.WaitSec(10)
        ACT_MAIN = StormTest.WaitImageMatch(Common.Img_Active_Main,percent=70,includedAreas=Common.Region_Active,timeToWait=20)        
        if ACT_MAIN[0][1]:
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Ok)
            Start_Time = time.clock()            
            English_Main = StormTest.WaitImageMatch(Common.Img_English_Main, percent=90, includedAreas=Common.Region_English,timeToWait=300)               
            if English_Main[0][1]:
                Duration = time.clock() - Start_Time
                EnglishTup.append(Duration) 
                EnglishAverage = sum(EnglishTup)/len(EnglishTup) 
                step_comment = "Launched Sucessfully in %s Seconds " %Duration
                step_result = StormTest.TM.PASS
                StormTest.EndTestStep(step_name,step_result,step_comment)
            else:
                Duration = time.clock() - Start_Time
                step_comment = "Failed to Launch English"
                StormTest.CaptureImageEx(None,'English_Error.png')
                step_result = StormTest.TM.FAIL
                StormTest.EndTestStep(step_name,step_result,step_comment)
                English_Fail += 1
            
        else:
            print"FAILED TO LAUNCH ACTIVE SERVICES"
            English_NonExecuted += 1        
            step_comment = "FAILED TO LAUNCH ACTIVE SERVICES"
            StormTest.CaptureImageEx(None,'step.png')
            step_result = StormTest.TM.FAIL            
            StormTest.EndTestStep(step_name,step_result,step_comment)    
            
        English_PASS=(English_Launched - English_Fail)            
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Total Executions = ", English_Launched
    print "Fail in Executions = ", English_NonExecuted
    print "Launched Sucessfully %d times" %English_PASS
    print "Failed to Launch English %d times" %English_Fail
    print "Average time for loading English is %d Seconds" %EnglishAverage                        
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if English_Fail>=1:
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch English %d times." %English_Fail
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Launched Sucessfully %d times. Average time is %d Seconds" %(English_PASS,EnglishAverage)
    StormTest.EndTestStep("ACTIVE_English",step_result,step_comment)  


########################################################################################
# TestCase                    : 2
# TestCase Description        : Test whether App is able to launch Games
#########################################################################################

def Games():
    Games_Launched = TotalExecutions
    Games_PASS = PassExecutions
    Games_Fail = FailExecutions
    Games_NonExecuted = 0
    StormTest.BeginTestStep("ACTIVE_Games")
    for i in range(Games_Launched):
        k = i+1
        step_name = "ITTERATION %d:::" %k
        StormTest.BeginTestStep(step_name)
        Common.VDL_RebootSTB()
        Common.VDL_Cisco_Active()
        StormTest.WaitSec(10)
        ACT_MAIN = StormTest.WaitImageMatch(Common.Img_Active_Main,percent=70,includedAreas=Common.Region_Active,timeToWait=20)        
        if ACT_MAIN[0][1]:
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Ok)
            Start_Time = time.clock()            
            Games_Main = StormTest.WaitImageMatch(Common.Img_Games_Main, percent=90, includedAreas=Common.Region_Games,timeToWait=300)               
            if Games_Main[0][1]:
                Duration = time.clock() - Start_Time
                GamesTup.append(Duration) 
                GamesAverage = sum(GamesTup)/len(GamesTup) 
                step_comment = "Launched Sucessfully in %s Seconds" %Duration
                step_result = StormTest.TM.PASS
                StormTest.EndTestStep(step_name,step_result,step_comment)
            else:
                Duration = time.clock() - Start_Time
                step_comment = "Failed to Launch Games"
                StormTest.CaptureImageEx(None,'Games_Error.png')
                step_result = StormTest.TM.FAIL
                StormTest.EndTestStep(step_name,step_result,step_comment)
                Games_Fail += 1
            
        else:
            print"FAILED TO LAUNCH ACTIVE SERVICES"
            Games_NonExecuted += 1        
            step_comment = "FAILED TO LAUNCH ACTIVE SERVICES"
            StormTest.CaptureImageEx(None,'step.png')
            step_result = StormTest.TM.FAIL            
            StormTest.EndTestStep(step_name,step_result,step_comment)    
            
        Games_PASS=(Games_Launched-Games_Fail)            
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Total Executions = ", Games_Launched
    print "Fail in Executions = ", Games_NonExecuted
    print "Launched Sucessfully %d times" %Games_PASS
    print "Failed to Launch Games %d times" %Games_Fail
    print "Average time for loading Games is %d Seconds" %GamesAverage                        
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if Games_Fail>=1:
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch Games %d times." %Games_Fail
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Launched Sucessfully %d times. Average time is %d Seconds" %(Games_PASS,GamesAverage)    
    StormTest.EndTestStep("ACTIVE_Games",step_result,step_comment)    

########################################################################################
# TestCase                    : 3
# TestCase Description        : Test whether App is able to launch KIDS
#########################################################################################
def Kids():
    Kids_Launched = TotalExecutions
    Kids_PASS = PassExecutions
    Kids_Fail = FailExecutions
    Kids_NonExecuted = 0
    StormTest.BeginTestStep("ACTIVE_KIDS")
    for i in range(Kids_Launched):
        k = i+1
        step_name = "ITTERATION %d:::" %k
        StormTest.BeginTestStep(step_name)
        Common.VDL_RebootSTB()
        Common.VDL_Cisco_Active()
        StormTest.WaitSec(10)
        ACT_MAIN = StormTest.WaitImageMatch(Common.Img_Active_Main,percent=70,includedAreas=Common.Region_Active,timeToWait=20)        
        if ACT_MAIN[0][1]:
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Ok)
            Start_Time = time.clock()            
            Kids_Main = StormTest.WaitImageMatch(Common.Img_Kids_Main, percent=90, includedAreas=Common.Region_Kids,timeToWait=300)               
            if Kids_Main[0][1]:
                Duration = time.clock() - Start_Time
                KidsTup.append(Duration) 
                KidsAverage = sum(KidsTup)/len(KidsTup) 
                step_comment = "Launched Sucessfully in %s Seconds " %Duration
                step_result = StormTest.TM.PASS
                StormTest.EndTestStep(step_name,step_result,step_comment)
            else:
                Duration = time.clock() - Start_Time
                step_comment = "Failed to Launch Kids"
                StormTest.CaptureImageEx(None,'Kids_Error.png')
                step_result = StormTest.TM.FAIL
                StormTest.EndTestStep(step_name,step_result,step_comment)
                Kids_Fail += 1
            
        else:
            print"FAILED TO LAUNCH ACTIVE SERVICES"
            Kids_NonExecuted += 1        
            step_comment = "FAILED TO LAUNCH ACTIVE SERVICES"
            StormTest.CaptureImageEx(None,'step.png')
            step_result = StormTest.TM.FAIL            
            StormTest.EndTestStep(step_name,step_result,step_comment)    
            
        Kids_PASS=(Kids_Launched-Kids_Fail)            
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Total Executions = ", Kids_Launched
    print "Fail in Executions = ", Kids_NonExecuted
    print "Launched Sucessfully %d times" %Kids_PASS
    print "Failed to Launch Kids %d times" %Kids_Fail
    print "Average time for loading Kids is %d Seconds" %KidsAverage                        
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if Kids_Fail>=1:
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch Kids %d times." %Kids_Fail
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Launched Sucessfully %d times. Average time is %d Seconds" %(Kids_PASS,KidsAverage)   
    StormTest.EndTestStep("ACTIVE_KIDS",step_result,step_comment)


########################################################################################
# TestCase                    : 4
# TestCase Description        : Test whether App is able to launch StateActive
#########################################################################################
def StateActive():
    StateActive_Launched = TotalExecutions
    StateActive_PASS = PassExecutions
    StateActive_Fail = FailExecutions
    StateActive_NonExecuted = 0
    StormTest.BeginTestStep("ACTIVE_StateActive")
    for i in range(StateActive_Launched):
        k = i+1
        step_name = "ITTERATION %d:::" %k
        StormTest.BeginTestStep(step_name)
        Common.VDL_RebootSTB()
        Common.VDL_Cisco_Active()
        StormTest.WaitSec(10)
        ACT_MAIN = StormTest.WaitImageMatch(Common.Img_Active_Main,percent=70,includedAreas=Common.Region_Active,timeToWait=20)        
        if ACT_MAIN[0][1]:
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Ok)
            Start_Time = time.clock()            
            StateActive_Main = StormTest.WaitImageMatch(Common.Img_StateActive_Main, percent=90, includedAreas=Common.Region_StateActive,timeToWait=300)               
            if StateActive_Main[0][1]:
                Duration = time.clock() - Start_Time
                StateActiveTup.append(Duration) 
                StateActiveAverage = sum(StateActiveTup)/len(StateActiveTup) 
                step_comment = "Launched Sucessfully in %s Seconds" %Duration
                step_result = StormTest.TM.PASS
                StormTest.EndTestStep(step_name,step_result,step_comment)
            else:
                Duration = time.clock() - Start_Time
                step_comment = "Failed to Launch StateActive"
                StormTest.CaptureImageEx(None,'StateActive_Error.png')
                step_result = StormTest.TM.FAIL
                StormTest.EndTestStep(step_name,step_result,step_comment)
                StateActive_Fail += 1
            
        else:
            print"FAILED TO LAUNCH ACTIVE SERVICES"
            StateActive_NonExecuted += 1        
            step_comment = "FAILED TO LAUNCH ACTIVE SERVICES"
            StormTest.CaptureImageEx(None,'step.png')
            step_result = StormTest.TM.FAIL            
            StormTest.EndTestStep(step_name,step_result,step_comment)    
            
        StateActive_PASS=(StateActive_Launched-StateActive_Fail)            
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Total Executions = ", StateActive_Launched
    print "Fail in Executions = ", StateActive_NonExecuted
    print "Launched Sucessfully %d times" %StateActive_PASS
    print "Failed to Launch StateActive %d times" %StateActive_Fail
    print "Average time for loading StateActive is %d Seconds" %StateActiveAverage                        
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if StateActive_Fail>=1:
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch StateActive %d times." %StateActive_Fail
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Launched Sucessfully %d times. Average time is %d Seconds" %(StateActive_PASS, StateActiveAverage)        
    StormTest.EndTestStep("ACTIVE_StateActive",step_result,step_comment)    


########################################################################################
# TestCase                    : 5
# TestCase Description        : Test whether App is able to launch Assistance
#########################################################################################
def Assistance():
    Assistance_Launched = TotalExecutions
    Assistance_PASS = PassExecutions
    Assistance_Fail = FailExecutions
    Assistance_NonExecuted = 0
    StormTest.BeginTestStep("ACTIVE_Assistance")
    for i in range(Assistance_Launched):
        k = i+1
        step_name = "ITTERATION %d:::" %k
        StormTest.BeginTestStep(step_name)
        Common.VDL_RebootSTB()
        Common.VDL_Cisco_Active()
        StormTest.WaitSec(10)
        ACT_MAIN = StormTest.WaitImageMatch(Common.Img_Active_Main,percent=70,includedAreas=Common.Region_Active,timeToWait=20)        
        if ACT_MAIN[0][1]:
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Down)
            StormTest.WaitSec(2)
            StormTest.PressButton(Common.RC_Ok)
            Start_Time = time.clock()            
            Assistance_Main = StormTest.WaitImageMatch(Common.Img_Assistance_Main, percent=90, includedAreas=Common.Region_Assistance,timeToWait=300)               
            if Assistance_Main[0][1]:
                Duration = time.clock() - Start_Time
                AssistanceTup.append(Duration) 
                AssistanceAverage = sum(AssistanceTup)/len(AssistanceTup) 
                step_comment = "Launched Sucessfully in %s Seconds " %Duration
                step_result = StormTest.TM.PASS
                StormTest.EndTestStep(step_name,step_result,step_comment)
            else:
                Duration = time.clock() - Start_Time
                step_comment = "Failed to Launch Assistance"
                StormTest.CaptureImageEx(None,'Assistance_Error.png')
                step_result = StormTest.TM.FAIL
                StormTest.EndTestStep(step_name,step_result,step_comment)
                Assistance_Fail += 1
            
        else:
            print"FAILED TO LAUNCH ACTIVE SERVICES"
            Assistance_NonExecuted += 1        
            step_comment = "FAILED TO LAUNCH ACTIVE SERVICES"
            StormTest.CaptureImageEx(None,'step.png')
            step_result = StormTest.TM.FAIL            
            StormTest.EndTestStep(step_name,step_result,step_comment)    
            
        Assistance_PASS=(Assistance_Launched-Assistance_Fail)            
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Total Executions = ", Assistance_Launched
    print "Fail in Executions = ", Assistance_NonExecuted
    print "Launched Sucessfully %d times" %Assistance_PASS
    print "Failed to Launch Assistance %d times" %Assistance_Fail
    print "Average time for loading Assistance is %d Seconds" %AssistanceAverage                        
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if Assistance_Fail>=1:
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch Assistance %d times." %Assistance_Fail
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Launched Sucessfully %d times. Average time is %d Seconds" %(Assistance_PASS,AssistanceAverage)
    StormTest.EndTestStep("ACTIVE_Assistance",step_result,step_comment)    


###############################################################################################    
def setupEnv():
    try:
          
        ret_value = StormTest.TM.PASS
        StormTest.ConnectToServer(Common.Server1, Common.User)
    
        # Reserves a slot on the server and start serial logging
        slot_is_free = StormTest.ReserveSlot( 1, Common.RC_KeySet, Common.logParam1, True )
     
        if slot_is_free:
            #Show Video
            StormTest.ShowVideo()
            #StormTest.StartVideoLog()
            English()
            Games()
            Kids()
            Assistance()
            StateActive()
            StormTest.CloseVideo()
            #StormTest.StopVideoLog()
            ret_value = StormTest.TM.PASS
            
        else:
            print "can not run, test slot is not free"
            ret_value = StormTest.TM.NOT_RUN
            
        
    except:
        print "Exception in the script"
        traceback.print_exc()
        ret_value = StormTest.TM.FAIL
    
    finally:
   
    # End of test - release ports back to the server
        StormTest.ReleaseServerConnection()

    # Return test result
        return ret_value


# So that this module can be used as reusable module, or as standalone program
if __name__ == '__main__':
    StormTest.ReturnTestResult(setupEnv())
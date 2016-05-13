############## Script Owned by:################################################
#  ______                          _   _                                      #
#  | ___ \                        | | | |                                     #
#  | |_/ / __ __ _ _ __   ___  ___| |_| |__                                   #
#  |  __/ '__/ _` | '_ \ / _ \/ _ \ __| '_ \                                  #
#  | |  | | | (_| | | | |  __/  __/ |_| | | |                                 #
#  \_|  |_|  \__,_|_| |_|\___|\___|\__|_| |_|                                 #
#                                                                             #
# Description : This file contains the test case related to Kids Main Page.   #
###############################################################################


######################################################################
#     FILES INCLUDED                                                 #
######################################################################
import stormtest.ClientAPI as StormTest
import Common
import traceback
import time


#TotalExecutions = int(input("Enter No.of Iterations you would like to repat..?: "))
TotalExecutions = 250
PassExecutions = 0
FailExecutions = 0

KidsTup = []
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
            Kids_Main = StormTest.WaitImageMatch(Common.Img_Kids_Main, percent=90, includedAreas=Common.Region_Kids,timeToWait=120)               
            if Kids_Main[0][1]:
                Duration = time.clock() - Start_Time
                KidsTup.append(Duration) 
                KidsAverage = sum(KidsTup)/len(KidsTup) 
                step_comment = "Launched Sucessfully in %2.3f Seconds " %Duration
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
            
        Kids_PASS = Kids_Launched-(Kids_Fail + Kids_NonExecuted)            
    print 'x' * 60
    print 'x' * 60
    print "x", "          Total Executions     =     " , Kids_Launched
    if Kids_NonExecuted > 0:
        print "x", "          Fail to Launch ACTIVE SERVICES %d times " %Kids_NonExecuted
    print "x", "          Launched Sucessfully %d times" %Kids_PASS  
    print "x", "          Failed to Launch Kids %d times" %Kids_Fail
    print "x", "          Average time for loading Kids is %d Seconds" %KidsAverage                      
    print 'x' * 60    
    print 'x' * 60
    if (Kids_Fail == Kids_Launched):
        step_result = StormTest.TM.FAIL
        step_comment = "Failed to Launch %d times." %Kids_Fail
    elif (Kids_Fail >= 1) and (Kids_Fail < Kids_Launched):
        step_result = StormTest.TM.PARTIAL_PASS
        step_comment = "Launched Sucessfully %d times:::Failed to Launch %d times:::Average Launch time: %dSeconds" %(Kids_PASS,Kids_Fail,KidsAverage)
    else:
        step_result = StormTest.TM.PASS
        step_comment = "Active Kids Launched Sucessfully %d times. Average time is %d Seconds" %(Kids_PASS,KidsAverage)   
    StormTest.EndTestStep("ACTIVE_KIDS",step_result,step_comment)


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
            Kids()
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
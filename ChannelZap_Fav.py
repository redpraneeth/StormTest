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

TotalZap = 100

Average = []



##############################################################################
# Local functions
#################################################################################
def SD2SD():    
    
    step_name = "Channel Zap Measurement SD to SD ::"
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.WaitSec(2)
    StormTest.PressDigits('1')
    StormTest.WaitSec(10)
    StormTest.BeginTestStep(step_name)        
    zap_region = (270, 140, 1400, 650)
    zap_results = []
    
    for i in range (TotalZap):
        if StormTest.ReserveVideoTimer():
            zapStatus= StormTest.StartZapMeasurement(Common.RC_ChnPlus, 0, zap_region, colorCount=5000, timeout=15.0)
            StormTest.PressButton(Common.RC_ChnPlus)
            StormTest.WaitSec(15)
            zapTimes = StormTest.GetZapTimes()
            print str(zapTimes)
            
            #if the zapping went fine, add the result to the zapping list
            if zapTimes[0][1]:
                zap_results.append(zapTimes[0][3])
            else:
                StormTest.CaptureImageEx(None,"step.png")

            StormTest.FreeVideoTimer()
    
    #Check if there is at least one result in the list of zapping
    if len(zap_results):
        #Calculate the average zapping time
        zap_average = sum(zap_results)/len(zap_results) 
        #format the result so that we have only 3 digits after the dot
        message = str("Average zap time is %2.3f seconds" %zap_average)        
        status = StormTest.TM.PASS
    else:
        message = "No Zap detected: timed out"  
        StormTest.CaptureImageEx(None,'step.png')
        status = StormTest.TM.FAIL
        return StormTest.TM.FAIL

    StormTest.EndTestStep(step_name, status, message )


def HD2HD():    
    
    step_name = "Channel Zap Measurement HD to HD ::"
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.WaitSec(2)
    StormTest.PressDigits('21')
    StormTest.WaitSec(20)
    StormTest.BeginTestStep(step_name)        
    zap_region = (270, 140, 1400, 650)
    zap_results = []
    
    for i in range (TotalZap):
        if StormTest.ReserveVideoTimer():
            zapStatus= StormTest.StartZapMeasurement(Common.RC_ChnPlus, 0, zap_region, colorCount=5000, timeout=15.0)
            StormTest.PressButton(Common.RC_ChnPlus)
            StormTest.WaitSec(15)
            zapTimes = StormTest.GetZapTimes()
            print str(zapTimes)
            
            #if the zapping went fine, add the result to the zapping list
            if zapTimes[0][1]:
                zap_results.append(zapTimes[0][3])
            else:
                StormTest.CaptureImageEx(None,"step.png")
                
            StormTest.FreeVideoTimer()
    
    #Check if there is at least one result in the list of zapping
    if len(zap_results):
        #Calculate the average zapping time
        zap_average = sum(zap_results)/len(zap_results) 
        #format the result so that we have only 3 digits after the dot
        message = str("Average zap time is %2.3f seconds" %zap_average)        
        status = StormTest.TM.PASS
    else:
        message = "No Zap detected: timed out"  
        StormTest.CaptureImageEx(None,'step.png')
        status = StormTest.TM.FAIL
        return StormTest.TM.FAIL

    StormTest.EndTestStep(step_name, status, message )


def SD2HD():    

    step_name = "Channel Zap Measurement SD to HD (vice-versa) ::"
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.PressButton(Common.RC_Exit)
    StormTest.WaitSec(2)
    StormTest.PressDigits('61')
    StormTest.WaitSec(10)
    StormTest.BeginTestStep(step_name)        
    zap_region = (270, 140, 1400, 650)
    zap_results = []
    
    for i in range (TotalZap):
        if StormTest.ReserveVideoTimer():
            zapStatus= StormTest.StartZapMeasurement(Common.RC_ChnPlus, 0, zap_region, colorCount=5000, timeout=5.0)
            StormTest.PressButton(Common.RC_ChnPlus)
            StormTest.WaitSec(15)
            zapTimes = StormTest.GetZapTimes()
            print str(zapTimes)
            
            #if the zapping went fine, add the result to the zapping list
            if zapTimes[0][1]:
                zap_results.append(zapTimes[0][3])
            else:
                StormTest.CaptureImageEx(None,"step.png")

            StormTest.FreeVideoTimer()
    
    #Check if there is at least one result in the list of zapping
    if len(zap_results):
        #Calculate the average zapping time
        zap_average = sum(zap_results)/len(zap_results) 
        #format the result so that we have only 3 digits after the dot
        message = str("Average zap time is %2.3f seconds" %zap_average)        
        status = StormTest.TM.PASS
    else:
        message = "No Zap detected: timed out"  
        StormTest.CaptureImageEx(None,'step.png')
        status = StormTest.TM.FAIL
        return StormTest.TM.FAIL

    StormTest.EndTestStep(step_name, status, message )






    
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
            Common.VDL_RebootSTB()            
            SD2SD()
            HD2HD()
            SD2HD()
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
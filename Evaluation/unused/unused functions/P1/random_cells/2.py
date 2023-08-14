import subprocess 
import shlex

def systemcall ( cmdstr ):
    ''' System call to execute command string in a shell. '''
    try:
        retcode = subprocess.call( cmdstr, shell=True)
        if retcode != 0:
            print ("Error code:", retcode)
        return retcode
    except OSError as e:
        print ("Execution failed:", e )
        
def systemcall_pipe( cmdstr, allow=None, disp=True ):
    ''' System call to execute command string, to get stderr and stdout output in variable proc. '''
    # this function is superior to systemcall for use with Spyder where otherwise stdout/stderr are not visible.
    # it is also needed if your main program needs to capture this output instead of only print it to terminal.
    args = shlex.split(cmdstr)
    try:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #stdout and stderr from your process
        out, err = proc.communicate()
        retcode = proc.returncode
        if err:
            #decode the standard errors to readable form
            str_err = err.decode("utf-8")
            #Exclude error messages in allow list which are expected.
            bShow = True
            if allow:
                for allowstr in allow:
                    if allowstr in str_err:
                        bShow = False
            if bShow:
                print ("System command '{0}' produced stderr message:\n{1}".format(cmdstr, str_err))

        if disp:
            str_out = out.decode("utf-8")
            if str_out:
                print ("System command '{0}' produced stdout message:\n{1}".format(cmdstr, str_out))

        return retcode, out
    except OSError as e:
        print ("Execution failed:", e )
#An example of how to use these functions to provide a directory listing.
cmdstr = "ls"
print("The systemcall method doesn't show stdout when used in Jupyter notebook but does from a script.")
retcode = systemcall(cmdstr)
print("")
print("With systemcall_pipe you can see the stdout from Jupyter notebook, and can use the results in variables:")
stdout, stderr = systemcall_pipe(cmdstr)
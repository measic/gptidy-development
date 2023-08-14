import sys
print(sys.version_info)
# the major and minor version numbers are printed
print(sys.version_info[0],sys.version_info[1])
#if the following statement causes an error then your version is lower than v.3.0
assert sys.version_info >= (3,0)
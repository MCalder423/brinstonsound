__author__ = 'mcalder'
import sndhdr

def DescribeFile(filespec):
    return sndhdr.what(filespec)

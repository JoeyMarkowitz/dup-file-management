# Created: 2015.10.23
"""
1) hash all files indir and write hash and full path to db
2) query duplicate files and display all found with each line numbered.  select number of file to keep, rest move to a recycle folder or write full path rm to execute later after review
"""

import os
import sys
import hashlib

print(sys.version)
print ""

"""hash file"""
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


"""hash all files in dir"""
def hashdir(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            
            print "{} : {}".format(file_hash, os.path.abspath(path))

            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups





"""test"""
def testoswaslk():
	# Set the directory you want to start from
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir):
	    print "---dirname---"
	    print dirName
	    print "---subdirlist---"
	    print subdirList
	    print "---filelist---"
	    print fileList
	    print "============="
	    #print('Found directory: %s' % dirName)
	    #for fname in fileList:
	    #    print('\t%s' % fname)

hashdir( '.')





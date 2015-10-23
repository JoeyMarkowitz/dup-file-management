import os
import sys
import hashlib

print(sys.version)
print ""


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()



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





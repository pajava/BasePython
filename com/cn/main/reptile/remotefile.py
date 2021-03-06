__author__ = 'Main'

import socket, sys, time

host = sys.argv[1]
textport = "80"
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(textport)
    s.connect((host, port))
    fd = s.makefile('rw', 0)
    print "sleeping..."
    time.sleep(10)
    print "Continuing."
    fd.write("GET %s HTTP/1.0\r\n\r\n" % filename)
    fd.flush()
    s.shutdown(1)
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)

while 1:
    try:
        buf = fd.read(2048)
    except socket.error, e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)
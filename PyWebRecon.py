import socket
import sys
print "\n\n\n\n\n\n"
print "```````````````````````````````````````````````````"
print "       PyWebRecon v1.0 twitter.com/dibsyhex        "
print "```````````````````````````````````````````````````"
print "Current features"
print "[-]IP finder"
print "[-]Subdomain finder"
print "[-]Supported HTTP Methods Finder"
print "\n\n"
try:
        s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
        print "Failed to create socket"+str(msg)
        sys.exit()
#print "Socket Crieated"

host = 'www.kiit.ac.in'
host = raw_input("Enter hostname(eg, www.site.com):")
port = 80
try:
        ip=socket.gethostbyname(host)
        subdomain=socket.gethostbyaddr(host)
        print "-------------------------------"
        print "Host:",host
        print "IP address of ",host," is:",ip
        print "Subdomain of host is:",subdomain[0]
        print "--------------------------------"

        #Connect to port 80

        s1.connect((ip,port))
        sndmsg="GET / HTTP/1.1 \r\n\r\n"
        s1.sendall(sndmsg)
        rcvmsg=s1.recv(8192)
        print "\nServer Responded"
        print rcvmsg
        s1.close()



        #check all the suported methods supported by the webserver
        s2.connect((ip,port))
        sndmsg="OPTIONS / HTTP/1.1 \r\nHost:"+host+"\r\n\r\n\r\n"
        s2.sendall(sndmsg)
        rcvmsg=s2.recv(8192)
        print "\nSupported HTTP Methods"
        print rcvmsg
        s2.close()

except socket.error,msg:
        print "Hostname cannot be resolved"
        sys.exit()

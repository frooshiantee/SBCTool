#import wx
import os
substring = "unique"
sipSigFail = "SIP Signaling port cannot use "
mediaCheck = "failed to create entry"
privateIngressIp = ["216.82.224.202", "216.82.225.202", "67.231.8.89", "67.231.8.90", "192.168.3.88", "192.168.5.91", "192.168.8.91", "67.231.0.90", "192.168.8.90", "192.168.3.221", "67.231.5.51", "67.231.8.195", "192.168.5.22", "67.231.0.89", "67.231.4.195", "67.231.8.87", "192.168.6.221", "67.231.0.87", "192.168.6.220"];
# Provisioning Starts


def curlInitiator(sbcIp,zone,zoneId,sipSigPort,ipv4,sipTrunk,media,directMedia,nature):
    ipv4List=ipv4.split(",")
    if len(ipv4List) != len(sbcIp):
        return "List mismatch"
    #return sbcIp
#    print sbcList
#    print 'SBC', sbcip
#    print 'Zone', zone
 #   sbcList = sbcIp.keys()
    index = 0
    for i in sbcIp:
        print i
        ''' #uncomment for production
        if i == "x.x.x.x":                # Enter JFK CASBC IP address
            if nature == "privateTerm":
                media = "CORE_MEDIA"
            else:
                media = "CARRIER_MEDIA"
        elif i == "mention IP address for FK1-CASBC-03" or i == "mention IP address for FK1-CASBC-04" or i == "mention IP address for LABNBS-04":
            if nature == "privateTerm":
                media = "MEDIA"  
	else:
	    if nature == "privateTerm":
                media = "I_MEDIA"
            else:
                media = "E_MEDIA" ''' #uncomment for produiction

        os.system('curl -ksiX POST https://'+i+'/api/config/addressContext/default/ -H "authorization: Basic Q0FMVklORjpCV0NpbnQzcm4yMCE3" -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<zone> <name>'+zone+'</name><id>'+zoneId+'</id> </zone>"')
        log = os.popen('curl -ksiX POST https://'+i+'/api/config/addressContext/default/zone/'+zone+'/  -H "authorization: Basic Q0FMVklORjpCV0NpbnQzcm4yMCE3" -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<sipSigPort> <index>'+zoneId+'</index><state>enabled</state><ipInterfaceGroupName>'+sipSigPort+'</ipInterfaceGroupName><ipAddressV4>'+ipv4List[index]+'</ipAddressV4> </sipSigPort>"').read()
        index += 1
        if sipSigFail in log:
            return "SipSigFail"
        if substring in log:
            return "Fail"
        mediaLog = os.popen('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/'+zone+'/  -H "authorization: Basic Q0FMVklORjpCV0NpbnQzcm4yMCE3" -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<sipTrunkGroup> <name>'+sipTrunk+'</name><state>enabled</state><mode>inService</mode><media><mediaIpInterfaceGroupName>'+media+'</mediaIpInterfaceGroupName></media> </sipTrunkGroup>"').read()
        if mediaCheck in mediaLog:
            return "mediaFail"
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/'+zone+'/sipTrunkGroup/'+sipTrunk+'/signaling/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<rel100Support>disabled</rel100Support>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods  -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<message>reject</message>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<publish>reject</publish>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<refer>reject</refer>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<subscribe>reject</subscribe>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<notify>reject</notify>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<info>reject</info>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<register>reject</register>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/methods -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<update>reject</update>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/retryCounters -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<invite>2</invite>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/signaling/timers/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<sessionKeepalive>0</sessionKeepalive>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/services/longDurationCall/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<timeoutValue>"1440"</timeoutValue>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/services/longDurationCall/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<action>trapAndRelease</action>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/services/longDurationCall/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<relCause>41</relCause>"')
        os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/services/  -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<dnsSupportType>a-srv-naptr</dnsSupportType>"')
        if directMedia == 'enabled':
            print os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/media/  -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<directMediaAllowed>enabled</directMediaAllowed>"')
            print os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/' + zone + '/sipTrunkGroup/' + sipTrunk + '/media/  -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<lateMediaSupport>passthru</lateMediaSupport>"')
        if nature == 'privateTerm':
            for ip in privateIngressIp:
                #print ip
                print os.system('curl -ksiX POST https://' + i + '/api/config/addressContext/default/zone/'+zone+'/sipTrunkGroup/'+sipTrunk+'/ -H "authorization: Basic " -H "cache-control: no-cache" -H "Content-type:application/vnd.yang.data+xml" --data "<ingressIpPrefix><ipAddress>'+ip+'</ipAddress> <prefixLength>'+"32"+'</prefixLength></ingressIpPrefix>  "')

	print '******************'
        print log
        print '*****************************************************************************************************************'
        print '*****************************************************************************************************************'
    return "Success!!!"
#Provisioning Ends

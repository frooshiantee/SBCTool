import os
from flask import Flask, render_template, request, flash
from curlinitiator import curlInitiator
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def Origination():
    return render_template('Origination.html')

@app.route('/', methods=['GET', 'POST'])
def Origination_post():
    sbcIp = request.form.getlist('sbcIp')
    zone = request.form['zoneName']
    zoneId = request.form['zoneID']
    sipSigPort = request.form['sipSigPort']
    ipv4 = request.form['ipv4']
    sipTrunk = request.form['sipTrunk']
    media = "CORE_MEDIA"            #delete this line for production
    directMedia = request.form['directMedia']
    nature = "origination"
    length = len(sbcIp)
    if length<1:
        flash("Select atleast one SBC")
    result = curlInitiator(sbcIp,zone,zoneId,sipSigPort,ipv4,sipTrunk,media,directMedia,nature)

    if result == "Fail" :
        flash("ERROR!!!IP address / port number must be unique within an address context")
        return render_template('IPFail.html')
    elif result == "SipSigFail" :
        flash ("ERROR!!!SIP Signaling port cannot use interface group with interfaces on multiple NPs")
        return render_template('SipSigFail.html')
    elif result == "mediaFail" :
        flash("ERROR!!!Enter Appropriate Media Interface Group Name")
        return render_template('mediaFail.html')
    else:
        flash(sbcIp)
        return render_template('success.html')

@app.route('/PublicTerm/')
def PublicTerm():
    return render_template('PublicTerm.html')
	
@app.route('/PublicTerm/', methods=['GET', 'POST'])
def PublicTerm_post():
    sbcIp = request.form.getlist('sbcIp')
    zone = request.form['zoneName']
    zoneId = request.form['zoneID']
    sipSigPort = request.form['sipSigPort']
    ipv4 = request.form['ipv4']
    sipTrunk = request.form['sipTrunk']
    media = "CORE_MEDIA"    #delete this line for production
    directMedia = request.form['directMedia']
    nature = "publicTerm"
    
    result = curlInitiator(sbcIp,zone,zoneId,sipSigPort,ipv4,sipTrunk,media,directMedia,nature)

    if result == "Fail" :
        flash("ERROR!!!IP address / port number must be unique within an address context")
        return render_template('IPFail.html')
    elif result == "SipSigFail" :
        flash ("ERROR!!!SIP Signaling port cannot use interface group with interfaces on multiple NPs")
        return render_template('SipSigFail.html')
    elif result == "mediaFail" :
        flash("ERROR!!!Enter Appropriate Media Interface Group Name")
        return render_template('mediaFail.html')
    else:
        flash("Success!!!!")
        return render_template('success.html')	
	
	
@app.route('/PrivateTerm/')
def PrivateTerm():
    return render_template('PrivateTerm.html')
	
@app.route('/PrivateTerm/', methods=['GET', 'POST'])
def PrivateTerm_post():
    sbcIp = request.form.getlist('sbcIp')
    zone = request.form['zoneName']
    zoneId = request.form['zoneID']
    sipSigPort = request.form['sipSigPort']
    ipv4 = request.form['ipv4']
    sipTrunk = request.form['sipTrunk']
    media = "CORE_MEDIA"    #delete this line for production
    directMedia = request.form['directMedia']
    nature = "privateTerm"
    
    result = curlInitiator(sbcIp,zone,zoneId,sipSigPort,ipv4,sipTrunk,media,directMedia,nature)



    if result == "Fail" :
        flash("ERROR!!!IP address / port number must be unique within an address context")
        return render_template('IPFail.html')
    elif result == "SipSigFail" :
        flash ("ERROR!!!SIP Signaling port cannot use interface group with interfaces on multiple NPs")
        return render_template('SipSigFail.html')
    elif result == "mediaFail" :
        flash("ERROR!!!Enter Appropriate Media Interface Group Name")
        return render_template('mediaFail.html')
    else:
        flash("Success!!!!")
        return render_template('success.html')	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0")

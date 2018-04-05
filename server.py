from flask import Flask, render_template, request
import json

w=json.load(open("worldl.json"))
nc=int(len(w))

app = Flask(__name__)
for c in w:
    c['tld']=c['tld'][1:]
page_size=20
app=Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('index.html',
        nc=nc,
        w=w[0:page_size],
        page_size=page_size,
        page_number=0
        )     
                           
@app.route('/begin/<b>')
def beginPage(b):
	bn = int(b)
	return render_template('index.html',
        nc=int(len(w)),
		w = w[bn:bn+page_size],
		page_number = bn,
		page_size = page_size
		)
    
@app.route('/continent/<a>')
def continentPage(a):
    cl=[c for c in w if c['continent']==a]
    return render_template('continent.html',
            length_of_cl=len(cl),
            cl=cl,
            a=a
            )
    
@app.route('/countryByName/<n>')
def countryByNamePage(n):
    c=None
    for x in w:
        if x['name']==n:
            c=x
    return render_template(
        'country.html',
        nc=int(len(w)),
        c=c)
                        
@app.route('/country/<i>')
def countryPage(i):
    return render_template('country.html', c=w[int(i)])
    nc=int(len(w)),

@app.route('/delete/<n>')
def deleteCountry(n):
    i=0
    for c in w:
        if c['name']==n:
            break
        i=i+1
    del w[i]
    return render_template('index.html',
        w=w[0:page_size],
        nc=int(len(w)),
        page_size=page_size,
        page_number=0)

@app.route('/editcountryByName/<n>')
def editcountryByNamePage(n):
    c=None
    for x in w:
        if x['name']==n:
            c=x
    return render_template(
        'country-edit.html',
        nc=int(len(w)),
        c=c)

@app.route('/updatecountryByName')
def updatecountryByNamePage():
    n=request.args.get('country')
    c=None
    for x in w:
        if x['name']==n:
            c=x
    c['capital']=request.args.get('capital')
    c['continent']=request.args.get('continent')
    return render_template(
        'country.html',
        nc=int(len(w)),
        c=c)

@app.route('/createcountry/<n>')
def Createcountry(n):
    c=None
    for x in w:
        if x['name']==n:
            c=x
    
    return render_template(
        'createcountry.html',
        nc=int(len(w)),
                c=c)

@app.route('/updatecreatecountry')
def updatecreatecountry():
    n=request.args.get('country')
    #n=request.args.get('capital')
    #n=request.args.get('continent')
    #n=request.args.get('population')
    #n=request.args.get('gdp')
    #n=request.args.get('area')
    c=None
    for x in w:
        if x['name']==n:
            c=x
            c['country']=request.args.get('country')
            c['capital']=request.args.get('capital')
            c['continent']=request.args.get('continent')
            c['population']=request.args.get('population')
            c['gdp']=request.args.get('gdp')
            c['area']=request.args.get('area')

    return render_template('country.html',nc=int(len(w)),
        c=c)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5624,debug=True)

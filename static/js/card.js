var fileCount = 1000
var addtime
var sindex = 0
var path
var cnswf="cnswf"
var enswf="enswf"
    function changesrc(srcindex,srcpath) {
			var name
			if(srcpath==cnswf){
				name=2
			}
			if(srcpath==enswf){
				name=5
			}
			var box = document.getElementById('box')
			str = '<embed id="embedid" src="/static/img/card/'+srcpath+'/'+srcindex+'A'+name+'.swf" type="application/x-shockwave-flash"></embed>';
			box.innerHTML = str
	}
   
	function start() {
		addtime = document.getElementById('timegap').value*1000
		sindex=sindex+1
		if(sindex<=fileCount){
			changesrc(sindex,path)
			window.setTimeout("start()",addtime);
		}
    }
	
	function startcn(){
		path=cnswf
		start()
	}	
	function starten(){
		path=enswf
		start()
	}
	function refresh(){
		history.go(0) 
	}





var list = document.getElementsByClassName("entry");
function add_properties(entries,ini_index) {
	var i;
	for (i = ini_index; i < entries.length; i++) {
		temp=entries[i];
	    temp.onmouseover = function(){	
	     	((this.getElementsByTagName('span'))[1]).style.opacity=1;
	    	((this.getElementsByTagName('span'))[0]).style.opacity=1;
	    }
		temp.onmouseout = function(){
	     	((this.getElementsByTagName('span'))[1]).style.opacity=0;
	    	((this.getElementsByTagName('span'))[0]).style.opacity=0;
	    }
	    
	    	

	    
	}
}
// Activate all close buttons
add_properties(list,0);	

window.onscroll = function(){scrollFunction()};
            
function scrollFunction(){
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200){
        
        document.getElementById("black").style.background = "rgba(0,0,0,0.65)";
        
    }else{
        document.getElementById("black").style.background = "transparent";
        

    }
}
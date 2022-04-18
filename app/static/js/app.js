/* Add your Application JavaScript */

function showCountryNav(){
  console.log('this is some JavaScript code');
  var search = document.getElementById('phonenav')
  search.style.display = "none"
  var countryNavBar = document.getElementById('country-news-selector-id')
  var countryNavBarHolder = document.getElementById('country-options-holder')
  var float = document.getElementById('floating')

  var elements = document.getElementsByClassName('phone');
  
  for (var i in elements) {
    if (elements.hasOwnProperty(i)) {
      elements[i].classList.remove('show-class')
    }
  }


    if(countryNavBar.style.height === "50vh" || countryNavBar.style.height === "auto"){ 
      countryNavBarHolder.style.display = "none"
      countryNavBar.style.height = "0vh"
      float.style.position = "relative"
      
    }else{      
      countryNavBar.style.height = "50vh"
      const wait = setTimeout(()=>{
        countryNavBarHolder.style.display = "block"
        countryNavBar.style.height = "auto"
      float.style.position = "fixed"
      }, 700);

    }
}


function switchSlider(id){
  for(var i=0; i<6; i++){
    var countryNavBar = document.getElementById('slider-page-'+i)
    countryNavBar.style.display = "none"
  }

  var countryNavBar = document.getElementById('slider-page-'+id)
  countryNavBar.style.display = "block"  

  var elements = document.getElementsByClassName('circular-pagification');
    
  for (var i in elements) {
    if (elements.hasOwnProperty(i)) {
      elements[i].classList.remove('cpactive')
      
      
    }
    if (i==id){
      console.log(i)
      elements[id].classList.add('cpactive')
    }
    
  }

    
  
}


function showSearch(){
  var search = document.getElementById('input-search')
  search.style.display = "inline"

  var wait = setTimeout(() => {
    search.style.width = "150px"
  }, 10);
}

function hideSearch(){
  var search = document.getElementById('input-search')
  search.style.width = "0px"
  var wait = setTimeout(() => {
    search.style.display = "none"
  }, 600);
}

function next(id){

  var hide = document.getElementById('adInfo1')
  hide.style.display = "none"
  var hide = document.getElementById('adInfo2')
  hide.style.display = "none"
  var hide = document.getElementById('adInfo3')
  hide.style.display = "none"
  

  var search = document.getElementById('adInfo'+id)
  search.style.display = "block"
}


function showNav(){
  var search = document.getElementById('phonenav')
  var elements = document.getElementsByClassName('phone');
  var countryNavBarHolder = document.getElementById('country-options-holder')
  var countryNavBar = document.getElementById('country-news-selector-id')
  countryNavBarHolder.style.display = "none"
  countryNavBar.style.height = "0vh"

  if(search.style.display === "none"){
      search.style.display = "block"
      for (var i in elements) {
        if (elements.hasOwnProperty(i)) {
          elements[i].classList.add('show-class')
        }
      }
  }else{
    search.style.display = "none"
    for (var i in elements) {
      if (elements.hasOwnProperty(i)) {
        elements[i].classList.remove('show-class')
      }
    }
  }
  
  
}
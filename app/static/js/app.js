/* Add your Application JavaScript */
function showCountryNav(){
  console.log('this is some JavaScript code');

  var countryNavBar = document.getElementById('country-news-selector-id')
  var countryNavBarHolder = document.getElementById('country-options-holder')

    if(countryNavBar.style.height === "50vh" || countryNavBar.style.height === "auto"){ 
      countryNavBarHolder.style.display = "none"
      countryNavBar.style.height = "0vh"
    }else{      
      countryNavBar.style.height = "50vh"
      const wait = setTimeout(()=>{
        countryNavBarHolder.style.display = "block"
        countryNavBar.style.height = "auto"
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

  for(var i=0; i<6; i++){
    var bulleting = document.getElementsByClassName('circular-pagification')[i]
    bulleting.classList.remove('cpactive')
  }

  var bulleting = document.getElementsByClassName('circular-pagification')[id]
    bulleting.classList.add('cpactive')

  
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
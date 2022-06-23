let dict={}
function displayStuff(response) {
  let stuff = JSON.parse(response);
  let div_html = ""
  for (let m of Object.keys(stuff)) {
    div_html+=stuff[m][4]
    console.log(stuff[m][4])
  }
  currentlyindoc=document.getElementById("allactualreviewslisted").innerHTML
  document.getElementById("allactualreviewslisted").innerHTML=currentlyindoc+div_html+"<br>"
  // console.log(document.getElementById("CSE 101").innerHTML)
}

function ratingReviewJSON(params) {
  JSON.stringify(params)
}
function actuallysubmit(){
  valm=document.getElementById("rating").value
  valn=document.getElementById("review").value
  valubit=document.getElementById("ubit").value
  csecode=document.getElementById("coursename").value
  let RatingReview = {"numericalvalue": valm, "statement": valn,"ubit":valubit,"csecode":csecode};
  let ratingReviewJSON=JSON.stringify(RatingReview)
  
  ajaxPostRequest("/putreview", ratingReviewJSON, displayStuff)
  document.getElementById("ubit").value = ""
	document.getElementById("rating").value = ""
	document.getElementById("review").value = ""
}
function kindasubmit() {
  valm=document.getElementById("rating").value
  valn=document.getElementById("review").value
  valubit=document.getElementById("ubit").value
  csecode=document.getElementById("coursename").value
  let RatingReview = {"numericalvalue": valm, "statement": valn,"ubit":valubit,"csecode":csecode};
  document.getElementById("ubit").value = ""
	document.getElementById("rating").value = ""
	document.getElementById("review").value = ""
}
// function listify(lister) {
//   jj=JSON.parse(lister)
//   valm=document.getElementById("filterbytopic").value
//   return 
// }
function whatcomesnext(params) {
  valm=document.getElementById("filterbytopic").value
  valn=document.getElementById("review").value
  valubit=document.getElementById("ubit").value
  csecode=document.getElementById("coursename").value
  let ratingReviewJSON=JSON.stringify([valm])
  ajaxPostRequest("/gimmietheDATA",ratingReviewJSON, listify)
}
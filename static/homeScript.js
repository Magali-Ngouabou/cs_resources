// Send the same request
function fetchData(category) {

  // var route = new URL('/app')
  // var params = {category:category} // or:
  // route.search = new URLSearchParams(params).toString();
  
  fetch('/app?category='+category)
      .then(function (result) {
          return result.json(); // But parse it as JSON this time
      })
      .then(function (response) {
          dataDiv = document.getElementById('data-'+category);
          console.log(response);
         
          for (x in response) {
            
            paragraphElem = document.createElement('p');
            linkElement = document.createElement('a');
            linkElement.innerText = response[x][0];
            linkElement.href = response[x][1];
            linkElement.target = "_blank"
            paragraphElem.append(linkElement);
            dataDiv.appendChild(paragraphElem);
          }        
          
      })
    }
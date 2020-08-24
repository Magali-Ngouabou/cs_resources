//import * as Papa from 'papaparse';
//const fetch = require("node-fetch");
// function init() {
//   Papa.parse('https://docs.google.com/spreadsheets/d/1kX_YT4AB2TjMurYKjmkvKrSix0C51lIkaHXBVpbx8r0/edit?usp=sharing', {
//     download: true,
//     header: true,
//     skipEmptyLines: true,
//     complete: function(results) {
//       var data = results.data
//       var errors = results.errors
//       var headers = results.meta.fields
//       //document.getElementById("Internships/paid opportunities").innerHTML = "<strong>Opportunities:</strong> " + [ data[0].Name, data[1].Name, data[2].Name ].join(", ")
//       //data = data.map(element => ({Internships: element.ID, Date: element.Date}))
//       //alert("Successfully processed " + data.length + " rows!")
//       console.log(data[0])
//     }
//   })

//   window.addEventListener('DOMContentLoaded', init)
// }

// fetch('/app')
//     .then(function (result) {
//         return result.text();
//     }).then(function (text) {
//         console.log('Result text:');
//         console.log(text); // Print the greeting as text
//     });

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
          
         
          for (x in response) {
            
            paragraphElem = document.createElement('p');
            linkElement = document.createElement('a');
            linkElement.innerText = x;
            linkElement.href = response[x];
            linkElement.target = "_blank"
            paragraphElem.append(linkElement);
            dataDiv.appendChild(paragraphElem);
          }        
          
      })
    }
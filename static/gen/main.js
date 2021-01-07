// const puppeteer = require('puppeteer');
// let page = null;
// let browser = null;
// (async () => {
//   browser = await puppeteer.launch();
//   page = await browser.newPage();

  
  
// })();

async function linkData(link) {
  fetch('/pageInfo?link='+link) 
    .then(function (response) {
        let result = response.json();
        console.log(result);
        return result;
    })
}

// Send the request to our app.py server
// that will then request info from the google api
// that gives us access to our google sheet database
// about the specified category
function fetchData(category) {
  
  // query our server with the category
  fetch('/app?category='+category)
      .then(function (result) {
          return result.json(); // But parse it as JSON this time
      })
      .then(async function (response) { // the output from previous 'then' is turned into useful data
          dataDiv = document.getElementById('data-'+category); // get the div box with this id
          console.log(response);
         
          for (x in response) { // go through each row of data in the excel json returned
            
            paragraphElem = document.createElement('p');

            // adds all the necessary info from the sheet into an element
            linkElement = document.createElement('a');
            imageElement = document.createElement('img');
          
            imageElement.src = linkData(response[x][1]).img;
            console.log("hello");
            linkElement.innerText = response[x][0];
            linkElement.href = response[x][1];
            linkElement.target = "_blank" // opens the link into a new window or tab
            linkElement.className = "link-box"; // allow to style in CSS

            paragraphElem.append(linkElement); // puts link element into paragraph
            paragraphElem.append(imageElement);
            dataDiv.appendChild(paragraphElem); // adds the links in the order they appear in sheet
          }        
         
          await browser.close();
      })
    }


  async function getTitle (page) {// mark function as being async; allow other things to run/load

    // function we pass into evaluate to extract title (could be written as separate function and pass as arg)
    const title = await page.evaluate(() => {
    const ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle != null && ogTitle.content.length > 0) { //if the fb title is there, grab it
      return ogTitle.content;
    }

    const twitterTitle = document.querySelector('meta[name="twitter:title"]');
    if (twitterTitle != null && twitterTitle.content.length > 0) { // if the twitter meta tag is there, grab it
      return twitterTitle.content;
    }

    const docTitle = document.title;
    if (docTitle != null && docTitle.length >0) { // check for the title in the meta tag, grab that
      return docTitle;
    }

    const h1 = document.querySelector("h1").innerHTML; // grab h1 if title is not there
    if (h1 != null && h1.length > 0) {
      return h1;
    }

    const h2 = document.querySelector("h2").innerHTML;
    if (h2 != null && h2.length > 0) { // if h1 fails, go to h2!
      return h2;
    }
    return null; // if nothing works out, we got nothing :(
  });
  return title; // return what we got from page.evaluate
}
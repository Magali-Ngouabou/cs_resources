function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Custom Menu')
     .addItem('Extract', 'extractData')
     .addToUi();
}
//355525519735-k89q519t72j1q6hrvm4r6449i5djq9gt.apps.googleusercontent.com
//UCyUCMjOclfhBGgqWQ621W2k              
function extractData() {
  // select the range from the Summary sheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Sheet1");
  //var lastRow = sheet.getLastRow();
  
  var range = sheet.getDataRange();
  var values = range.getValues();
  for (var i = 0; i < values.length; i++) {
    var col = "";
    for (var j = 0; j < values[i].length; j++) {
      if (values[j][i]) {
        col = col + ", " + values[j][i];
      }
    //col = col + ", ";
    }
  Logger.log(col);
  }
  // create timestamp to mark when communication was sent
  var timestamp = new Date(); 
  return col;
}
        

const webdriver = require('selenium-webdriver');
var chromeCapabilities = webdriver.Capabilities.chrome();

var driver = new webdriver.Builder().
  usingServer('http://selenium_hub:4444/wd/hub').
  withCapabilities(chromeCapabilities).
  build();

console.log(driver)

driver.get('https://www.google.com').then(function(){
  driver.findElement(webdriver.By.name('q')).sendKeys('webdriver\n').then(function(){
    driver.getTitle().then(function(title) {
      console.log(title);
      if(title === 'webdriver - Google Search') {
         console.log('Test passed');
      } else {
         console.log('Test failed');
      }      
      driver.quit();
    });
  });
});
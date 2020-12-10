const webdriver = require('selenium-webdriver');
var chromeCapabilities = webdriver.Capabilities.chrome();

console.log(chromeCapabilities)

// console.log(driver)
// const {Builder, By, Key, until} = require('selenium-webdriver');
// var driver = new Builder().forBrowser('internet explorer').build();

async function basicExample(){
    try{
        var driver = new webdriver.Builder().
        withCapabilities(chromeCapabilities).
        build();

        await driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html');

        await driver.getTitle().then(function(title) {
                    console.log("The title is: " + title)
            });

        driver.quit();
    }

    catch(err){
        handleFailure(err, driver)
    }

}

basicExample();

function handleFailure(err, driver) {
     console.error('Something went wrong!\n', err.stack, '\n');
     driver.quit();
} 

// driver.get('https://www.google.com').then(function(){
//   driver.findElement(webdriver.By.name('q')).sendKeys('webdriver\n').then(function(){
//     driver.getTitle().then(function(title) {
//       console.log(title);
//       if(title === 'webdriver - Google Search') {
//          console.log('Test passed');
//       } else {
//          console.log('Test failed');
//       }      
//       driver.quit();
//     });
//   });
// });
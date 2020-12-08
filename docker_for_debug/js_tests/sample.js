// yarn addで入れたpackageを利用する時はrequireを使う
webdriver = require("selenium-webdriver")

var driver = new webdriver.Builder()
.withCapabilities({'browserName': 'chrome','name':'Chrome Test','tz':'America/Los_Angeles','build':'Chrome Build','idleTimeout':'60'})
.usingServer('http://selenium_hub:4444/wd/hub')
.build();

// describe("入力フォーム デモ", () => {
//     before(() => {
//         var driver = new webdriver.Builder()
//         .withCapabilities({'browserName': 'chrome','name':'Chrome Test','tz':'America/Los_Angeles','build':'Chrome Build','idleTimeout':'60'})
//         .usingServer('http://selenium_hub:4444/wd/hub')
//         .build();
//         process.on("unhandledRejection", console.dir);
//     });
  
//     after(() => {
//       return driver.quit();
//     });
  
//     it("名前欄の必須入力チェック その1", async () => {
//       // テスト対象のページへアクセス
//       await driver.get(
//         "http://ics-drive.jp/sandbox/demo/demo.html"
//       );
  
//       // 何も入力せずにSubmitする
//       await driver.findElement(By.id("submitButton")).click();
  
//       // エラーメッセージを取得して、エラー文言が正しいかチェックする
//       const errorMessage = await driver
//         .findElement(By.id("error_name"))
//         .getText();
//       assert.equal(errorMessage, "名前を入力してください。");
//     });
  
//     it("名前欄の必須入力チェック その2", async () => {
//       // テスト対象のページへアクセス
//       await driver.get(
//         "http://ics-drive.jp/sandbox/demo/demo.html"
//       );
  
//       // 名前を入力してSubmitする
//       await driver
//         .findElement(By.id("name"))
//         .sendKeys("品川太郎");
//       await driver.findElement(By.id("submitButton")).click();
  
//       // エラーメッセージを取得して、エラー文言が空であるかチェックする
//       const errorMessage = await driver
//         .findElement(By.id("error_name"))
//         .getText();
//       assert.equal(errorMessage, "");
//     });
//   });

// testはdescribeに記載

describe('Google Search', function() {
    // timeoutの問題がある時は以下でdefault値(2000msec)を変更する
    // アロー関数の時は使えないので注意（https://github.com/mochajs/mocha/issues/2018）
    this.timeout(20000);

    // // mochaはtestする前にbefore関数で書かれた内容を一度実行する
    before(function(done) {
        // pythonの時と同じようにselenium hubに向けてリクエストを送りテストをする事が出来る。
        // ?? nodeは今chromeしか立ててないのでfirefoxだと怒られるそう。どうなるか？
        // var driver = new webdriver.Builder()
        // .withCapabilities({'browserName': 'chrome','name':'Chrome Test','tz':'America/Los_Angeles','build':'Chrome Build','idleTimeout':'60'})
        // .usingServer('http://selenium_hub:4444/wd/hub')
        // .build();

        // error handling - if you want do st
        // process.on('uncaughtException', function(err) {
        //     console.log("My error handler... " + err);

        //     if (driver) {
        //         //recording screenshot
        //         driver.takeScreenshot().then(function(img) {
        //             fs.writeFileSync("/tmp/test.png", new Buffer(img, 'base64'));
        //         });
        //     }
        // });
    });

    // mochaはテストが終わった後にafterで書かれた部分を実行する
    after(function(done) {
        // works with promise
        driver.quit().then(done);
    });

    
    it('should work', function(done) {
        // open start page
        driver.get('http://google.com').then(function() {
            console.log("open google.com...");
            done();
        });

    //     var searchBox = driver.findElement(webdriver.By.name('q'));

    //     searchBox.sendKeys('webdriver\n').then(function() {
    //         return searchBox.getAttribute('value');
    //     }).then(function(value) {
    //         assert.equal(value, 'webxdriver');
    //         done();
    //     });

    });
});